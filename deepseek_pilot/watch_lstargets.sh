#!/bin/bash
# Exit (one completion notification) when the lstargets phase finishes — either the
# driver advances to the translate track / finishes, or coverage hits the full slice.
# The driver's own full-exit is reported separately by the harness.
cd "$(dirname "$0")"
DRV="/c/Users/user/AppData/Local/Temp/claude/C--Users-user-Documents-GitHub-PWG/10a86ff5-85c4-4420-993e-6fdfa8754d5a/tasks/bd1u4vf6s.output"

cov() {
  python - <<'PY' 2>/dev/null
import json
ids=set()
try:
    for l in open('out/lstargets/j.jsonl',encoding='utf-8'):
        try: r=json.loads(l)
        except Exception: continue
        if not r.get('_error') and r.get('L'): ids.add(r['L'])
except Exception: pass
print(len(ids))
PY
}

while true; do
  grep -qE "TRACK translate|SCALE COMPLETE" "$DRV" 2>/dev/null && break
  c=$(cov); [ -n "$c" ] && [ "$c" -ge 2404 ] && break
  sleep 60
done
echo "LSTARGETS PHASE FINISHED — coverage $(cov)/2404"
