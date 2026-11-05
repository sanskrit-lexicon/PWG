# BUGHUNT-FINDINGS-PWG-05.11.2026

_Created: 05-11-2026 · Last updated: 05-11-2026_

Nightly one-repo bug hunt (MG ruling 26-09-2026: nightly, one repo, auto-fix HIGH), run 05-11-2026.
Executor: GLM 5.3 Flash (`opencode/z-ai/glm-5.3-flash`). Scope: repo CODE — maintained
surface (`pagecolumn/`, `prefaces/`, `scripts/`, `tests/`, CI wiring) plus the active correction
pipeline (`pwg_ls2/`) and the declared-legacy verb lanes (`verbs01/`, `verbs01a/`);
`pwgissues/` (per-issue archive, ~250k lines of one-off JS) treated as data-giant archive and skipped.

**Elapsed: ~22 min wall (hunt ~17 min, landing ~5 min).**

## Verdict

**No HIGH findings.** 3 MEDIUM, 1 LOW. No committed secrets, no money rows, no credential or
infra exposure — so per the auto-fix fence nothing qualified for in-run fixing (MEDIUM/LOW are
report-only), and no GTD credential row is owed. All four findings are error-path/edge-input
defects in legacy or one-shot lanes; the maintained critical path (parse → change-file → export)
is green end-to-end.

## Findings (ranked)

### F1 — MEDIUM · TypeError crash on the malformed-data logging path (3 copies)

