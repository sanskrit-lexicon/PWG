"""
Phase F: Cross-check PWG abbreviations against MW's authoritative list.

Many abbreviations are shared between MW (English-medium dictionary) and
PWG (German-medium dictionary).  Where the abbreviation strings match
literally, MW's <disp> is a good candidate to copy into PWG with light
adaptation.  Where they overlap conceptually but the abbreviation differs
(e.g. PWG 'Causativ' vs MW 'caus.'), we surface that for human review.

Inputs:
  PWG_abbr_global.txt                                  (787)
  ../../../csl-pywork/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt
  ../../../csl-pywork/v02/distinctfiles/pwg/pywork/pwgab/pwgab_input.txt
                                                       (existing 54)

Output:
  mw_overlap.txt        -- abbreviations identical between MW and PWG
                           with MW's <disp>
  mw_diff_case.txt      -- abbreviations that match under case-insensitive
                           comparison (different capitalization)
  mw_pwg_existing.txt   -- what existing pwgab_input.txt already covers
  pwgab_with_mw_hints.txt -- draft pwgab_input.txt enriched with MW hints
"""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).resolve().parent
PWG_LIST = HERE / "PWG_abbr_global.txt"
MW_INPUT = HERE.parent.parent.parent / "csl-pywork" / "v02" / "distinctfiles" / "mw" / "pywork" / "mwab" / "mwab_input.txt"
PWG_EXISTING = HERE.parent.parent.parent / "csl-pywork" / "v02" / "distinctfiles" / "pwg" / "pywork" / "pwgab" / "pwgab_input.txt"
DRAFT = HERE / "pwgab_input_draft.txt"

OUT_OVERLAP = HERE / "mw_overlap.txt"
OUT_DIFF = HERE / "mw_diff_case.txt"
OUT_EXISTING = HERE / "mw_pwg_existing.txt"
OUT_ENRICHED = HERE / "pwgab_with_mw_hints.txt"

print("Loading PWG global list...", flush=True)
pwg = []
with PWG_LIST.open(encoding="utf-8") as f:
    for line in f:
        m = re.search(r"<ab>(.*?)</ab>", line)
        if m:
            pwg.append(m.group(1))
print(f"  {len(pwg)} PWG abbreviations", flush=True)

print("Loading MW abbreviation file...", flush=True)
mw = {}
mw_disp = {}
with MW_INPUT.open(encoding="utf-8") as f:
    for line in f:
        if not line.strip() or line.startswith(";"):
            continue
        parts = line.rstrip("\n").split("\t", 1)
        if len(parts) != 2:
            continue
        abbr, rest = parts
        mw[abbr] = rest
        dm = re.search(r"<disp>(.*?)</disp>", rest)
        if dm:
            mw_disp[abbr] = dm.group(1)
print(f"  {len(mw)} MW abbreviations", flush=True)

print("Loading existing PWG abbreviation file (csl-pywork)...", flush=True)
pwg_existing = {}
with PWG_EXISTING.open(encoding="utf-8") as f:
    for line in f:
        if not line.strip() or line.startswith(";"):
            continue
        parts = line.rstrip("\n").split("\t", 1)
        if len(parts) != 2:
            continue
        pwg_existing[parts[0]] = parts[1]
print(f"  {len(pwg_existing)} existing PWG abbreviations", flush=True)

pwg_set = set(pwg)
mw_set = set(mw.keys())

exact_overlap = sorted(pwg_set & mw_set)
case_only = []
mw_lower_map = {a.lower(): a for a in mw_set}
for p in pwg_set - mw_set:
    pl = p.lower()
    if pl in mw_lower_map and mw_lower_map[pl] != p:
        case_only.append((p, mw_lower_map[pl]))
case_only.sort()

print(f"  exact overlap PWG ∩ MW: {len(exact_overlap)}", flush=True)
print(f"  case-only matches:      {len(case_only)}", flush=True)

with OUT_OVERLAP.open("w", encoding="utf-8") as f:
    f.write(f"PWG abbreviations also present in MW (exact match): {len(exact_overlap)}\n")
    f.write("=" * 50 + "\n")
    f.write("Format: <abbr>\\t<MW disp>\n\n")
    for a in exact_overlap:
        d = mw_disp.get(a, "?")
        f.write(f"{a}\t{d}\n")
print(f"Wrote {OUT_OVERLAP}", flush=True)

with OUT_DIFF.open("w", encoding="utf-8") as f:
    f.write(f"PWG vs MW differ only by capitalization: {len(case_only)}\n")
    f.write("=" * 50 + "\n")
    f.write("Format: <PWG form>\\t<MW form>\\t<MW disp>\n\n")
    for p, m in case_only:
        d = mw_disp.get(m, "?")
        f.write(f"{p}\t{m}\t{d}\n")
print(f"Wrote {OUT_DIFF}", flush=True)

with OUT_EXISTING.open("w", encoding="utf-8") as f:
    f.write(f"PWG abbreviations already in csl-pywork pwgab_input.txt: {len(pwg_existing)}\n")
    f.write("=" * 50 + "\n")
    f.write("Of these, also in our global list:\n")
    for a in sorted(pwg_existing):
        in_list = "Y" if a in pwg_set else "N"
        f.write(f"  {in_list}  {a}\n")
print(f"Wrote {OUT_EXISTING}", flush=True)

print("Building enriched draft (pwgab + MW hints)...", flush=True)
draft_lines = []
with DRAFT.open(encoding="utf-8") as f:
    for line in f:
        if line.startswith(";") or not line.strip():
            draft_lines.append(line.rstrip("\n"))
            continue
        parts = line.rstrip("\n").split("\t", 1)
        if len(parts) != 2:
            draft_lines.append(line.rstrip("\n"))
            continue
        abbr, rest = parts
        extra = []
        if abbr in mw_disp:
            extra.append(f"MW-disp={mw_disp[abbr]!r}")
        if abbr in pwg_existing:
            existing = pwg_existing[abbr]
            em = re.search(r"<disp>(.*?)</disp>", existing)
            if em:
                extra.append(f"existing-csl-pywork-disp={em.group(1)!r}")
        if extra:
            draft_lines.append(f"{abbr}\t{rest}  ; {' | '.join(extra)}")
        else:
            draft_lines.append(f"{abbr}\t{rest}")
with OUT_ENRICHED.open("w", encoding="utf-8") as f:
    for line in draft_lines:
        f.write(line + "\n")
print(f"Wrote {OUT_ENRICHED}", flush=True)
print("DONE", flush=True)
