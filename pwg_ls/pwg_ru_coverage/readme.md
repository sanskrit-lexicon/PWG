# pwg_ru_coverage — literary-source link coverage of the PWG article subset

_Created: 02-07-2026 · Last updated: 02-07-2026_

Coverage measurement of the `<ls>` literary-source citations in the **PWG
article subset** — the ~51 roots translated to Russian/English and published at
[gasyoun.github.io/SanskritLexicography](https://gasyoun.github.io/SanskritLexicography/).
It reports how many citations resolve to a Cologne target (a page **scan** or a
digital-**HTML** page) and which works have no target yet.

**Scope.** This measures only the translated article subset, **not the whole PWG
dictionary**. Full-dictionary `<ls>` extraction and the works bibliography live
next door in [`pwg_dhaval/`](https://github.com/sanskrit-lexicon/PWG/tree/main/pwg_ls/pwg_dhaval)
and [`pwgbib/`](https://github.com/sanskrit-lexicon/PWG/tree/main/pwg_ls/pwgbib).

## Files (all auto-generated — do not edit by hand)

- [CITATION_SOURCES.md](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwg_ru_coverage/CITATION_SOURCES.md) — abbreviation → scan/HTML target + per-abbreviation coverage.
- [UNCOVERED_SOURCES.md](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwg_ru_coverage/UNCOVERED_SOURCES.md) — most-cited works with **no** Cologne target, by frequency.
- [COVERAGE_COMPARISON.md](https://github.com/sanskrit-lexicon/PWG/blob/main/pwg_ls/pwg_ru_coverage/COVERAGE_COMPARISON.md) — covered vs uncovered, the coverage frontier, and provenance (who/when).
- `citation_sources.json`, `uncovered_sources.json`, `coverage_comparison.json` — the same data, machine-readable.

## How it is generated

The generator and its input data live in the **RussianTranslation** workspace
(the translation pipeline), which is where the DE/RU/EN corpus and the `<ls>`
resolver are:

- generator: [`RussianTranslation/src/build_citation_index.py`](https://github.com/gasyoun/SanskritLexicography/blob/master/RussianTranslation/src/build_citation_index.py)
- resolver: [`RussianTranslation/src/ls_resolver.py`](https://github.com/gasyoun/SanskritLexicography/blob/master/RussianTranslation/src/ls_resolver.py) (a Python port of the canonical [`csl-app/lib/core/ls_service.dart`](https://github.com/sanskrit-lexicon/csl-app/blob/main/lib/core/ls_service.dart))

To refresh these reports, run (with PWG checked out as a sibling of
SanskritLexicography, which is the default output target):

```sh
python RussianTranslation/src/build_citation_index.py
# or explicitly:
python RussianTranslation/src/build_citation_index.py --out-dir <path>/PWG/pwg_ls/pwg_ru_coverage
```

_Dr. Mārcis Gasūns_
