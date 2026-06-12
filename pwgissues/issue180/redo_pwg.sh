#!/usr/bin/env bash

if [ $# -ne 3 ]; then
    echo "Usage: $0 base vn pwg"
    exit 1
fi

base="$1"
vn="$2"
pwg="$3"

# echo "all three args are present"
echo "Restore line breaks from $base. Result is tempredo_base.txt"

python basevn/div_split.py $base tempredo_base.txt

echo "join temp_redo_base.txt and $vn. Result is tempredo_lend.txt"

python basevn/basevn_join.py tempredo_base.txt $vn tempredo_lend.txt

echo "Restore LEND line breaks from tempredo_lend.txt"
python basevn/lend.py RESTORE tempredo_lend.txt $pwg

echo ""
echo "$pwg constucted"
echo "PLEASE REMOVE tempredo_base.txt and tempredo_lend.txt when done"



