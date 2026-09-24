# PWG handoffs

_Created: 24-09-2026 · Last updated: 24-09-2026_

PWG-related handoffs are minted and tracked HERE, not in
[gasyoun/Uprava](https://github.com/gasyoun/Uprava)/handoffs/ — MG ruling
24-09-2026: «move them from Uprava to PWG repo. And the ones to come as well».

Scope: PWG dictionary text, `<ls>`/bibliography (`pwgbib`), link-target and
correction work under this repo. **PWG→RU translation work is NOT in scope** —
it lives in its own repos ([pwg-ru-data](https://github.com/gasyoun/pwg-ru-data),
pwg_ru_prompts) and its handoffs stay on their own tracks.

Live handoffs:

- ~~`H5465-OxAlpha_csl-observatory_pwg-ls-additions-defects_24.09.26.md`~~ —
  ✅ EXECUTED 24-09-2026 (OxAlpha-tier file; executed by GLM
  `zai-coding-plan/glm-5.3-flash` after the assigned lane stalled, MG «бери»):
  215 `[Cologne Addition]` entries ([csl-observatory#236](https://github.com/sanskrit-lexicon/csl-observatory/pull/236)),
  defect classes on [#240](https://github.com/sanskrit-lexicon/PWG/issues/240#issuecomment-5820130011),
  upstream [csl-pywork#94](https://github.com/sanskrit-lexicon/csl-pywork/pull/94),
  kosha row `pwg-ls-additions-215` ([gasyoun/kosha#645](https://github.com/gasyoun/kosha/pull/645),
  merge pending a stale-base guard ruling on the README count bump).
- `H5466-Fable_csl-observatory_pwg-ls-full-classifier_24.09.26.md` — full-set
  `<ls>` taxonomy classifier: person+subtype, book, journal, kośa, Hdschr.,
  German series; rules + MW name-lexicon + human-residue sheet (hard).

Note: the Uprava queue tools (`handoff.py go`, `handoff_batch_drain.py`,
`precheck_handoff.py`) scan only `Uprava/handoffs/` — execute these with the
Read-starter line pointing at this directory, or move them back temporarily.

_Гасунс_
