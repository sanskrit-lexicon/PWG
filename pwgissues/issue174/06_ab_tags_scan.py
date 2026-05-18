"""
Phase E: Scanner for the additional AB-tags proposed in AB_tags_PWG.txt.

For each proposed tag, do two things:
  1. Check whether the tag already exists in pwg.txt and count instances.
  2. Where it does NOT yet exist, propose heuristic candidates.

Heuristics per tag (best-effort — humans confirm):
  <div n="X">       — div tags are positional; just count current usage.
  <bot></bot>       — botanical names. Heuristic: scan for the abbreviation
                      <ab>bot.</ab> in newly-wrapped narrative (Phase B output).
                      Also report passages where 'bot.' is currently bare.
  <zoo></zoo>       — same approach for 'zool.'/'Zool.'.
  <arab>            — Arabic-script Unicode block (U+0600..U+06FF).
  <gk>              — Greek-script Unicode block (U+0370..U+03FF, U+1F00..U+1FFF).
  <heb>             — Hebrew block (U+0590..U+05FF).
  <rus>             — Cyrillic block (U+0400..U+04FF).
  <mong>            — Mongolian / Phags-pa: rare. Look for cyrillic + 'mong'.
  <ocs>             — Old Church Slavonic. Marked by 'ocs' near foreign script.
  <zen>             — Avestan / Zend (no Unicode block — typically Latin
                      transliteration with breve diacritics or sharp s).
                      Scan for the abbreviation 'Zend' or 'zend.' nearby.
  <fr>              — French quotations. Scan for {%…%} blocks containing
                      common French function words preceded by 'franz.'/'fr.'
  <is></is>         — italic Sanskrit. Already exists; count.
  <ns>              — needs definition from AB. Report count if any.
  <iw>              — needs definition from AB.
  <mng></mng>       — meaning markup. Likely manual.
  <ed></ed>         — editor markup. Manual.
  <ms></ms>         — manuscript markup. Manual.
  <num></num>       — numeric markup. Heuristic: bare digit-only tokens in
                      otherwise narrative lines.
  <pe></pe>         — page-end? (positional)
  <per></per>       — period marker. Manual.

Output:
  ab_tags_scan.txt   -- one section per tag with counts and sample lines
"""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).resolve().parent
PWG_TXT = HERE.parent.parent.parent / "csl-orig" / "v02" / "pwg" / "pwg.txt"
TAGS_FILE = HERE / "AB_tags_PWG.txt"
OUT = HERE / "ab_tags_scan.txt"

