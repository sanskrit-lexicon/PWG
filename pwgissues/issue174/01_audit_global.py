"""
Phase A: Frequency + context audit of global PWG abbreviations.

Strategy: avoid regex over the full 51MB file 787 times.  Use Python's
built-in str.count() and str.find() — both are fast C-level scans.

For each abbreviation X:
- marked    = text.count("<ab>X</ab>")
- total     = text.count(X)
- unmarked  = total - marked   (occurrences of the bare string not inside <ab>)

Note: 'unmarked' may overcount when X is a substring of another abbreviation
(e.g. 'a.' inside 'a. a. O.'), or of an unrelated word.  We treat the number
as an upper bound and flag ambiguous (short) ones for human review.

Inputs:
  PWG_abbr_global.txt
  ../../../csl-orig/v02/pwg/pwg.txt

Outputs:
  audit_global.tsv
  audit_global_summary.txt
"""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).resolve().parent
PWG_TXT = HERE.parent.parent.parent / "csl-orig" / "v02" / "pwg" / "pwg.txt"
ABBR_FILE = HERE / "PWG_abbr_global.txt"

OUT_TSV = HERE / "audit_global.tsv"
OUT_SUM = HERE / "audit_global_summary.txt"

print(f"Reading abbreviations from: {ABBR_FILE}", flush=True)
abbrs = []
ab_re = re.compile(r"<ab>(.*?)</ab>")
with ABBR_FILE.open(encoding="utf-8") as f:
    for line in f:
        m = ab_re.search(line)
        if m:
            abbrs.append(m.group(1))
print(f"  loaded {len(abbrs)} abbreviations", flush=True)

print(f"Reading PWG text from: {PWG_TXT}", flush=True)
text = PWG_TXT.read_text(encoding="utf-8")
print(f"  loaded {len(text):,} chars", flush=True)


def sample_unmarked_contexts(needle, hay, n=3, span=50):
    """Return up to n contexts where needle appears OUTSIDE an <ab>...</ab> wrap."""
    out = []
    start = 0
    while len(out) < n:
        idx = hay.find(needle, start)
        if idx == -1:
            break
        prefix_check = hay[max(0, idx-4):idx]
        suffix_check = hay[idx+len(needle):idx+len(needle)+5]
        if prefix_check.endswith("<ab>") and suffix_check.startswith("</ab>"):
            start = idx + len(needle)
            continue
        a = max(0, idx - span)
        b = min(len(hay), idx + len(needle) + span)
        snippet = hay[a:b].replace("\n", " ").replace("\t", " ")
        out.append(snippet)
        start = idx + len(needle)
    while len(out) < n:
        out.append("")
    return out


print("Auditing...", flush=True)
rows = []
for i, abbr in enumerate(abbrs, 1):
    marked = text.count(f"<ab>{abbr}</ab>")
    total = text.count(abbr)
    unmarked = max(0, total - marked)
    ambiguous = "Y" if len(abbr) <= 3 else ""
    ctxs = sample_unmarked_contexts(abbr, text, n=3, span=50) if unmarked > 0 else ["", "", ""]
    rows.append((abbr, len(abbr), ambiguous, total, marked, unmarked, *ctxs))
    if i % 100 == 0:
        print(f"  {i}/{len(abbrs)}", flush=True)

rows.sort(key=lambda r: (-r[3], r[0]))

with OUT_TSV.open("w", encoding="utf-8") as f:
    f.write("abbr\tlen\tambiguous\traw\tmarked\tunmarked\tctx1\tctx2\tctx3\n")
    for row in rows:
        f.write("\t".join(str(x) for x in row) + "\n")
print(f"Wrote {OUT_TSV}", flush=True)

total_raw = sum(r[3] for r in rows)
total_marked = sum(r[4] for r in rows)
total_unmarked = sum(r[5] for r in rows)
zero_occur = sum(1 for r in rows if r[3] == 0)
ambig_count = sum(1 for r in rows if r[2] == "Y")
already_fully = sum(1 for r in rows if r[5] == 0 and r[3] > 0)
never_marked = sum(1 for r in rows if r[4] == 0 and r[3] > 0)

with OUT_SUM.open("w", encoding="utf-8") as f:
    f.write("PWG global-abbreviation audit\n")
    f.write("=" * 50 + "\n")
    f.write(f"abbreviations in list:        {len(rows)}\n")
    f.write(f"  ambiguous (<=3 chars):      {ambig_count}\n")
    f.write(f"  with zero occurrences:      {zero_occur}\n")
    f.write(f"  already fully marked:       {already_fully}\n")
    f.write(f"  never marked anywhere:      {never_marked}\n")
    f.write("\n")
    f.write(f"total occurrences:            {total_raw:,}\n")
    f.write(f"  already inside <ab></ab>:   {total_marked:,}\n")
    f.write(f"  bare text (need wrapping):  {total_unmarked:,}\n")
    f.write("\n")
    f.write("Top 20 by raw frequency:\n")
    for r in rows[:20]:
        f.write(f"  {r[0]:25s} raw={r[3]:>6}  marked={r[4]:>6}  unmarked={r[5]:>6}\n")
    f.write("\n")
    f.write("Top 20 unmarked (need wrapping most):\n")
    for r in sorted(rows, key=lambda x: -x[5])[:20]:
        f.write(f"  {r[0]:25s} unmarked={r[5]:>6}  marked={r[4]:>6}\n")

print(f"Wrote {OUT_SUM}", flush=True)
print("DONE", flush=True)
