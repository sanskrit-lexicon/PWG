"""
Phase G: Markup fixer + audit for pwg.txt.

Two jobs:

  1. FIX problems that have a single safe automatic resolution.
     Currently:
       (a) nested <ab><ab>X</ab> Y</ab>  →  <ab>X Y</ab>           (rare-but-possible)
       (b) nested <ab><ab>X</ab></ab>    →  <ab>X</ab>             (degenerate dup)
       (c) whitespace inside tag pairs:
            <ls>  …  </ls>   →   trim leading/trailing spaces
            <ab>  …  </ab>
            <lex> …  </lex>
            <is>  …  </is>
            <lang …> … </lang>

  2. AUDIT issues that need a human decision. These are reported but
     NOT auto-modified. Each finding lands in markup_audit.txt with
     enough surrounding context to act.

Why the nesting fixer exists even though pwg.txt is currently clean:
this script is meant to run AFTER Phase B's changes_safe.txt is applied
AND AB's local-abbreviation pass overlays its own `<ab n="…">` wraps.
Without coordination the two passes can produce `<ab><ab>…</ab>…</ab>`.
This script is the cleanup tool for that contingency.

Inputs:
  ../../../csl-orig/v02/pwg/pwg.txt

Outputs:
  pwg_fixed.txt           -- repaired copy
  markup_fix_changes.txt  -- updateByLine-style log of every auto-fix
  markup_audit.txt        -- everything that needs a human eye, with line ref

Usage:
  python 08_markup_fix.py            # uses default in/out paths
  python 08_markup_fix.py IN OUT     # custom paths
"""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).resolve().parent

if len(sys.argv) >= 3:
    PWG_TXT = Path(sys.argv[1])
    OUT_FIX = Path(sys.argv[2])
else:
    PWG_TXT = HERE.parent.parent.parent / "csl-orig" / "v02" / "pwg" / "pwg.txt"
    OUT_FIX = HERE / "pwg_fixed.txt"

OUT_LOG = HERE / "markup_fix_changes.txt"
OUT_AUDIT = HERE / "markup_audit.txt"


# ---------------------------------------------------------------------------
# Pattern 1: nested <ab> wrappings
# ---------------------------------------------------------------------------
#
# After Phase B + AB's local overlay we may see e.g.:
#   <ab><ab>vor.</ab> W.</ab>             (case a)
#   <ab n="?"><ab>St.</ab></ab>           (case b — exact-duplicate)
#
# Rule of repair:
#  * If the inner wrap covers a strict prefix or suffix of the outer wrap,
#    drop the inner — the outer is canonical.
#  * If the inner wrap exactly matches the outer wrap's content, drop the
#    inner (degenerate duplicate).
#  * If the inner wrap covers something in the middle, leave it — that is
#    too ambiguous to resolve without semantic context.

NEST_RX = re.compile(
    r"<ab(?P<oa>\b[^>]*)>(?P<pre>[^<]*)<ab(?P<ia>\b[^>]*)>(?P<inner>[^<]*)</ab>(?P<post>[^<]*)</ab>"
)


def fix_nested_ab(line):
    n_fixed = 0
    while True:
        m = NEST_RX.search(line)
        if not m:
            return line, n_fixed
        oa = m.group("oa")
        pre = m.group("pre")
        inner = m.group("inner")
        post = m.group("post")
        repl = f"<ab{oa}>{pre}{inner}{post}</ab>"
        line = line[:m.start()] + repl + line[m.end():]
        n_fixed += 1


# ---------------------------------------------------------------------------
# Pattern 2: whitespace inside common tag pairs
# ---------------------------------------------------------------------------
TRIM_TAGS = ["ls", "ab", "lex", "is", "lang"]