- [pwg_ls2/mbh/make_change_ls.py line 251](https://github.com/sanskrit-lexicon/PWG/blob/3602cc8a0bd2763a54a493d209eb00117a105b36/pwg_ls2/mbh/make_change_ls.py#L251)
- [pwg_ls2/hariv/make_change_ls.py line 320](https://github.com/sanskrit-lexicon/PWG/blob/3602cc8a0bd2763a54a493d209eb00117a105b36/pwg_ls2/hariv/make_change_ls.py#L320)
- [pwg_ls2/hariv/make_change2_ls.py line 320](https://github.com/sanskrit-lexicon/PWG/blob/3602cc8a0bd2763a54a493d209eb00117a105b36/pwg_ls2/hariv/make_change2_ls.py#L320)

`fdbg.write('; _5 data error a',orig)` — `write()` takes exactly one argument, so when the
`_5` parser meets a verse-list whose first verse has no parvan (the `p == None` error path),
the script dies with `TypeError: write() takes exactly one argument (2 given)` instead of
logging the malformed input and falling through to `return orig`. Every sibling error branch
in the same functions writes ONE string (`'; _6 data error a'` prints are fine — `print` takes
multi-args); these three lines are the deviants. Effect if re-run: generation of the change
file aborts mid-run (truncated/missing `change_X` output) and the malformed-LS evidence the
debug file exists to capture is lost. AST scan across all non-archived `*.py` confirms these
are the only 3 two-arg `write()` calls in the repo. Ranked MEDIUM not HIGH: one-shot completed
workflows (outputs already committed), failure is loud (traceback), not silent corruption.

### F2 — MEDIUM · ZeroDivisionError crash on `--per 1` / `--per 0`

- [pagecolumn/pwg_page_verify.py line 78](https://github.com/sanskrit-lexicon/PWG/blob/3602cc8a0bd2763a54a493d209eb00117a105b36/pagecolumn/pwg_page_verify.py#L78)

`step = (len(pages) - 1) / (per - 1)` — with `--per 1` (a legitimate request: "one anchor per
volume") or `--per 0`, `per - 1` is 0 and the tool crashes. Lived evidence this run:

```
$ python3 pagecolumn/pwg_page_verify.py --per 1 --out /tmp/opencode/pwg_verify_per1.tsv
  File ".../pwg_page_verify.py", line 78, in anchor_pages
    step = (len(pages) - 1) / (per - 1)
ZeroDivisionError: division by zero
```

Tool crash on edge CLI input; default `--per 10` unaffected. Fix shape (when picked up):
guard `per < 2` → return `[pages[0]]` (or `[]`), or `max(per, 2)`.

### F3 — MEDIUM · dead source-path wiring in both verb-lane redo scripts

- [verbs01a/redo.sh line 5](https://github.com/sanskrit-lexicon/PWG/blob/3602cc8a0bd2763a54a493d209eb00117a105b36/verbs01a/redo.sh#L5) — `orig="../../../cologne/csl-orig/v02"` resolves to `~/Documents/cologne/csl-orig/v02`: **directory does not exist** on this machine (probed). The real source lives at `~/Documents/GitHub/csl-orig/v02/pwg/pwg.txt` (= `../../csl-orig` from the script dir).
- [verbs01/redo.sh line 6](https://github.com/sanskrit-lexicon/PWG/blob/3602cc8a0bd2763a54a493d209eb00117a105b36/verbs01/redo.sh#L6) — `../pwg.txt` (`PWG/pwg.txt`, probed missing) and line 1 `../../mw/mw.txt` (probed missing).

All three regeneration steps of the verb-filter lane (`pwg_verb_filter.py` →
`pwg_verb_filter_map.py` → `preverb1.py`) reference a nonexistent source, so the documented
"remake" lane is unwireable as committed. `../../MWS/mwverbs/mwverbs1.txt` (the one input that
does exist) confirms the layout drifted, not the whole lane. Dead wiring, not data loss —
both dirs are declared legacy by [ruff.toml](https://github.com/sanskrit-lexicon/PWG/blob/3602cc8a0bd2763a54a493d209eb00117a105b36/ruff.toml)
and CI convention.

### F4 — LOW · unbound `mwpreverb` (NameError) on the mismatch error path

- [verbs01a/preverb1.py lines 243–257](https://github.com/sanskrit-lexicon/PWG/blob/3602cc8a0bd2763a54a493d209eb00117a105b36/verbs01a/preverb1.py#L243)

The `try` at 243–246 reads `preverbs[iupa]`, `mwpreverbs[iupa]`, `mwpreverbs_found[iupa]`; the
handler at 247–251 resets `preverb = '?'` and `mwfound = False` but **not** `mwpreverb`, which
line 257 formats into the output row — so when the upasarga/mw-verb counts mismatch (the exact
situation the handler exists for), execution raises `NameError` instead of emitting the `?`
row. Same shape at [verbs01/preverb1.py line 292](https://github.com/sanskrit-lexicon/PWG/blob/3602cc8a0bd2763a54a493d209eb00117a105b36/verbs01/preverb1.py#L292).
Report-only diagnostic path in a legacy lane.

## What verified GREEN (evidence actually run)

- **Test suite:** `python3 -m pytest tests/ -q` → **30 passed** in 1.44s (H5799 smoke suite: parseheadline, updateByLine, diff-roundtrip, make_change3_ls entry parsing, pagecolumn views, prefaces combined export).
- **Lint:** `ruff check .` → **All checks passed** (repo config: E9/F63/F7, legacy dirs excluded by policy).
- **Page-index contract:** `pwg_page_index.py` re-parsed all **123,366** entries from live `csl-orig/v02/pwg/pwg.txt`; all 123,366 header lines match `HEADER_RE` (the feared silent-drop of `<e>`-tagged headers does not occur — zero unmatched); regenerated `pwg_columns.tsv`, `pwg_pages.tsv`, `pwg_entry_locations.tsv` are **byte-identical** to the committed copies (derive-don't-store holds).
- **parseheadline py2/3 shim:** `xrange = range` shim present in all 8 `pwg_ls2/*/parseheadline.py` copies; the copy-parity test (`tests/test_parseheadline.py`, 1 digest across 8 copies) passes.
- **Secrets sweep:** `(api_key|secret|password|token) = 'literal'` pattern across py/sh/yml/txt/md → **no hits**.
- **CI wiring:** all four workflows (`ci.yml`, `changelog-lint.yml`, `data-validate.yml`, `dependabot-auto-merge.yml`) read sane — changelog-lint correctly forces `fetch-depth: 0`, guard fail-open paths are loud and documented, no `pull_request_target`/script-injection shapes, `GITHUB_TOKEN` scope minimal.

## Disposition

Per fence (MG ruling 26-09-2026): MEDIUM/LOW findings are **report-only** — no code edits this
run. No HIGH code bug → no auto-fix attempt spent (0 of 3). No HIGH credential/infra finding →
no GTD row owed. All four findings are small, surgical fixes (guard clause, one-arg write,
path repoint, one assignment) suitable for a single cleanup PR if MG wants them.

_Dr. Mārcis Gasūns_
