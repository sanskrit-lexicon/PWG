"""
step2.py - Restore </ls> / <ls n="..."> tags into AB from CDSL.

For line pairs (CDSL_1, AB_1) aligned within the same <L> block, if the
ONLY difference is that AB is missing some '</ls>' and/or '<ls n="...">'
tokens (optionally plus AB's '√' root marker after <hom>N.</hom>), merge
the missing tokens into AB's line (AB's '√' kept) in the AB output.

Inputs : temp_cdsl_1.txt, temp_ab_1.txt
Output : temp_ab_2.txt  (AB_1 with the qualifying lines merged)
"""
import re
import difflib
import time

TOK = re.compile(r'<ls n="[^"]*">|</ls>')
NATTR = re.compile(r'n="[^"]*"')


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def merge_ls(c, a):
    """If AB line 'a' is CDSL line 'c' with zero or more '</ls>'/'<ls n="...">'
    tokens deleted (optionally with '√' root markers inserted — AB writes
    '√' before a root after <hom>N.</hom> where CDSL does not), return 'a'
    with those tokens re-inserted and AB's '√' kept.

    Returns None if the lines differ in any other way, or if nothing would
    change. The result always contains all of 'a', so no AB content is lost."""
    if c == a:
        return None
    out = []
    i = j = 0
    while i < len(c):
        if j < len(a) and c[i] == a[j]:
            out.append(c[i])
            i += 1
            j += 1
        elif j < len(a) and a[j] == '√':
            out.append('√')
            j += 1
        else:
            m = TOK.match(c, i)
            if not m:
                return None
            out.append(c[i:m.end()])
            i = m.end()
    out.append(a[j:])
    res = ''.join(out)
    return None if res == a else res


def ls_only(s):
    """True iff s is made up solely of '</ls>'/'<ls n="...">' tokens and
    whitespace."""
    pos = 0
    while pos < len(s):
        while pos < len(s) and s[pos] in ' \t':
            pos += 1
        if pos >= len(s):
            break
        m = TOK.match(s, pos)
        if not m:
            return False
        pos = m.end()
    return True


def is_subset_delete(c, a):
    """True iff a == c with zero or more '</ls>'/'<ls n="...">' tokens
    deleted and nothing else changed (segment-level check)."""
    if c == a:
        return False
    i = j = 0
    while i < len(c):
        if j < len(a) and c[i] == a[j]:
            i += 1
            j += 1
        else:
            m = TOK.match(c, i)
            if not m:
                return False
            i = m.end()
    return j == len(a)


def merge_segments(segs):
    """Build the merged AB line from one porcelain group's segments.

    Git's word-diff already aligns the CDSL and AB sides. For each '-/+'
    pair (a changed region), if the '+' segment is the '-' segment with only
    ls tokens removed, restore the '-' segment (the missing markup) into the
    output; otherwise keep '+' (AB's own content, e.g. '<ab>adj.</ab>' vs
    CDSL's '<lex>adj.</lex>'). A lone '-' that is entirely ls tokens is
    restored too; other CDSL-only content ('<div n="...">', etc.) is dropped.

    Returns (merged_line, changed)."""
    out = []
    changed = False
    i = 0
    n = len(segs)
    while i < n:
        s = segs[i]
        if s[0] == ' ':
            out.append(s[1:])
        elif s[0] == '-':
            if i + 1 < n and segs[i + 1][0] == '+':
                nxt = segs[i + 1]
                if is_subset_delete(s[1:], nxt[1:]):
                    out.append(s[1:])
                    changed = True
                else:
                    out.append(nxt[1:])
                i += 1
            elif ls_only(s[1:]):
                out.append(s[1:])
                changed = True
        else:  # '+'
            out.append(s[1:])
        i += 1
    return ''.join(out), changed


def match_run(c_lines, a_lines):
    """Maximum bipartite matching between a replace run's CDSL lines and
    AB lines where merge_ls(c, a) is not None.

    Returns {ab_index: (cdsl_index, merged_line), ...}. Each AB line is
    replaced by its merged line (CDSL's missing ls tokens inserted, AB's
    '√' kept); unmatched AB lines are kept; unmatched CDSL lines are
    dropped (as in the old positional pairing)."""
    n, m = len(c_lines), len(a_lines)
    adj = []
    for j in range(m):
        row = []
        for i in range(n):
            ml = merge_ls(c_lines[i], a_lines[j])
            if ml is not None:
                row.append((i, ml))
        adj.append(row)

    # augmenting-path maximum matching (runs are small)
    used_c = {}
    match_a = {}

    def augment(j, visited):
        for i, ml in adj[j]:
            if i in visited:
                continue
            visited.add(i)
            if i not in used_c or augment(used_c[i], visited):
                used_c[i] = j
                match_a[j] = (i, ml)
                return True
        return False

    for j in range(m):
        augment(j, set())
    return match_a


