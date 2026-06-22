#!/usr/bin/env python3
"""Run a DeepSeek batch pass over the pilot slice for one track.

Tracks (prompt template -> derived artifact, source is NEVER modified):
  translate  prompts/translate.md  -> out/translate/<letter>.<lang>.jsonl
  lstargets  prompts/lstargets.md  -> out/lstargets/<letter>.jsonl
  struct     prompts/struct.md     -> out/struct/<letter>.jsonl
  ocrdiff    prompts/ocrdiff.md    -> out/ocrdiff/<letter>.jsonl   (needs --ab-diffs)

Provider is the OpenModel gateway (OpenAI-compatible). Configure via .env
(see .env.example):
  OPENMODEL_API_KEY=sk-...
  OPENMODEL_MODEL=deepseek-chat                 # bulk model
  OPENMODEL_BASE_URL=https://api.openmodel.ai/v1

Examples:
  python run_pilot.py --track struct --limit 3 --dry-run      # show a filled prompt, no API call
  python run_pilot.py --track translate --lang en --limit 20  # real calls (needs key)
  python run_pilot.py --track lstargets                       # full slice, resumes if re-run
"""
from __future__ import print_function
import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))

LANG_NAME = {"en": "English", "ru": "Russian", "de": "German"}


def load_env(path=os.path.join(HERE, ".env")):
    """Minimal .env loader (no python-dotenv dependency)."""
    env = {}
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    # process env overrides file
    for k in ("OPENMODEL_API_KEY", "OPENMODEL_MODEL", "OPENMODEL_BASE_URL", "OPENMODEL_MAX_TOKENS"):
        if os.environ.get(k):
            env[k] = os.environ[k]
    return env


def load_template(track):
    path = os.path.join(HERE, "prompts", "%s.md" % track)
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    # split on the first 'USER:' at line start
    m = re.search(r"^SYSTEM:\s*\n", text)
    u = re.search(r"^USER:\s*\n", text, re.M)
    if not (m and u):
        sys.exit("template %s missing SYSTEM:/USER: sections" % path)
    system = text[m.end():u.start()].strip()
    user = text[u.end():].strip()
    return system, user


def fill(tpl, rec, extra=None):
    vals = dict(rec)
    vals["h"] = rec.get("h") or ""
    if extra:
        vals.update(extra)
    out = tpl
    for k, v in vals.items():
        out = out.replace("{%s}" % k, str(v) if v is not None else "")
    return out


def read_jsonl(path):
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def done_ids(path):
    """Successfully-completed entry ids. Errored records are NOT counted, so a
    re-run retries them."""
    ids = set()
    if os.path.exists(path):
        for rec in read_jsonl(path):
            if "L" in rec and not rec.get("_error"):
                ids.add(rec["L"])
    return ids


