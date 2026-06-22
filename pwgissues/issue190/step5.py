import re

with open('temp_pwg4.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def fix_orphan_fg(m):
    first_n = m.group(1) or ''
    first_content = m.group(2)
    second_n = m.group(3) or ''
    fg_word = m.group(4).strip()
    second_rest = m.group(5)
    trail_period = m.group(6) or ''

    first_n_attr = f' n="{first_n}"' if first_n else ''
    second_n_attr = f' n="{second_n}"' if second_n else ''

    first_tag = f'<ls{first_n_attr}>{first_content}. {fg_word}</ls>'
    second_tag = f'<ls{second_n_attr}>{second_rest}</ls>{trail_period}'

    return first_tag + ' ' + second_tag

# Pattern 1: no period between tags (space only) — not handled by step4
no_period_pat = r'<ls(?: n="([^"]*)")?>([^<]*)</ls>\s+<ls(?: n="([^"]*)")?>(fg{1,2}\.\s*)((?:(?!</ls>).)*?)</ls>(\.)?'

# Pattern 2: period between tags (like step4) — missed by step4 due to left-to-right
with_period_pat = r'<ls(?: n="([^"]*)")?>([^<]*)</ls>\.\s*<ls(?: n="([^"]*)")?>(fg{1,2}\.\s*)((?:(?!</ls>).)*?)</ls>(\.)?'

total = 0
result = text

while True:
    result, c1 = re.subn(no_period_pat, fix_orphan_fg, result)
    result, c2 = re.subn(with_period_pat, fix_orphan_fg, result)
    if c1 + c2 == 0:
        break
    total += c1 + c2
    print(f"  pass: {c1} no-period + {c2} with-period = {c1 + c2}")

with open('temp_pwg5.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Done: temp_pwg5.txt written, {total} total replacements made")
