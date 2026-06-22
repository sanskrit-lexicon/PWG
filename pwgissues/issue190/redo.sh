#!/bin/sh
# Redo the full fg/fgg correction pipeline on temp_pwg0.txt
# Usage: sh redo.sh
# Requires: python3

set -e

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: python3 not found" >&2
    exit 1
fi

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "=== Step 1: Merge adjacent <ls> tags where second has fg/fgg ==="
python3 step1.py

echo ""
echo "=== Step 2: Extract fg/fgg from n attributes ==="
python3 step2.py

echo ""
echo "=== Step 3: Second pass for consecutive fg/fgg tags ==="
python3 step3.py

echo ""
echo "=== Step 4: Merge fg/fgg from start of content with preceding tag ==="
python3 step4.py

echo ""
echo "=== Step 5: Merge remaining orphan fg/fgg at content start (looping) ==="
python3 step5.py

echo ""
echo "=== Step 6: Normalize redundant fg.. fg and fgg.. fg sequences ==="
python3 step6.py

echo ""
echo "=== Step 7: Split tags at internal fgg ==="
python3 step7.py

echo ""
echo "=== Step 8: Manual corrections from log1.txt ==="
python3 step8.py

echo ""
echo "Done: temp_pwg1.txt (step1), temp_pwg2.txt (step2), temp_pwg3.txt (step3), temp_pwg4.txt (step4), temp_pwg5.txt (step5), temp_pwg6.txt (step6), temp_pwg7.txt (step7), temp_pwg8.txt (step8)"
