# tests/ — PWG smoke suite (H5799)

_Run: `python3 -m pytest tests/ -v` (CI: `.github/workflows/ci.yml` →
**Smoke tests (parse + export critical path)** job). Scope: the active
pipeline only (`pwg_ls2/`, `pagecolumn/`, `prefaces/`) — legacy dirs
(`misc/`, `pwg_ls/`, `pwg_ls1/`, `pwgissues/`, `verbs01*`) stay excluded
per `ruff.toml`. Fixtures use real entry data (provenance in
`conftest.py`): metalines from `pwg_ls2/mbh/change_01.txt`, the
csl-orig header form from `pagecolumn/pwg_page_index.py`, correction
lines from `pwg_ls2/p/change_01.txt`._

## Entry points exercised (30 tests)

| Entry point (script) | Tests | What is exercised |
| --- | --- | --- |
| `pwg_ls2/*/parseheadline.py` | 5 | real metalines (`<L>16850<pc>292-3…`, `<L>8<pc>1-0004…`), empty-value keys, 8-copy byte-identity drift lock |
| `pwg_ls2/ak/updateByLine.py` | 6 | `new` replace, `ins` insert-after, `del` remove, `;` comments, old-text mismatch refusal (exit 1), 6-copy byte-identity drift lock |
| `pwg_ls2/p/diff_to_changes.py` | 3 | change-pair generation, **round-trip contract** `updateByLine(old, diff(old,new)) == new`, zero-change case |
| `pwg_ls2/p/make_change3_ls.py` | 8 | `init_entries` metaline→`<LEND>` parsing + line bounds, duplicate-L refusal, single-shot `Entry.Ldict` behavior, `make_number_change` forms 1/2/3/3a on real `<ls>` citation shapes |
| `pagecolumn/pwg_page_index.py` | 5 | `page_of` 2-columns/page, `parse_source` headers+`[PageV-CCCC]` spans, optional `<h>`, float-L Nachtrag form, CLI writes 3 TSV views |
| `prefaces/build_combined.py` | 3 | PAGES table vs 27×3 per-page files, combined `pwgpref_all.{de,en,ru}.md` carry all 27 sections + TOC + scan-source notes (read-only) |

## Known behaviors locked on purpose

- `Entry.Ldict` is class-level state; change builders are single-shot CLIs
  (second `init_entries` in one process exits 1).
- `updateByLine.py` refuses changes whose old-text mismatches the input
  (exit 1) — correction batches must never partially apply silently.
- `parseheadline.py` / `updateByLine.py` exist as per-workdir copies; the
  active-copy groups are byte-identity locked.

_2026-10-11 · H5799 · OxAlpha_
