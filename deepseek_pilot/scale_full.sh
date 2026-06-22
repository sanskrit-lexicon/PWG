#!/bin/bash
# Scale the full ज slice across all runnable tracks (EN first, then RU), with
# auto-resume: each track is re-run until "0 to do" (every entry has a successful
# record) or a max number of passes. The runner itself retries the flaky link 6x
# per call; this outer loop mops up entries that still exhausted their retries.
# ocrdiff is skipped (needs aligned AB v1e diffs, #180/#163).
set -u
cd "$(dirname "$0")"
ENVF="/c/Users/user/Documents/GitHub/IndologyScholars/.env"
MODEL="deepseek-v4-flash"
WORKERS=12
MAXPASS=15

run_track() {           # $1=track  $2=lang(optional)
  local track="$1" lang="${2:-}" largs=""
  [ -n "$lang" ] && largs="--lang $lang"
  echo "========== TRACK $track $lang =========="
  for p in $(seq 1 $MAXPASS); do
    echo "--- $track $lang pass $p ---"
    out=$(python run_pilot.py --track "$track" $largs --workers $WORKERS \
          --model "$MODEL" --env "$ENVF" 2>&1)
    echo "$out" | tail -2
    # stop when the resume run finds nothing left to do
    echo "$out" | grep -q ", 0 to do," && { echo "$track $lang: complete"; break; }
  done
}

# struct runs LAST: a limit-20 struct validation may still be writing out/struct/j.jsonl
# when this launches; by the time the long lstargets/translate passes finish, it is done.
run_track lstargets
run_track translate en
run_track translate ru
run_track struct

echo "########## DEDUP ##########"
python - <<'PY'
import json, glob, os
slice_L=[json.loads(l)["L"] for l in open('slice/j.jsonl',encoding='utf-8')]
sset=set(slice_L)
for path in glob.glob('out/*/j*.jsonl'):
    recs=[json.loads(l) for l in open(path,encoding='utf-8')]
    best={r["L"]:r for r in recs if r.get("L") in sset and not r.get("_error")}
    with open(path,'w',encoding='utf-8') as w:
        for L in sorted(best,key=int): w.write(json.dumps(best[L],ensure_ascii=False)+"\n")
    print("%-34s %d/%d entries"%(os.path.relpath(path), len(best), len(slice_L)))
PY
echo "########## SCALE COMPLETE ##########"
