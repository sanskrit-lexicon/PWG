"""
Phase B: Safe-wrap script.

For each abbreviation in the GLOBAL list that has >=3 alphabetic
characters and is not in the curated DENYLIST, wrap every bare-narrative
occurrence in pwg.txt with <ab>...</ab>.

Per-line algorithm:
  1. Skip metalines starting with <L>.
  2. Mask out protected regions (<ls>,<lex>,<is>,<lang>,<ab>,{#…#},{%…%}).
     Replace each with a placeholder of identical length but containing no
     abbreviation characters (just NUL bytes).
  3. Sort abbreviations by length, longest first (so e.g. "Adj. compp."
     matches before "compp.").
  4. For each, use re.sub with boundary check
     (?<![A-Za-zÄÖÜäöüß])  …  (?![A-Za-zÄÖÜäöüß])
     replacing with <ab>X</ab>.
  5. Unmask protected regions.
  6. If line changed, append paired entries to changes_safe.txt.

Outputs:
  changes_safe.txt              -- updateByLine.py format change file
  changes_safe_stats.txt        -- per-abbreviation wrap counts
  changes_safe_skipped.txt      -- abbreviations not wrapped (and why)
"""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).resolve().parent
PWG_TXT = HERE.parent.parent.parent / "csl-orig" / "v02" / "pwg" / "pwg.txt"
ABBR_FILE = HERE / "PWG_abbr_global.txt"

OUT_CHG = HERE / "changes_safe.txt"
OUT_STATS = HERE / "changes_safe_stats.txt"
OUT_SKIP = HERE / "changes_safe_skipped.txt"

DENYLIST = {
    "vor.",
}

print("Loading abbreviations...", flush=True)
abbrs = []
with ABBR_FILE.open(encoding="utf-8") as f:
    for line in f:
        m = re.search(r"<ab>(.*?)</ab>", line)
        if m:
            abbrs.append(m.group(1))

safe = [a for a in abbrs if sum(1 for c in a if c.isalpha()) >= 3
        and a not in DENYLIST]
review = [a for a in abbrs if a not in safe]

print(f"  total = {len(abbrs)}", flush=True)
print(f"  safe  = {len(safe)} (alpha>=3, not in denylist)", flush=True)
print(f"  review = {len(review)} (deferred)", flush=True)

safe.sort(key=lambda a: (-len(a), a))

TAG_PATTERNS = [
    re.compile(r"<ls\b[^>]*>.*?</ls>"),
    re.compile(r"<lex\b[^>]*>.*?</lex>"),
    re.compile(r"<is\b[^>]*>.*?</is>"),
    re.compile(r"<lang\b[^>]*>.*?</lang>"),
    re.compile(r"<ab\b[^>]*>.*?</ab>"),
    re.compile(r"\{#.*?#\}"),
    re.compile(r"\{%.*?%\}"),
]

PLACEHOLDER = "\x00"


def mask(line):
    """Replace each protected region with placeholder of equal length."""
    out = line
    spans = []
    for pat in TAG_PATTERNS:
        for m in pat.finditer(out):
            spans.append((m.start(), m.end()))
    if not spans:
        return out
    spans.sort()
    merged = []
    cs, ce = spans[0]
    for s, e in spans[1:]:
        if s <= ce:
            ce = max(ce, e)
        else:
            merged.append((cs, ce))
            cs, ce = s, e
    merged.append((cs, ce))
    chars = list(out)
    for s, e in merged:
        for i in range(s, e):
            chars[i] = PLACEHOLDER
    return "".join(chars)


def safe_wrap_line(line, _unused):
    """Mask protected regions, wrap each safe abbreviation, then return line.

    bare_part is kept length-aligned with line; after each wrap, the new
    <ab>…</ab> region is itself masked in bare_part so subsequent
    abbreviations cannot match inside it.
    """
    if line.startswith("<L>"):
        return line, 0
    bare_part = mask(line)
    total_wraps = 0
    for abbr in safe:
        idx_in_bare = bare_part.find(abbr)
        while idx_in_bare != -1:
            before_ok = idx_in_bare == 0 or not bare_part[idx_in_bare - 1].isalpha()
            after_pos = idx_in_bare + len(abbr)
            after_ok = after_pos >= len(bare_part) or not bare_part[after_pos].isalpha()
            if before_ok and after_ok:
                replacement = f"<ab>{abbr}</ab>"
                bp = list(bare_part)
                bp[idx_in_bare:idx_in_bare + len(abbr)] = [PLACEHOLDER] * len(replacement)
                bare_part = "".join(bp)
                ln = list(line)
                ln[idx_in_bare:idx_in_bare + len(abbr)] = list(replacement)
                line = "".join(ln)
                total_wraps += 1
                idx_in_bare = bare_part.find(abbr, idx_in_bare + len(replacement))
            else:
                idx_in_bare = bare_part.find(abbr, idx_in_bare + 1)
    return line, total_wraps


print(f"Reading PWG text from: {PWG_TXT}", flush=True)
lines = PWG_TXT.read_text(encoding="utf-8").splitlines()
print(f"  {len(lines):,} lines", flush=True)

print("Wrapping...", flush=True)
out_lines = []
changes = []
wraps_per_abbr = {}
total_changed_lines = 0
total_wraps = 0

for lineno, line in enumerate(lines, 1):
    new_line, n = safe_wrap_line(line, line)
    if new_line != line:
        changes.append((lineno, line, new_line))
        total_changed_lines += 1
        total_wraps += n
    out_lines.append(new_line)
    if lineno % 100000 == 0:
        print(f"  {lineno:,}/{len(lines):,}  changed lines: {total_changed_lines:,}", flush=True)

print(f"Total changed lines: {total_changed_lines:,}", flush=True)
print(f"Total wraps:         {total_wraps:,}", flush=True)

print(f"Writing {OUT_CHG} ...", flush=True)
with OUT_CHG.open("w", encoding="utf-8") as f:
    f.write("; PWG issue #174 — safe wrap of global abbreviations (alpha>=3)\n")
    f.write(f"; auto-generated by 03_safewrap.py\n")
    f.write(f"; {len(safe)} abbreviations applied, {total_wraps:,} wraps over {total_changed_lines:,} lines\n;\n")
    for lineno, old, new in changes:
        f.write(f"{lineno} old {old}\n")
        f.write(f"{lineno} new {new}\n")

print("Computing per-abbreviation counts...", flush=True)
joined_new = "\n".join(out_lines)
abbr_counts = {}
for abbr in safe:
    cnt = joined_new.count(f"<ab>{abbr}</ab>")
    abbr_counts[abbr] = cnt

with OUT_STATS.open("w", encoding="utf-8") as f:
    f.write(f"Safe-wrap statistics\n")
    f.write(f"====================\n")
    f.write(f"abbreviations applied:  {len(safe)}\n")
    f.write(f"changed lines:          {total_changed_lines:,}\n")
    f.write(f"total wraps:            {total_wraps:,}\n\n")
    f.write("Per-abbreviation wrap count (>0 only):\n")
    for abbr in sorted(safe, key=lambda a: -abbr_counts[a]):
        n = abbr_counts[abbr]
        if n > 0:
            f.write(f"  {abbr:30s} {n:>6}\n")
print(f"Wrote {OUT_STATS}", flush=True)

with OUT_SKIP.open("w", encoding="utf-8") as f:
    f.write("Abbreviations DEFERRED to Phase C (need disambiguation review)\n")
    f.write("=" * 60 + "\n")
    for abbr in review:
        f.write(f"{abbr}\n")
print(f"Wrote {OUT_SKIP}", flush=True)
print("DONE", flush=True)