def fix_trim_whitespace(line):
    n = 0
    for tag in TRIM_TAGS:
        pat = re.compile(rf"(<{tag}\b[^>]*>)(\s+)([^<]*?)(\s*)(</{tag}>)")
        def _repl(m):
            nonlocal n
            inside = m.group(3).rstrip()
            if inside != m.group(2) + m.group(3) + m.group(4):
                n += 1
            return f"{m.group(1)}{inside}{m.group(5)}"
        line = pat.sub(_repl, line)
        pat2 = re.compile(rf"(<{tag}\b[^>]*>)([^<]*?)(\s+)(</{tag}>)")
        def _repl2(m):
            nonlocal n
            inside = m.group(2).rstrip()
            n += 1
            return f"{m.group(1)}{inside}{m.group(4)}"
        line = pat2.sub(_repl2, line)
    return line, n


# ---------------------------------------------------------------------------
# Audit (no auto-modification)
# ---------------------------------------------------------------------------

AUDIT_CHECKS = [
    ("Adjacent </ab> <ab> — possibly intentional but worth verifying",
     re.compile(r"</ab>\s*<ab")),
    ("<ab n=\"?\"> with literal '?' placeholder — needs an expansion",
     re.compile(r'<ab\s+n="\?">')),
    ("Empty content tag",
     re.compile(r"<(ls|ab|lex|is|lang)\b[^>]*></\1>")),
    ("<ls> ending in lone period before a quotation",
     re.compile(r"<ls>[^<]*\.</ls>\s*[‘’„“]")),
    ("Sanskrit token immediately followed by <ab> (no space)",
     re.compile(r"#\}<ab\b")),
    ("Malformed tag with unescaped < inside its own attribute value",
     re.compile(r'<[A-Za-z][A-Za-z0-9]*\s+[A-Za-z]+="[^"]*<[^"]*"\s*[^>]*>')),
    ("[PageN-NNNN] without preceding space",
     re.compile(r"[^\s\(\[]\[Page\d")),
    ("<ab> wrapping a token NOT in PWG_abbr_global.txt (run after wrapping)",
     None),
    ("<ab> directly after a German preposition followed by capital (vor . S.) — risk of mis-wrap",
     None),
]


