"""
step1.py - Normalize CDSL to match AB's format conventions.

Transforms applied to CDSL:
1. Wrap <bot>…</bot> in {%…%}
2. <k2>word<h>N  →  <k2>N. word   (hom number moved before the headword)
3. For each <L> block whose <L> number also exists in AB, replace the
   block's header line with AB's header line.
4. Before a bare '— <ab>X</ab>' where X is in the set of <ab> contents
   that AB wraps after <div n="conj">, write '<div n="conj">'.
   Set is computed from AB (caus., partic., desid., intens., pass.,
   Caus., Desid., des., part., Intens., Denom., intrans., insens.).
   Already-wrapped markers are left untouched.
5. '</ab> zu <ls' → '</ab>_zu_<ls'  (broad pattern, incl. <ls n=)
   AB uses the underscore form predominantly (4,200 vs 771 spaced);
   CDSL has it spaced 4,950 times (8 underscored).
9. '</ab> des <ls' → '</ab>_des_<ls'  (CDSL)
   Same convention for 'des'; AB has 128 underscore vs 1 spaced;
   CDSL has 129 spaced, 0 underscored.
6. Collapse multiple spaces into one and remove trailing whitespace.
   AB is clean (0 lines with 2+ spaces); CDSL has 180.
7. '<div n="p">' → '<div n="pf">'
   AB uses <div n="pf"> predominantly (8,664 vs 15 <div n="p">);
   CDSL has 9,198 <div n="p"> and 0 <div n="pf">.

Transforms applied to AB:
8. '</ab> zu <ls' → '</ab>_zu_<ls'
   Same underscore convention as CDSL transform 5; AB still has 771
   spaced forms (4,200 already underscored).
"""
import re
import time


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def extract_l(header_line):
    m = re.match(r'<L>([^<]*?)<pc>', header_line)
    return m.group(1) if m else None


def ab_headers(ab_text):
    """Map <L> number → full header line, from the AB file."""
    result = {}
    for line in ab_text.split('\n'):
        if line.startswith('<L>'):
            n = extract_l(line)
            if n is not None:
                result[n] = line
    return result


def conj_set(ab_text):
    """Set of <ab> contents that AB wraps after <div n="conj">."""
    s = set()
    for m in re.finditer(r'<div n="conj">', ab_text):
        tail = ab_text[m.end():m.end() + 150]
        ab = re.search(r'<ab>([^<]*)</ab>', tail)
        if ab:
            s.add(ab.group(1))
    return s


def transform_ab(text):
    return text.replace('</ab> zu <ls', '</ab>_zu_<ls')


def transform_cdsl(text, headers, conjs):
    out = []
    replaced = 0
    for line in text.split('\n'):
        line = re.sub(r'  +', ' ', line)
        if line.startswith('<L>'):
            n = extract_l(line)
            if n is not None and n in headers:
                line = headers[n]
                replaced += 1
            line = re.sub(r'<k2>([^<]*)<h>([0-9]+)', r'<k2>\2. \1', line)
        line = re.sub(r'<bot>(.*?)</bot>', r'{%<bot>\1</bot>%}', line)
        line = re.sub(
            r'(?<!<div n="conj">)(— <ab>([^<]*)</ab>)',
            lambda m: f'<div n="conj">{m.group(1)}'
                      if m.group(2) in conjs else m.group(1),
            line)
        line = line.replace('</ab> zu <ls', '</ab>_zu_<ls')
        line = line.replace('</ab> des <ls', '</ab>_des_<ls')
        line = line.replace('<div n="p">', '<div n="pf">')
        line = line.rstrip()
        out.append(line)
    return '\n'.join(out), replaced


def main():
    t0 = time.time()

    print("Reading files …")
    cdsl0 = read_file('temp_cdsl_0.txt')
    ab0 = read_file('temp_ab_0.txt')

    print("Transforming AB …")
    ab1 = transform_ab(ab0)

    print("Building AB header index …")
    headers = ab_headers(ab1)
    print(f"  AB <L> headers: {len(headers):,}")

    print("Building AB <div n=\"conj\"> ab-set …")
    conjs = conj_set(ab1)
    print(f"  AB conj-ab contents: {len(conjs)}  {sorted(conjs)}")

    print("Transforming CDSL …")
    cdsl1, replaced = transform_cdsl(cdsl0, headers, conjs)

    print("Writing outputs …")
    write_file('temp_cdsl_1.txt', cdsl1)
    write_file('temp_ab_1.txt', ab1)

    print(f"  CDSL_1: {cdsl1.count(chr(10))+1:,} lines")
    print(f"  AB_1:   {ab1.count(chr(10))+1:,} lines")
    print(f"  Headers replaced from AB: {replaced:,}")
    print(f"  Done in {time.time()-t0:.1f}s")

    import subprocess
    r = subprocess.run(
        'diff temp_cdsl_1.txt temp_ab_1.txt | wc -l',
        shell=True, capture_output=True, text=True
    )
    print(f"  Diff lines: {r.stdout.strip()}")

    for label, pat in [
        ('{%<bot>',        '{%<bot>'),
        ('<bot>',          '<bot>'),
        ('<k2>',           '<k2>'),
        ('<h>',            '<h>'),
        ('<hom>',          '<hom>'),
        ('<div n="conj">', '<div n="conj">'),
        ('</ab>_zu_<ls',   '</ab>_zu_<ls'),
        ('<div n="pf">',   '<div n="pf">'),
    ]:
        c = cdsl1.count(pat)
        a = ab1.count(pat)
        print(f"  {label}: CDSL_1={c}  AB_1={a}  gap={a-c:+d}")


if __name__ == '__main__':
    main()
