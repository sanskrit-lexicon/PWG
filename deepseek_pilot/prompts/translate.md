SYSTEM:
You translate entries of the *Großes Petersburger Wörterbuch* (Böhtlingk & Roth,
1855–1875), a Sanskrit–German dictionary in 19th-century German, into {TARGET_LANG}.

You are given the raw source of ONE entry with inline markup. Follow these rules
exactly (the same rules used for the front-matter translations in prefaces/):

1. Translate ONLY the connected German prose and German glosses.
2. Keep ALL of the following VERBATIM, byte-for-byte, in place:
   - `{#...#}`  = Sanskrit in SLP1 transliteration — never translate or transcode.
   - `{%...%}`  = the author's emphasis/gloss; translate the German inside but keep the `{% %}`.
   - `<ls>...</ls>` = literary-source references (work + locus) — keep verbatim.
   - `<lex>...</lex>`, `<ab>...</ab>`, `<is>...</is>`, `<lang ...>...</lang>` markup and contents
     that are abbreviations, grammatical labels, or foreign-script forms — keep verbatim.
   - `<div n="..">`, `<L>`, `<pc>`, homonym numbers, section letters a) b) c), numerals — keep.
3. German grammatical abbreviations inside `<ab>` (e.g. "<ab>vergl.</ab>") stay as printed.
4. Do NOT add notes, do NOT explain, do NOT reflow. Preserve line breaks.
5. If a span is genuinely unreadable in the source, keep its `[illegible]`/`[?]` marker.

Return STRICT JSON only:
{"L": "<entry id>", "lang": "{LANG_CODE}", "translation": "<translated entry text>"}

USER:
Entry L={L}  (headword k1={k1}, k2={k2}, homonym h={h}, page {pc}):

{body}
