import re

with open('temp_pwg1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def strip_fg(n):
    m = re.search(r'\s+(fg{1,2}\.)\s*(.*)', n)
    if m:
        return (m.group(1), (n[:m.start()] + ' ' + m.group(2)).strip())
    return (None, n)

def fix_fg_in_n(m):
    first_attrs = m.group(1) or ''
    first_content = m.group(2)
    second_n = m.group(3)
    second_content = m.group(4)
    trail_period = m.group(5) or ''

    # Extract fg/fgg from both n attributes
    first_fg, first_attrs_clean = strip_fg(first_attrs) if first_attrs else (None, first_attrs)
    second_fg, second_n_clean = strip_fg(second_n)

    if not second_fg:
        return m.group(0)

    fg_word = second_fg
    # If first tag also had fg, prefer that word (should be same)
    if first_fg:
        fg_word = first_fg

    first_tag = f'<ls{(" n=\"" + first_attrs_clean + "\"") if first_attrs_clean else ""}>{first_content}. {fg_word}</ls>'
    second_tag_n = f' n="{second_n_clean}"' if second_n_clean else ''
    second_tag = f'<ls{second_tag_n}>{second_content}</ls>{trail_period}'

    return first_tag + ' ' + second_tag

pattern = r'<ls(?: n="([^"]*)")?>([^<]*)</ls>\.\s*<ls n="([^"]*fg{1,2}\.[^"]*)">([^<]*)</ls>(\.)?'

result, count = re.subn(pattern, fix_fg_in_n, text)

with open('temp_pwg2.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Done: temp_pwg2.txt written, {count} replacements made")
