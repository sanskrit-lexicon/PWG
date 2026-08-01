"""
step2.py - Restore </ls> / <ls n="..."> tags into AB from CDSL.

For line pairs (CDSL_1, AB_1) aligned within the same <L> block, if the
ONLY difference is that AB is missing some '</ls>' and/or '<ls n="...">'
tokens (subset deletion; nothing else differs), keep the CDSL line in the
AB output instead of AB's line.

Inputs : temp_cdsl_1.txt, temp_ab_1.txt
Output : temp_ab_2.txt  (AB_1 with the qualifying lines replaced)
"""
import re
import difflib
import time

TOK = re.compile(r'<ls n="[^"]*">|</ls>')


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def is_subset_delete(c, a):
    """True iff AB line 'a' is CDSL line 'c' with zero or more of the
    tokens '</ls>' / '<ls n="...">' deleted and nothing else changed."""
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
        i = j = 0
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                out.extend(cblock[i1:i2])
                i, j = i2, j2
            elif tag == 'delete':
                i = i2
            elif tag == 'insert':
                out.extend(ablock[j1:j2])
                j = j2
            else:  # replace
                n = min(i2 - i1, j2 - j1)
                for x in range(n):
                    c = cblock[i1 + x]
                    a = ablock[j1 + x]
                    if is_subset_delete(c, a):
                        out.append(c)
                        restored += 1
                    else:
                        out.append(a)
                if n < i2 - i1:
                    i = i1 + n
                if n < j2 - j1:
                    out.extend(ablock[j1 + n:j2])
                i, j = i1 + n, j1 + n
        kept.extend(out)

    ab2 = '\n'.join(kept)
    write_file('temp_ab_2.txt', ab2)

    print(f'  Restored CDSL lines into AB: {restored:,}')
    print(f'  AB_2 lines: {ab2.count(chr(10))+1:,}')
    print(f'  Done in {time.time()-t0:.1f}s')

    import subprocess
    r = subprocess.run(
        'diff temp_cdsl_1.txt temp_ab_2.txt | wc -l',
        shell=True, capture_output=True, text=True)
    print(f'  Diff CDSL_1 vs AB_2: {r.stdout.strip()}')


if __name__ == '__main__':
    main()