print("Reading AB-tag list...", flush=True)
proposed = []
with TAGS_FILE.open(encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        proposed.append(line)
print(f"  {len(proposed)} proposed tag forms", flush=True)

print("Reading pwg.txt...", flush=True)
text = PWG_TXT.read_text(encoding="utf-8")
lines = text.splitlines()
print(f"  {len(lines):,} lines", flush=True)

UNICODE_BLOCKS = {
    "Arabic":   ((0x0600, 0x06FF),),
    "Greek":    ((0x0370, 0x03FF), (0x1F00, 0x1FFF)),
    "Hebrew":   ((0x0590, 0x05FF),),
    "Cyrillic": ((0x0400, 0x04FF),),
    "Mongolian":((0x1800, 0x18AF),),
    "Devanagari":((0x0900, 0x097F),),
}

def block_count(name):
    ranges = UNICODE_BLOCKS[name]
    n = 0
    for c in text:
        cp = ord(c)
        for a, b in ranges:
            if a <= cp <= b:
                n += 1
                break
    return n


def sample_lines_with(needle, max_n=5):
    out = []
    for lineno, line in enumerate(lines, 1):
        if needle in line:
            out.append((lineno, line[:140]))
            if len(out) >= max_n:
                break
    return out


def sample_lines_with_block(name, max_n=5):
    ranges = UNICODE_BLOCKS[name]
    def has_block(s):
        for c in s:
            cp = ord(c)
            for a, b in ranges:
                if a <= cp <= b:
                    return True
        return False
    out = []
    for lineno, line in enumerate(lines, 1):
        if has_block(line):
            out.append((lineno, line[:140]))
            if len(out) >= max_n:
                break
    return out


sections = []

def section(title, body):
    sections.append((title, body))


for tag in proposed:
    m = re.match(r'<div n="([^"]+)">', tag)
    if m:
        n = m.group(1)
        existing = text.count(f'<div n="{n}">')
        body = f"  current occurrences in pwg.txt: {existing:,}\n"
        if existing > 0:
            body += "  samples:\n"
            for ln, t in sample_lines_with(f'<div n="{n}">', max_n=3):
                body += f"    L{ln}: {t}\n"
        section(tag, body)
        continue

    m = re.match(r'<(/?\w+)>', tag)
    pair = re.match(r'<(\w+)></\w+>', tag)
    if pair:
        name = pair.group(1)
        open_t = f"<{name}"
        close_t = f"</{name}>"
        opens = len(re.findall(rf"<{name}\b[^>]*>", text))
        closes = text.count(close_t)
        body = f"  current open tags <{name}…>: {opens:,}\n"
        body += f"  current close tags {close_t}: {closes:,}\n"
        if opens > 0:
            body += "  samples:\n"
            rx = re.compile(rf"<{name}\b[^>]*>.*?</{name}>")
            for i, mm in enumerate(rx.finditer(text)):
                if i >= 3:
                    break
                snippet = mm.group(0)[:140]
                body += f"    {snippet}\n"
        elif name in ("bot", "zoo"):
            ab_form = "bot." if name == "bot" else ("zool.", "Zool.")
            forms = [ab_form] if isinstance(ab_form, str) else ab_form
            for form in forms:
                ct = text.count(form)
                body += f"  candidate via abbreviation '{form}': {ct:,} occurrences in text\n"
                for ln, t in sample_lines_with(form, max_n=2):
                    body += f"    L{ln}: {t}\n"
        elif name in ("arab", "gk", "heb", "rus", "mong"):
            block_name = {"arab": "Arabic", "gk": "Greek", "heb": "Hebrew",
                          "rus": "Cyrillic", "mong": "Mongolian"}[name]
            try:
                bc = block_count(block_name)
            except Exception:
                bc = -1
            body += f"  candidate via Unicode block ({block_name}): {bc:,} chars\n"
            for ln, t in sample_lines_with_block(block_name, max_n=3):
                body += f"    L{ln}: {t}\n"
        elif name == "zen":
            body += "  no dedicated block; look for the literal abbreviation 'Zend'/'Av.'\n"
            for ln, t in sample_lines_with("Zend", max_n=3):
                body += f"    L{ln}: {t}\n"
        elif name == "fr":
            body += "  no dedicated block; candidates near abbreviation 'franz.'/'fr.':\n"
            for ln, t in sample_lines_with("franz.", max_n=3):
                body += f"    L{ln}: {t}\n"
        elif name == "ocs":
            body += "  no dedicated marker; look for 'ksl.'/'altslav.'\n"
            for ln, t in sample_lines_with("altslav", max_n=3):
                body += f"    L{ln}: {t}\n"
        elif name == "num":
            body += "  heuristic — bare 'n.' followed by digits, or {#…#} containing only digits.\n"
        elif name in ("is", "ns", "iw", "mng", "ed", "ms", "pe", "per"):
            body += f"  no existing occurrences; semantic intent from AB needed before scanning.\n"
        section(tag, body)
        continue

    section(tag, "  unrecognised proposed tag form; no scan attempted.\n")


print(f"Writing {OUT}...", flush=True)
with OUT.open("w", encoding="utf-8") as f:
    f.write("AB-tags scan (issue #174, AB_tags_PWG.txt)\n")
    f.write("=" * 50 + "\n")
    f.write(f"Source: {PWG_TXT}\n\n")
    for title, body in sections:
        f.write(f"## {title}\n")
        f.write(body)
        f.write("\n")
print("DONE", flush=True)
