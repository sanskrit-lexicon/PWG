"""
Phase C: Disambiguation worklist for short / ambiguous abbreviations.

For each abbreviation deferred in Phase B (alpha < 3), find every bare-text
occurrence in pwg.txt (i.e., not inside <ls>, <lex>, <is>, <lang>, <ab>,
{#…#} or {%…%}), and write a per-abbreviation worklist sorted by the
following word.  Clustering by next-word makes it easy for a human to
decide once per cluster instead of once per occurrence.

Outputs:
  disambig/<safe-name>.txt   -- one file per ambiguous abbreviation
  disambig_index.txt         -- summary count per abbreviation
"""

import sys
import re
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).resolve().parent
PWG_TXT = HERE.parent.parent.parent / "csl-orig" / "v02" / "pwg" / "pwg.txt"
ABBR_FILE = HERE / "PWG_abbr_global.txt"
LOCAL_FILE = HERE / "PWG_abbr_local.txt"
DISAMBIG_DIR = HERE / "disambig"
DISAMBIG_DIR.mkdir(exist_ok=True)
INDEX_FILE = HERE / "disambig_index.txt"

print("Loading abbreviations...", flush=True)
abbrs = []
with ABBR_FILE.open(encoding="utf-8") as f:
    for line in f:
        m = re.search(r"<ab>(.*?)</ab>", line)
        if m:
            abbrs.append(m.group(1))

review = [a for a in abbrs if sum(1 for c in a if c.isalpha()) < 3]
print(f"  reviewing {len(review)} ambiguous abbreviations", flush=True)

print("Loading local-abbreviation context hints from AB's list...", flush=True)
local_hints = defaultdict(list)
local_rx = re.compile(r'<ab n="([^"]*)">(.*?)</ab>')
with LOCAL_FILE.open(encoding="utf-8") as f:
    for line in f:
        m = local_rx.search(line)
        if m:
            expansion, abbr = m.group(1), m.group(2)
            local_hints[abbr].append(expansion)


def safe_filename(abbr):
    s = abbr.replace(".", "_dot").replace(" ", "_sp")
    s = "".join(c if c.isalnum() or c == "_" else "x" for c in s)
    case_tag = "U" if any(c.isupper() for c in abbr) else "L"
    return f"{case_tag}_{s}.txt"


TAG_PATTERNS = [
    re.compile(r"<ls\b[^>]*>.*?</ls>"),
    re.compile(r"<lex\b[^>]*>.*?</lex>"),
    re.compile(r"<is\b[^>]*>.*?</is>"),
    re.compile(r"<lang\b[^>]*>.*?</lang>"),
    re.compile(r"<ab\b[^>]*>.*?</ab>"),
    re.compile(r"\{#.*?#\}"),
    re.compile(r"\{%.*?%\}"),
]

print("Reading pwg.txt...", flush=True)
lines = PWG_TXT.read_text(encoding="utf-8").splitlines()
print(f"  {len(lines):,} lines", flush=True)


def mask(line):
    spans = []
    for pat in TAG_PATTERNS:
        for m in pat.finditer(line):
            spans.append((m.start(), m.end()))
    if not spans:
        return line
    spans.sort()
    chars = list(line)
    merged_end = -1
    for s, e in spans:
        if s < merged_end:
            for i in range(merged_end, e):
                if 0 <= i < len(chars):
                    chars[i] = "\x00"
            merged_end = max(merged_end, e)
        else:
            for i in range(s, e):
                chars[i] = "\x00"
            merged_end = e
    return "".join(chars)


print("Per-abbreviation scan (this is one mask pass per line; cheap)...", flush=True)
masked_lines = [mask(L) if not L.startswith("<L>") else "" for L in lines]


def find_with_boundary(needle, hay, exclude_overlap_set):
    out = []
    idx = hay.find(needle)
    while idx != -1:
        before_ok = idx == 0 or not hay[idx - 1].isalpha()
        ap = idx + len(needle)
        after_ok = ap >= len(hay) or not hay[ap].isalpha()
        if before_ok and after_ok:
            out.append(idx)
        idx = hay.find(needle, idx + 1)
    return out


next_word_rx = re.compile(r"[A-Za-zÄÖÜäöüß]+")
review_sorted = sorted(review, key=lambda a: (-len(a), a))

stats = {}
for abbr in review_sorted:
    print(f"  {abbr} ...", flush=True)
    rows = []
    for lineno, line in enumerate(lines, 1):
        masked = masked_lines[lineno - 1]
        if not masked or abbr not in masked:
            continue
        for idx in find_with_boundary(abbr, masked, None):
            a = max(0, idx - 60)
            b = min(len(line), idx + len(abbr) + 60)
            ctx = line[a:b].replace("\t", " ")
            nw_m = next_word_rx.search(line[idx + len(abbr):idx + len(abbr) + 30])
            nw = nw_m.group(0) if nw_m else ""
            rows.append((nw.lower(), lineno, ctx))
    rows.sort()
    stats[abbr] = len(rows)
    out_path = DISAMBIG_DIR / safe_filename(abbr)
    with out_path.open("w", encoding="utf-8") as f:
        f.write(f"# Ambiguous abbreviation: {abbr}\n")
        f.write(f"# Occurrences in bare narrative: {len(rows)}\n")
        if abbr in local_hints:
            f.write(f"# Known LOCAL expansions for this abbreviation (from AB's local list):\n")
            for h in local_hints[abbr]:
                f.write(f"#   - {h}\n")
        f.write("# Format: <next-word>\\t<line>\\t<context>\n")
        f.write("# Rows are sorted by next-word so similar contexts cluster.\n\n")
        for nw, ln, ctx in rows:
            f.write(f"{nw}\t{ln}\t{ctx}\n")

print(f"Writing {INDEX_FILE}", flush=True)
with INDEX_FILE.open("w", encoding="utf-8") as f:
    f.write("Disambiguation worklists\n")
    f.write("=" * 50 + "\n")
    f.write(f"{len(stats)} ambiguous abbreviations from global list.\n")
    f.write("Files in disambig/  (sorted by occurrence count, desc):\n\n")
    for abbr, n in sorted(stats.items(), key=lambda x: -x[1]):
        fname = safe_filename(abbr)
        hint = ""
        if abbr in local_hints:
            hint = f"   [{len(local_hints[abbr])} local expansions in AB's list]"
        f.write(f"  {abbr:10s}  {n:>6}  disambig/{fname}{hint}\n")

print("DONE", flush=True)
