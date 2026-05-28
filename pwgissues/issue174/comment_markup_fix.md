{% raw %}
## Markup fixer + audit for `pwg.txt`

Adding `08_markup_fix.py` to `pwgissues/issue174/`. It does two things, both safe to re-run after Phase B is applied **and** after @Andhrabharati's local-abbreviation overlay lands.

### What it auto-fixes

| Pattern | Result |
|---|---|
| `<ab><ab>vor.</ab> W.</ab>` | `<ab>vor. W.</ab>` |
| `<ab n="X"><ab>St.</ab></ab>` | `<ab n="X">St.</ab>` |
| `<ab>foo<ab>bar</ab>baz</ab>` | `<ab>foobarbaz</ab>` |
| `<ls> GORR. 1,69,9 </ls>` | `<ls>GORR. 1,69,9</ls>` |
| `<lang n="greek"> ἀ</lang>` | `<lang n="greek">ἀ</lang>` |

Whitespace trimming applies to `<ls>`, `<ab>`, `<lex>`, `<is>`, `<lang>` (the five tag pairs that currently exist in `pwg.txt`). The original file is never modified — output goes to `pwg_fixed.txt`, with the full diff in `markup_fix_changes.txt` (updateByLine format).

### What it found in current `pwg.txt`

- **0** nested `<ab>` — `pwg.txt` is currently clean. The fixer exists for the contingency where Phase B's `changes_safe.txt` and AB's local overlay produce nesting at their boundary.
- **4** whitespace trims: 1 `<ls>` and 3 `<lang n="greek">` had leading/trailing spaces.
- **91** `<ab n="?">` placeholders — the literal `?` was left as the local-abbreviation expansion. These are the single biggest cleanup target. Examples:
  ```
  L55:   {%des%} <ab n="?">D.</ab> {%unwürdig%}
  L2019: Sg. N. {#a/kzi#}, <ab n="?">V.</ab>
  L63752: {%Desmodium gangeticum%} <ab n="?">DC.</ab>
  ```
  Many can be resolved by cross-referencing `PWG_abbr_local.txt`.
- **9** adjacent `</ab> <ab>` — all look intentional (e.g. `<ab>N. pr.</ab> <ab>u. s. w.</ab>`); listed for verification rather than auto-merge.

### Broader cleanup checklist (in `markup_audit.txt`)

1. **`<ab n="?">` placeholders** — 91 occurrences, full list with line numbers in the audit.
2. **Adjacent `</ab> <ab>`** — 9 occurrences, verify they are separate intended abbreviations.
3. **Phase B false positives** — review `changes_safe.txt` for end-of-line `<ab>X</ab>` where `X` is also a common German word (only `vor.` denylisted so far).
4. **Local-overlay collision** — Phase B may wrap inner pieces of compounds (`<ab>u. d.</ab> O.` vs. AB's intended `<ab n="dem und dem Ort">u. d. O.</ab>`). AB's pass resolves these; re-running the fixer afterward catches any nesting they create.
5. **Residual hyphenation** — line-break hyphens carried over from earlier digitisation (cf. ApteES thread); not addressed here, needs a dedicated pass.
6. **`<INFER/>` expansions** — 58 entries in `pwgab_input_draft.txt` flagged as inferred German expansions; `grep '<INFER/>' pwgab_input_draft.txt` lists them.
7. **Zero-usage AB-tags** — `<ns>`, `<iw>`, `<mng>`, `<ed>`, `<ms>`, `<pe>`, `<per>` have no occurrences and no semantic definition; deferred until @Andhrabharati confirms intent.

### Usage

```sh
cd pwgissues/issue174
python 08_markup_fix.py
# default in:  ../../../csl-orig/v02/pwg/pwg.txt
# default out: pwg_fixed.txt

# Or on the wrapped output:
python 08_markup_fix.py pwg_with_abs.txt pwg_with_abs_fixed.txt
```

Synthetic-input tests of the nesting fixer all pass.
{% endraw %}
