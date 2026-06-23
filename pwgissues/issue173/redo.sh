#!/bin/sh
# Redo the ṚV. PRĀT. / ṚV. Prāt. reference pipeline.
# Usage: sh redo.sh
# Requires: python3

set -e

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: python3 not found" >&2
    exit 1
fi

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

# Attempt to locate csl-orig for sourcing dictionary files
CSL_ORIG=""
for candidate in \
    "$DIR/../../sanskrit-lexicon/csl-orig" \
    "$DIR/../../../csl-orig" \
    /Users/Shared/sanskrit-lexicon/csl-orig \
    /c/xampp/htdocs/cologne/csl-orig; do
    if [ -d "$candidate/v02/pwg" ]; then
        CSL_ORIG="$candidate"
        break
    fi
done

fetch_dict() {
    local name="$1"  # e.g. pwg
    local out="$2"   # e.g. temp_pwg_0.txt
    if [ -f "$out" ]; then
        echo "  $out exists, skipping"
        return
    fi
    if [ -n "$CSL_ORIG" ]; then
        echo "  Copying from $CSL_ORIG/v02/$name/${name}.txt"
        cp "$CSL_ORIG/v02/$name/${name}.txt" "$out"
    else
        echo "  Error: $out not found and csl-orig not located"
        exit 1
    fi
}

echo "========================================"
echo " Step 0: Obtain dictionary copies"
echo "========================================"
fetch_dict pwg    temp_pwg_0.txt
fetch_dict pw     temp_pw_0.txt
fetch_dict pwkvn  temp_pwkvn_0.txt
fetch_dict sch    temp_sch_0.txt
fetch_dict mw     temp_mw_0.txt

echo ""
echo "========================================"
echo " Step 1: Analyze ṚV. PRĀT. refs"
echo "========================================"
python3 lsfix2.py pwg   temp_pwg_0.txt   lsfix2_pwg_0.txt
python3 lsfix2.py pw    temp_pw_0.txt    lsfix2_pw_0.txt
python3 lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt
python3 lsfix2.py sch   temp_sch_0.txt   lsfix2_sch_0.txt

echo ""
echo "========================================"
echo " Step 2: Apply pw corrections"
echo "========================================"
python3 dict_replace2.py temp_pw_0.txt lsfix2_pw_0.txt temp_pw_1.txt
# temp_pwg_1.txt is identical to temp_pwg_0.txt (no auto-fixable refs)
cp temp_pwg_0.txt temp_pwg_1.txt

echo ""
echo "========================================"
echo " Step 3: Build scan repo index"
echo "========================================"
python3 combine_index.py
python3 make_js_index.py index.txt index.js

echo ""
echo "========================================"
echo " Summary"
echo "========================================"
echo "pwg:   $(grep -c '^True'   lsfix2_pwg_0.txt) True  / $(grep -c '^None'   lsfix2_pwg_0.txt) None  / $(grep -c '^False'   lsfix2_pwg_0.txt) False"
echo "pw:    $(grep -c '^True'   lsfix2_pw_0.txt) True  / $(grep -c '^fixed'  lsfix2_pw_0.txt) fixed / $(grep -c '^None'   lsfix2_pw_0.txt) None  / $(grep -c '^False'   lsfix2_pw_0.txt) False"
echo "pwkvn: $(grep -c '^True'   lsfix2_pwkvn_0.txt) True"
echo "sch:   $(grep -c '^True'   lsfix2_sch_0.txt) True"
echo "index: $(wc -l < index.txt) records in index.txt"

echo ""
echo "Done."
