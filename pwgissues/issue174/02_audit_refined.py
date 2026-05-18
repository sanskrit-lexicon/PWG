"""
Phase A (refined): audit again, this time excluding occurrences that are
already inside existing tag-pairs.

We strip the following from a working copy of the text before counting:
- whole metalines  `<L>...$`         (headword section, no narrative)
- `<ls>...</ls>`                     (literary source — already tagged)
- `<lex>...</lex>`                   (lexical category)
- `<is>...</is>`                     (italic Sanskrit)
- `<lang ...>...</lang>`             (foreign-script quote)
- `<ab>...</ab>`                     (already an abbreviation)
- `{#...#}`                          (Sanskrit in AS coding)
- `{%...%}`                          (italic German)

After stripping, the remaining text is "narrative German prose" — the
context in which `<ab>` wrapping is wanted.  Counting the abbreviation
in that stripped text gives a true "candidate for wrapping" number.

Outputs:
  audit_refined.tsv
  audit_refined_summary.txt
"""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).resolve().parent
PWG_TXT = HERE.parent.parent.parent / "csl-orig" / "v02" / "pwg" / "pwg.txt"
ABBR_FILE = HERE / "PWG_abbr_global.txt"

OUT_TSV = HERE / "audit_refined.tsv"
OUT_SUM = HERE / "audit_refined_summary.txt"

print("Reading abbreviations...", flush=True)
abbrs = []
with ABBR_FILE.open(encoding="utf-8") as f:
    for line in f:
        m = re.search(r"<ab>(.*?)</ab>", line)
        if m:
            abbrs.append(m.group(1))
print(f"  loaded {len(abbrs)} abbreviations", flush=True)

print("Reading PWG text...", flush=True)
text = PWG_TXT.read_text(encoding="utf-8")
print(f"  loaded {len(text):,} chars", flush=True)

print("Counting marked-as-<ab> for each abbreviation...", flush=True)
marked_counts = {a: text.count(f"<ab>{a}</ab>") for a in abbrs}

print("Stripping already-tagged content to build narrative-only text...", flush=True)
stripped = text
stripped = re.sub(r"<L>[^\n]*", " ", stripped)
stripped = re.sub(r"<ls\b[^>]*>.*?</ls>", " ", stripped, flags=re.DOTALL)
stripped = re.sub(r"<lex\b[^>]*>.*?</lex>", " ", stripped, flags=re.DOTALL)
stripped = re.sub(r"<is\b[^>]*>.*?</is>", " ", stripped, flags=re.DOTALL)
stripped = re.sub(r"<lang\b[^>]*>.*?</lang>", " ", stripped, flags=re.DOTALL)
stripped = re.sub(r"<ab\b[^>]*>.*?</ab>", " ", stripped, flags=re.DOTALL)
stripped = re.sub(r"\{#.*?#\}", " ", stripped, flags=re.DOTALL)
stripped = re.sub(r"\{%.*?%\}", " ", stripped, flags=re.DOTALL)
print(f"  stripped length: {len(stripped):,} chars (was {len(text):,})", flush=True)


def sample_contexts(needle, hay, n=3, span=50):
    out, start = [], 0
    while len(out) < n:
        idx = hay.find(needle, start)
        if idx == -1:
            break
        a = max(0, idx - span)
        b = min(len(hay), idx + len(needle) + span)
        out.append(hay[a:b].replace("\n", " ").replace("\t", " "))
        start = idx + len(needle)
    while len(out) < n:
        out.append("")
    return out


print("Counting in stripped (narrative-only) text...", flush=True)
rows = []
for i, abbr in enumerate(abbrs, 1):
    raw = text.count(abbr)
    marked = marked_counts[abbr]
    bare = stripped.count(abbr)
    in_other_tags = max(0, raw - marked - bare)
    ambiguous = "Y" if len(abbr) <= 3 else ""
    ctxs = sample_contexts(abbr, stripped, n=3, span=50) if bare > 0 else ["", "", ""]
    rows.append((abbr, len(abbr), ambiguous, raw, marked, in_other_tags, bare, *ctxs))
    if i % 100 == 0:
        print(f"  {i}/{len(abbrs)}", flush=True)

rows.sort(key=lambda r: (-r[6], r[0]))

with OUT_TSV.open("w", encoding="utf-8") as f:
    f.write("abbr\tlen\tambiguous\traw\tmarked\tin_other_tags\tbare_narrative\tctx1\tctx2\tctx3\n")
    for row in rows:
        f.write("\t".join(str(x) for x in row) + "\n")
print(f"Wrote {OUT_TSV}", flush=True)

total_raw = sum(r[3] for r in rows)
total_marked = sum(r[4] for r in rows)
total_other = sum(r[5] for r in rows)
total_bare = sum(r[6] for r in rows)
zero_bare = sum(1 for r in rows if r[6] == 0)
ambig_count = sum(1 for r in rows if r[2] == "Y")

with OUT_SUM.open("w", encoding="utf-8") as f:
    f.write("PWG global-abbreviation audit (refined: tag-content stripped)\n")
    f.write("=" * 60 + "\n")
    f.write(f"abbreviations in list:               {len(rows)}\n")
    f.write(f"  ambiguous (<=3 chars):             {ambig_count}\n")
    f.write(f"  with zero bare-narrative occurr.:  {zero_bare}\n")
    f.write("\n")
    f.write(f"total raw occurrences in pwg.txt:    {total_raw:,}\n")
    f.write(f"  already in <ab></ab>:              {total_marked:,}\n")
    f.write(f"  in other tags (<ls>,<lex>,...):    {total_other:,}\n")
    f.write(f"  bare in narrative (wrap targets):  {total_bare:,}\n")
    f.write("\n")
    f.write("Top 30 by BARE NARRATIVE occurrence (the real wrap targets):\n")
    for r in rows[:30]:
        f.write(f"  {r[0]:25s} bare={r[6]:>6}  in_other_tags={r[5]:>6}  marked={r[4]:>6}\n")
    f.write("\n")
    f.write("Abbreviations in list with ZERO bare narrative occurrences\n")
    f.write("(safe to skip — either always tagged already, or list-only):\n")
    for r in rows:
        if r[6] == 0:
            f.write(f"  {r[0]}\n")

print(f"Wrote {OUT_SUM}", flush=True)
print("DONE", flush=True)
