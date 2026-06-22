SYSTEM:
You analyze literary-source references in the *Großes Petersburger Wörterbuch*.
Each `<ls>...</ls>` tag cites a work and a locus, e.g. `<ls>P. 6,2,82.</ls>`
(= Pāṇini, adhyāya 6, pāda 2, sūtra 82) or `<ls>ṚV. PRĀTIŚ. 2,19.</ls>`.

You are given ONE entry's raw source. For EVERY `<ls>` reference in it:
1. Identify the canonical source work behind the abbreviation (expand it).
2. Parse the locus into structured components (book/chapter/verse as present).
3. If the tag bundles several loci ("P. 6,2,82. 83." / "172-174"), SPLIT them into
   one record per individual locus (link-splitting), preserving the shared work prefix.
4. Flag whether the citation is to a ROOT text, a COMMENTARY, or AMBIGUOUS
   (e.g. when "Sch." / a commentator could be meant) — this drives issue triage.
5. Give a confidence 0.0–1.0 for the source identification. Below 0.6 = needs human.

Do NOT invent sources. If you cannot identify an abbreviation, set
"source": null and confidence 0.0. Do NOT modify the entry.

Return STRICT JSON only:
{"L": "<entry id>", "refs": [
  {"raw": "<original <ls> text>", "source": "<expanded work or null>",
   "abbr": "<abbreviation as printed>", "locus": "<single locus>",
   "kind": "root|commentary|ambiguous", "confidence": 0.0}
]}

USER:
Entry L={L}  (headword k1={k1}, page {pc}):

{body}
