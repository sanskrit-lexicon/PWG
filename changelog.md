# Changelog

All notable changes to PWG are documented here.

This repository does not currently publish versioned release notes. Entries use
dated maintenance snapshots; keep upcoming work under [Unreleased] until it is
ready for a dated entry.

## [Unreleased]

### Added
- `pagecolumn/` — page/column co-location index. `pwg_page_index.py` derives, from the entry-start column (`<pc>`) in `csl-orig/v02/pwg/pwg.txt`, three views: column → entries that start in it (8,171 columns), physical page (2 columns merged) → entries (4,329 pages), and entry → its column(s)/page(s) (123,366 entries). `pwg_page_verify.py` emits a 70-row scan-verification anchor sheet so the derived `page = (column+1)//2` mapping can be checked against a scan (per-volume front-matter offset, column pairing). Derived `.tsv` views are git-ignored/regenerable; tools + the verification sheet are tracked.

## [Unreleased]

### Added
- Front-matter OCR methods note and cite path: [`prefaces/METHODS.md`](prefaces/METHODS.md) (scan source, engines A/B, translation policy, BibTeX); root [`CITATION.cff`](CITATION.cff) expanded with OCR identifiers and dual-cite message (H1558).

## [1.0.0] - 2026-06-13

### Added
- Added this changelog so repository-level changes have a stable home.
- Recorded the current repository purpose: Scripts and data for correcting and enriching the PWG (Petersburger Wörterbuch, Sanskrit-Wörterbuch, Böhtlingk & Roth, 1855–1875) as part of the Sanskrit Lexicon project.

### Recent Git History
- 2026-05-29 ai-wip: add .pre-commit-config.yaml (yaml-only)
- 2026-05-29 ai-wip: add .github/dependabot.yml for GitHub Actions auto-updates
- 2026-05-29 fix(ci): backport improved validator from batch deploy
- 2026-05-29 fix(ci): exclude pwgissues/ and legacy dirs; skip non-change stats files
- 2026-05-29 fix(ci): add ruff.toml to configure lint exclusions persistently
