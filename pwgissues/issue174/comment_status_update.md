Quick coordination note — three of you have converged on `pwgissues/issue174/` from different angles, so here is what's there, who built what, and what's the cleanest next step for each of you.

## Tooltips — already drafted

@funderburkjim, the file @Andhrabharati pointed you at — `pwgissues/issue174/pwgab_input_draft.txt` — is exactly the 782/787 tooltip table you were about to start. Same format as `mwab_input.txt`:

```
abbr<TAB><id>abbr</id> <disp>German expansion - English gloss</disp>[ <INFER/>]
```

Headline numbers:
- 787 lines, one per global abbreviation
- **58 flagged `<INFER/>`** — uncertain/inferred expansions awaiting human review
- Format mirrors the MW convention so the tooltips can be wired in without code changes

Two companion files worth a look before you write any new tooltip text:

| File | What it gives you |
|---|---|
| `mw_overlap.txt` | **136 abbreviations** that appear identically in MW (`Abl., Aor., Caus., Dat., Loc., …`) — you can lift MW's `<disp>` for these where the semantics match |
| `mw_diff_case.txt` | 45 abbreviations that match MW under case-insensitive comparison (e.g. PWG `Vergl.` ↔ MW `vergl.`) — same trick, but check casing |
| `pwgab_with_mw_hints.txt` | The full draft with MW's `<disp>` annotated inline as `; MW-disp=...` for cross-reference |

Caveat: a handful diverge by language. `Ind.` in MW = *indeclinable*, in PWG it usually = *Indien / indisch*. The draft flags these with `<INFER/>`.

## On `<lex>` vs `<ab>` for `indecl. / ind. / Ind.`

> `indecl.`, `ind.` and `Ind.` are marked as `<ab>` currently; should they be marked `<lex>`?

- **`indecl.`** — yes, treat as `<lex>`. It's a part-of-speech marker (indeclinable) on the same plane as `adj., adv., f., m., n., interj.` already in your `<lex>` set.
- **`ind.` (lowercase)** — ambiguous: it means *Indikativ* (mood) in some entries and *indisch* (Indian) in others. Should stay `<ab>` and be disambiguated per-entry. The MW overlap file has MW's English gloss; comparing in context will sort it.
- **`Ind.` (capital)** — almost always *Indien / indisch* in PWG, never lexical. Keep as `<ab>`.

So: `indecl.` → `<lex>`; both `ind.` and `Ind.` → stay `<ab>`.

## Markup-fixer + audit

`08_markup_fix.py` is a defensive cleanup pass to run **after** you've merged AB's local overlay onto `temp_pwg_8.txt`. It auto-fixes:

- Nested `<ab><ab>X</ab> Y</ab>` → `<ab>X Y</ab>` (which can land at the boundary of global + local passes)
- Whitespace inside `<ls>/<ab>/<lex>/<is>/<lang>`

And emits `markup_audit.txt` flagging things that need eyes — most usefully the **91 existing `<ab n="?">` placeholders** in `pwg.txt` where the local expansion was never filled in. Those are concrete cleanup targets right now, independent of the new wave of work.

## For AB's local-abbreviation pass

@Andhrabharati, when you come to do the locals, `pwgissues/issue174/disambig/` has 47 per-abbreviation worklists for the 48 short/ambiguous globals (`N.`, `d.`, `p.`, `c.`, `St.`, `W.`, `v. a.`, …). Each file is **clustered by the following word** so similar contexts group together — should let you decide once per cluster rather than once per occurrence. `disambig_index.txt` is the table of contents (occurrence counts + which already have hints in your own local list).

If it helps for the line-diff format Jim asked for, the `updateByLine.py`-style `NNN old / NNN new` pairs in `changes_safe.txt` show the convention.

## Reconciling the counts

For the record, the gap between my 102k (`changes_safe.txt`) and Jim's 178k (`count_ab_8.txt`) isn't a contradiction — my Phase B was a **conservative subset** that only wrapped abbreviations with ≥3 alpha chars and left 48 short/ambiguous ones to AB's local pass. Jim's `temp_pwg_8` includes those short ones (`S., u., Z.` adding ~4,300; `Vgl.` 18,300; `Schol.`/`Sch.` from `<ls>` 9,700; etc.), plus the `<ls>X</ls> → <ab>X</ab>` reclassifications, which my script deliberately didn't touch. Both pipelines arrive at the same target — Jim's is the canonical one going forward.

## TL;DR — proposed next actions

- **@funderburkjim**: start from `pwgab_input_draft.txt`; use `mw_overlap.txt` to copy 136 MW `<disp>` values; fill in the 58 `<INFER/>` entries; flip `indecl.` to `<lex>`; run `08_markup_fix.py` on `temp_pwg_8.txt` once you're happy with it.
- **@Andhrabharati**: use `disambig/*.txt` as the source material for the local-abbreviation pass; output as `NNN old / NNN new` lines against `temp_pwg_8.txt`.
- **declare temporary victory** on global wraps — agreed.
