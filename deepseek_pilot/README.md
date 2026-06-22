# DeepSeek pilot — ज (ja) slice

A bounded, four-track pilot for putting an LLM (DeepSeek) over the PWG dictionary.
Everything here produces **derived artifacts** — the canonical source
[../../csl-orig/v02/pwg/pwg.txt](../../csl-orig/v02/pwg/pwg.txt) is never modified.

## Input

Canonical source is the inline-markup `.txt` (the `pwgxml.zip` download is dead;
the `.txt` is the source the `.xml` is generated from). The slice extractor reads
it directly from the sibling `csl-orig` checkout.

## Slice

`python extract_slice.py --letter j` → [slice/j.jsonl](slice/j.jsonl) (2,404 ज entries).
SLP1 is case-sensitive, so `j` = ज only (झ is `J`).

## Tracks

| Track | What DeepSeek does | Output | Maps to |
|---|---|---|---|
| `translate` | EN/RU translation of German prose; Sanskrit/`<ls>`/markup kept verbatim | `out/translate/j.{en,ru}.jsonl` | prefaces/ → body |
| `lstargets` | Resolve + split `<ls>` refs, flag root/commentary, confidence-scored | `out/lstargets/j.jsonl` | DTB issues (#133,#166,#172…) |
| `struct` | Extract headword/grammar/senses; flag `<lang>`/`<fg>`/`<lex>`/transcode issues | `out/struct/j.jsonl` | SD (#188,#190,#91,#78) |
| `ocrdiff` | Adjudicate Cologne vs Andhrabharati v1e diffs | `out/ocrdiff/j.jsonl` | DQ (#191,#163,#180) |

## Run

```sh
# 1. extract the slice (done; re-run to refresh)
python extract_slice.py --letter j

# 2. preview a filled prompt without any API call or key
python run_pilot.py --track struct --limit 1 --dry-run

# 3. add the key, then run a small batch
cp .env.example .env   # then edit .env, paste OPENMODEL_API_KEY
python run_pilot.py --track translate --lang en --limit 20
python run_pilot.py --track lstargets --limit 20
python run_pilot.py --track struct --limit 20

# 4. scale to the full slice (resumes; re-running skips done L ids)
#    translation order: EN first, then RU
python run_pilot.py --track translate --lang en
python run_pilot.py --track translate --lang ru
```

`ocrdiff` needs aligned A/B diffs from the AB v1e merge work (#180/#163):
`python run_pilot.py --track ocrdiff --ab-diffs path/to/diffs.jsonl`.

## Go/no-go before scaling beyond ज

Per track, hand-check a sample and record: translation fidelity, % `<ls>` resolved
≥0.6 confidence vs flagged, real markup issues vs false positives, OCR-adjudication
precision. If precision clears the bar, extend letter-by-letter.

## Notes

- `.env` and `out/` are gitignored. The slice JSONL is regenerable, also gitignored.
- Provider: OpenModel gateway (OpenAI-compatible), `OPENMODEL_API_KEY`,
  base `https://api.openmodel.ai/v1`, model `deepseek-chat` for bulk.
- JSON mode + `temperature=0` for reproducible, machine-mergeable output.
