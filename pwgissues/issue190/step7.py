import re

with open('temp_pwg6.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def extract_author(pre_text):
    m = re.match(r'^(.+?\.)\s*(?:\d|[XIV])', pre_text)
    if m:
        return m.group(1)
    return None

def fix_fgg(m):
    n_val = m.group(1) or ''
    before = m.group(2)
    after = m.group(3)
    trail = m.group(4) or ''

    n_str = f' n="{n_val}"' if n_val else ''

    author = n_val
    if not author:
        raw = extract_author(before)
        if raw:
            author = raw.rstrip('.') + '.'

    first_content = re.sub(r'\.\s*$', '', before.rstrip())
    first = f'<ls{n_str}>{first_content}. fgg.</ls>'

    raw_refs = re.split(r'\.\s+', after)
    refs = []
    for r in raw_refs:
        r = r.strip()
        if not r:
            continue
        if r in ('fgg.', 'fg.'):
            if refs:
                refs[-1] = refs[-1] + ' ' + r
            continue
        refs.append(r)

    merged = []
    buf = ''
    for r in refs:
        if r.startswith('(') and not r.rstrip('.').endswith(')'):
            buf = (buf + '. ' + r) if buf else r
            continue
        if buf:
            buf = buf + '. ' + r
            if r.rstrip('.').endswith(')'):
                merged.append(buf)
                buf = ''
            continue
        merged.append(r)
    if buf:
        merged.append(buf)

    has_content = any(re.search(r'[\d\w]', ref) for ref in merged)
    if not has_content:
        return m.group(0)

    rest = []
    for ref in merged:
        ref = ref.strip()
        if not ref:
            continue
        t = ref if ref.endswith('.') or ref.endswith(')') else ref + '.'
        if author:
            rest.append(f'<ls n="{author}">{t}</ls>')
        else:
            rest.append(f'<ls>{t}</ls>')

    if not rest:
        return m.group(0)

    return first + ' ' + ' '.join(rest) + trail

pat = r'<ls(?: n="([^"]*)")?>([^<]*(?:<(?!ls|/ls)[^>]*>[^<]*)*?)fgg\.\s*((?:(?!\s*</ls>).)+?)</ls>(\.)?'

result, count = re.subn(pat, fix_fgg, text)

with open('temp_pwg7.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Done: temp_pwg7.txt written, {count} replacements made")