def _extract_json(text):
    """Parse a JSON object out of model text, tolerating ```json fences / prose."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text).strip()
    try:
        return json.loads(text)
    except Exception:
        # fall back to the outermost {...} span
        s, e = text.find("{"), text.rfind("}")
        if s != -1 and e != -1 and e > s:
            return json.loads(text[s:e + 1])
        raise


def call_deepseek(env, system, user, max_retries=3):
    import requests  # imported lazily so --dry-run needs no network stack

    # OpenModel exposes the Anthropic Messages format at {base}/messages
    # (its OpenAI-format endpoint is the Responses API, not chat/completions).
    base = env.get("OPENMODEL_BASE_URL", "https://api.openmodel.ai/v1").rstrip("/")
    url = base + "/messages"
    payload = {
        "model": env.get("OPENMODEL_MODEL", "deepseek-chat"),
        "max_tokens": int(env.get("OPENMODEL_MAX_TOKENS", "16384")),
        "system": system + "\n\nRespond with ONLY the JSON object, no markdown fences.",
        "messages": [{"role": "user", "content": user}],
        "temperature": 0.0,
    }
    headers = {"x-api-key": env["OPENMODEL_API_KEY"],
               "anthropic-version": "2023-06-01",
               "content-type": "application/json"}
    for attempt in range(max_retries):
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=120)
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(min(2 ** attempt, 3))
                continue
            r.raise_for_status()
            blocks = r.json().get("content", [])
            text = "".join(b.get("text", "") for b in blocks if b.get("type") == "text")
            return _extract_json(text)
        except Exception as e:  # noqa: BLE001 - fail fast; resume passes mop up stragglers
            if attempt == max_retries - 1:
                return {"_error": str(e)}
            time.sleep(min(2 ** attempt, 3))
    return {"_error": "exhausted retries"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--track", required=True, choices=["translate", "lstargets", "struct", "ocrdiff"])
    ap.add_argument("--letter", default="j")
    ap.add_argument("--lang", default="en", help="translate track target language (en/ru)")
    ap.add_argument("--slice", default=None, help="override slice JSONL path")
    ap.add_argument("--ab-diffs", default=None, help="ocrdiff track: JSONL of {L,a_text,b_text} diffs")
    ap.add_argument("--limit", type=int, default=0, help="cap entries (0 = all)")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--dry-run", action="store_true", help="print first filled prompt, no API call")
    ap.add_argument("--env", default=os.path.join(HERE, ".env"),
                    help="path to .env (default deepseek_pilot/.env)")
    ap.add_argument("--model", default=None,
                    help="override OPENMODEL_MODEL (e.g. deepseek-v4-flash / deepseek-v4-pro)")
    args = ap.parse_args()

    slice_path = args.slice or os.path.join(HERE, "slice", "%s.jsonl" % args.letter)
    if args.track == "ocrdiff":
        if not args.ab_diffs:
            sys.exit("ocrdiff needs --ab-diffs (aligned A/B diffs from the AB v1e merge, #180/#163)")
        records = list(read_jsonl(args.ab_diffs))
    else:
        if not os.path.exists(slice_path):
            sys.exit("slice not found: %s (run extract_slice.py first)" % slice_path)
        records = list(read_jsonl(slice_path))

    if args.limit:
        records = records[: args.limit]

    system, user_tpl = load_template(args.track)
    extra = {}
    if args.track == "translate":
        extra = {"TARGET_LANG": LANG_NAME.get(args.lang, args.lang), "LANG_CODE": args.lang}

    # output path
    if args.track == "translate":
        out_path = os.path.join(HERE, "out", "translate", "%s.%s.jsonl" % (args.letter, args.lang))
    else:
        out_path = os.path.join(HERE, "out", args.track, "%s.jsonl" % args.letter)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    if args.dry_run:
        rec = records[0]
        print("=== SYSTEM ===\n%s\n" % fill(system, rec, extra))
        print("=== USER ===\n%s" % fill(user_tpl, rec, extra))
        print("\n[dry-run] %d entries would be processed -> %s" % (len(records), out_path))
        return

    env = load_env(args.env)
    if args.model:
        env["OPENMODEL_MODEL"] = args.model
    if not env.get("OPENMODEL_API_KEY"):
        sys.exit("no OPENMODEL_API_KEY in %s (see .env.example)" % args.env)

    already = done_ids(out_path)
    todo = [r for r in records if r.get("L") not in already]
    print("track=%s letter=%s: %d total, %d already done, %d to do, model=%s"
          % (args.track, args.letter, len(records), len(already), len(todo),
             env.get("OPENMODEL_MODEL", "deepseek-chat")))

    n_ok = n_err = 0
    with open(out_path, "a", encoding="utf-8") as w:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = {}
            for rec in todo:
                u = fill(user_tpl, rec, extra)
                s = fill(system, rec, extra)
                futs[ex.submit(call_deepseek, env, s, u)] = rec
            for fut in as_completed(futs):
                rec = futs[fut]
                res = fut.result()
                # always trust the input id; the model occasionally echoes a wrong L
                if isinstance(res, dict):
                    res["L"] = rec.get("L")
                w.write(json.dumps(res, ensure_ascii=False) + "\n")
                w.flush()
                if res.get("_error"):
                    n_err += 1
                else:
                    n_ok += 1
                if (n_ok + n_err) % 25 == 0:
                    print("  ...%d ok, %d err" % (n_ok, n_err))

    print("done: %d ok, %d err -> %s" % (n_ok, n_err, out_path))


if __name__ == "__main__":
    main()
