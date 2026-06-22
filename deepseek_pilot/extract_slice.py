#!/usr/bin/env python3
"""Extract a single-letter pilot slice from csl-orig PWG source into JSONL.

The canonical PWG source is csl-orig/v02/pwg/pwg.txt (inline-markup .txt, NOT
the generated .xml). Each entry runs from a `<L>` header line to `<LEND>`:

    <L>26306<pc>3-0001<k1>ja<k2>ja<h>1
    1. {#ja#}¦ ...German prose with <ls>/<lex>/<lang>/<ab> markup...
    <LEND>

We pull every entry whose <k1> headword begins with the requested SLP1 letter
and emit one JSON object per line:

    {"L": "26306", "pc": "3-0001", "k1": "ja", "k2": "ja", "h": "1", "body": "..."}

Nothing here touches the source file. Output is a derived artifact.

Usage:
    python extract_slice.py            # default: letter "j" (ja), -> slice/ja.jsonl
    python extract_slice.py --letter j --out slice/ja.jsonl
"""
from __future__ import print_function
import argparse
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SRC = os.path.normpath(
    os.path.join(HERE, "..", "..", "csl-orig", "v02", "pwg", "pwg.txt")
)

# <L>NNN<pc>V-PPPP<k1>...<k2>...<h>N   (h is optional)
HDR = re.compile(
    r"^<L>(?P<L>\d+)<pc>(?P<pc>[^<]*)<k1>(?P<k1>[^<]*)<k2>(?P<k2>[^<]*)(?:<h>(?P<h>\d+))?"
)


def iter_entries(path):
    """Yield (header_dict, body_str) for each <L>..<LEND> block."""
    with open(path, "r", encoding="utf-8") as fh:
        hdr = None
        buf = []
        for line in fh:
            m = HDR.match(line)
            if m:
                hdr = m.groupdict()
                buf = []
                continue
            if hdr is None:
                continue
            if line.startswith("<LEND>"):
                yield hdr, "".join(buf).strip()
                hdr = None
                buf = []
                continue
            buf.append(line)


def slp1_letter_match(k1, letter):
    """True if k1 belongs to the requested SLP1 consonant letter.

    SLP1 is case-sensitive: ja=ज is 'j', JHa=झ is 'J'. So a simple lowercase
    prefix test on the exact case is correct and will not pull in झ.
    """
    return k1.startswith(letter)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=DEFAULT_SRC, help="path to pwg.txt")
    ap.add_argument("--letter", default="j", help="SLP1 initial to slice (default j = ja/ज)")
    ap.add_argument("--out", default=None, help="output JSONL path")
    args = ap.parse_args()

    out = args.out or os.path.join(HERE, "slice", "%s.jsonl" % args.letter)
    os.makedirs(os.path.dirname(out), exist_ok=True)

    if not os.path.exists(args.src):
        sys.exit("source not found: %s" % args.src)

    n = 0
    with open(out, "w", encoding="utf-8") as w:
        for hdr, body in iter_entries(args.src):
            if not slp1_letter_match(hdr["k1"], args.letter):
                continue
            rec = {
                "L": hdr["L"],
                "pc": hdr["pc"],
                "k1": hdr["k1"],
                "k2": hdr["k2"],
                "h": hdr.get("h"),
                "body": body,
            }
            w.write(json.dumps(rec, ensure_ascii=False) + "\n")
            n += 1

    print("wrote %d entries -> %s" % (n, out))


if __name__ == "__main__":
    main()