def main():
    print(f"Reading {PWG_TXT} …", flush=True)
    lines = PWG_TXT.read_text(encoding="utf-8").splitlines()
    print(f"  {len(lines):,} lines", flush=True)

    out_lines = []
    fix_log = []
    tot_nested = 0
    tot_trim = 0

    audit_hits = {label: [] for label, _ in AUDIT_CHECKS}

    for lineno, line in enumerate(lines, 1):
        orig = line
        line, n1 = fix_nested_ab(line)
        line, n2 = fix_trim_whitespace(line)
        tot_nested += n1
        tot_trim += n2
        if line != orig:
            fix_log.append((lineno, orig, line))
        out_lines.append(line)
        for label, pat in AUDIT_CHECKS:
            if pat is None:
                continue
            for m in pat.finditer(orig):
                start = max(0, m.start() - 40)
                end = min(len(orig), m.end() + 40)
                snippet = orig[start:end].replace("\t", " ")
                audit_hits[label].append((lineno, snippet))
                if len(audit_hits[label]) >= 200:
                    break
        if lineno % 200000 == 0:
            print(f"  {lineno:,}/{len(lines):,}", flush=True)

    print(f"Total nested <ab> repairs:    {tot_nested}", flush=True)
    print(f"Total whitespace trims:       {tot_trim}", flush=True)
    print(f"Total changed lines:          {len(fix_log)}", flush=True)

    print(f"Writing {OUT_FIX} …", flush=True)
    with OUT_FIX.open("w", encoding="utf-8", newline="\n") as f:
        for line in out_lines:
            f.write(line + "\n")

    print(f"Writing {OUT_LOG} …", flush=True)
    with OUT_LOG.open("w", encoding="utf-8") as f:
        f.write("; markup_fix log\n")
        f.write(f"; nested <ab>:    {tot_nested}\n")
        f.write(f"; whitespace:     {tot_trim}\n")
        f.write(f"; changed lines:  {len(fix_log)}\n;\n")
        for lineno, old, new in fix_log:
            f.write(f"{lineno} old {old}\n")
            f.write(f"{lineno} new {new}\n")

    print(f"Writing {OUT_AUDIT} …", flush=True)
    with OUT_AUDIT.open("w", encoding="utf-8") as f:
        f.write("PWG markup audit — findings requiring a human decision\n")
        f.write("=" * 60 + "\n\n")
        f.write("Generated by 08_markup_fix.py against pwg.txt.\n")
        f.write("Items below were DETECTED but NOT modified by the fixer.\n")
        f.write("Each section explains the pattern and what to consider.\n\n")
        f.write("If a check has matches: 0, that pattern is currently absent\n")
        f.write("from pwg.txt — the check is kept so this script can be re-run\n")
        f.write("after Phase B + AB's local pass to catch problems they introduce.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nWHAT THIS FIXER AUTO-CORRECTS\n")
        f.write("------------------------------------------------------------\n")
        f.write("  - Nested <ab><ab>X</ab> Y</ab>          → <ab>X Y</ab>\n")
        f.write("  - Whitespace inside <ls>/<ab>/<lex>/<is>/<lang>\n")
        f.write("\nThe original file is left untouched; results go to\n")
        f.write("pwg_fixed.txt with the full change log in markup_fix_changes.txt.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nWHAT NEEDS HUMAN ATTENTION (broader list, beyond the\n")
        f.write("automated checks below)\n")
        f.write("------------------------------------------------------------\n")
        f.write("  1. <ab n=\"?\"> placeholders — 91 occurrences in pwg.txt where\n")
        f.write("     the local-abbreviation expansion was never filled in.\n")
        f.write("     AB's PWG_abbr_local.txt is the reference. Many of these\n")
        f.write("     can be resolved by looking up the abbreviation letter +\n")
        f.write("     surrounding noun in AB's local list.\n\n")
        f.write("  2. Adjacent </ab> <ab> — 9 occurrences. Inspect to confirm\n")
        f.write("     they are intentional separate abbreviations (e.g.\n")
        f.write("     'N. pr. u. s. w.') rather than artifacts of an earlier\n")
        f.write("     auto-wrap that should have been a single <ab> wrap.\n\n")
        f.write("  3. Phase B false positives — review changes_safe.txt for\n")
        f.write("     wraps at end-of-line that may be sentence-final words\n")
        f.write("     that happened to end in a period (e.g. the 'vor.' case).\n")
        f.write("     The DENYLIST in 03_safewrap.py is the place to add them.\n\n")
        f.write("  4. Local-abbreviation overlay collision — after Phase B,\n")
        f.write("     short abbreviations inside compound contexts may be\n")
        f.write("     wrapped (e.g. <ab>u. d.</ab> O. instead of\n")
        f.write("     <ab n=\"dem und dem Ort\">u. d. O.</ab>). AB's local pass\n")
        f.write("     resolves these; re-run this fixer afterward to catch any\n")
        f.write("     <ab><ab>…</ab>…</ab> nesting created in the process.\n\n")
        f.write("  5. Trim residual hyphenation errors — AB's ApteES thread\n")
        f.write("     mentions hyphenation carry-overs from earlier digitisation\n")
        f.write("     work. These are not addressed here; a dedicated pass over\n")
        f.write("     line-break hyphens (especially in {#…#} blocks) is needed.\n\n")
        f.write("  6. pwgab_input_draft.txt <INFER/> tags — 58 abbreviations\n")
        f.write("     have inferred/uncertain expansions flagged for review.\n")
        f.write("     `grep '<INFER/>' pwgab_input_draft.txt` lists them.\n\n")
        f.write("  7. AB_tags_PWG.txt tags with zero usage — <ns>, <iw>, <mng>,\n")
        f.write("     <ed>, <ms>, <pe>, <per> have no examples in pwg.txt and\n")
        f.write("     AB has not specified semantic intent. Skip until AB\n")
        f.write("     provides definitions.\n\n")
        f.write("------------------------------------------------------------\n")
        f.write("\nAUTOMATED CHECKS BELOW\n")
        f.write("------------------------------------------------------------\n\n")
        for label, hits in audit_hits.items():
            f.write(f"## {label}\n")
            f.write(f"   matches: {len(hits)} (showing up to 200)\n")
            for ln, snippet in hits[:200]:
                f.write(f"   L{ln}: {snippet}\n")
            f.write("\n")

    print("DONE", flush=True)


if __name__ == "__main__":
    main()