def blocks(text):
    """[(l_number or None, [lines, incl. the <L> header line]), ...]"""
    lines = text.split('\n')
    bs = []
    cur = [None, []]
    for ln in lines:
        if ln.startswith('<L>'):
            bs.append(cur)
            m = re.match(r'<L>([^<]*?)<pc>', ln)
            cur = [m.group(1) if m else None, [ln]]
        else:
            cur[1].append(ln)
    bs.append(cur)
    return bs


def porcelain_groups(text):
    """Parse `git diff --word-diff=porcelain` text into (ab_index, [line_segments]).

    Each '~'-terminated group is one line of the AB side (in file order); ab_index is
    anchored by the '@@ -n +m @@' hunk headers and advanced per group."""
    groups = []
    cur = []
    idx = -1
    for l in text.split('\n'):
        if l.startswith('@@'):
            m = re.match(r'@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@', l)
            if m:
                idx = int(m.group(1)) - 1
            continue
        if l.startswith(('diff --git', 'index ', '--- ', '+++ ')):
            continue
        if l.startswith('~'):
            groups.append((idx, cur))
            cur = []
            idx += 1
        else:
            cur.append(l)
    return groups


def restore_from_git_diff(cdsl_file, ab_file, worddiff_file, restore_to_lines):
    """Phase B: use git's word-diff (porcelain) alignment to restore AB lines
    missing '</ls>'/'<ls n="...">' tokens that CDSL has.

    Git's character-level alignment handles cases the block/line matching of
    Phase A cannot: CDSL keeping an entry on one line while AB splits it across
    several (e.g. <div n="conj"> sections). Per porcelain group, merge_segments
    restores the missing tokens from each '-/+' pair while keeping AB's own
    content ('<ab>adj.</ab>' vs CDSL's '<lex>adj.</lex>', AB's '√', etc.).

    Iterated to a fixpoint: each restore changes git's alignment and can make
    further '-/+' pairs restorable, so the pass repeats until nothing changes.

    restore_to_lines is the AB line list, mutated in place. Returns #restored."""
    import subprocess
    total = 0
    while True:
        r = subprocess.run(
            ['git', 'diff', '--no-index', '--word-diff=porcelain',
             cdsl_file, ab_file],
            capture_output=True, text=True)
        write_file(worddiff_file, r.stdout)

        restored = 0
        for gidx, segs in porcelain_groups(r.stdout):
            if not segs:
                continue
            merged, changed = merge_segments(segs)
            if not changed:
                continue
            a_side = ''.join(s[1:] for s in segs if s[0] in ' +')
            # locate the exact AB line near the '@@'-anchored index
            for p in range(max(0, gidx - 20), min(len(restore_to_lines), gidx + 2000)):
                if restore_to_lines[p] == a_side:
                    restore_to_lines[p] = merged
                    restored += 1
                    break
        total += restored
        if restored == 0:
            break
        # write back so the next iteration's git diff sees the restored lines
        write_file(ab_file, '\n'.join(restore_to_lines))
    return total


def main():
    t0 = time.time()
    print('Reading files …')
    cdsl = read_file('temp_cdsl_1.txt')
    ab = read_file('temp_ab_1.txt')

    print('Aligning <L> blocks …')
    cblks = blocks(cdsl)
    ablks = blocks(ab)
    ab_by_l = {k: v for k, v in ablks}

    print('Scanning line pairs …')
    restored = 0
    kept = []
    for k, cblock in cblks:
        ablock = ab_by_l.get(k)
        if ablock is None:
            continue
        sm = difflib.SequenceMatcher(a=cblock, b=ablock, autojunk=False)
        out = []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                out.extend(cblock[i1:i2])
            elif tag == 'delete':
                pass
            elif tag == 'insert':
                out.extend(ablock[j1:j2])
            else:  # replace
                m = match_run(cblock[i1:i2], ablock[j1:j2])
                for x in range(j2 - j1):
                    if x in m:
                        out.append(m[x][1])
                        restored += 1
                    else:
                        out.append(ablock[j1 + x])
        kept.extend(out)

    ab2 = '\n'.join(kept)
    write_file('temp_ab_2.txt', ab2)

    print(f'  Phase A restored (block subset-delete): {restored:,}')

    print('Phase B: git word-diff ls-token restore …')
    ab2_lines = ab2.split('\n')
    restored_b = restore_from_git_diff(
        'temp_cdsl_1.txt', 'temp_ab_2.txt', 'worddiff_porcelain.txt', ab2_lines)
    ab2 = '\n'.join(ab2_lines)
    write_file('temp_ab_2.txt', ab2)
    print(f'  Phase B restored (git word-diff): {restored_b:,}')

    print(f'  AB_2 lines: {ab2.count(chr(10))+1:,}')
    print(f'  Done in {time.time()-t0:.1f}s')

    import subprocess
    r = subprocess.run(
        'diff temp_cdsl_1.txt temp_ab_2.txt | wc -l',
        shell=True, capture_output=True, text=True)
    print(f'  Diff CDSL_1 vs AB_2: {r.stdout.strip()}')


if __name__ == '__main__':
    main()
