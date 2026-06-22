import re

with open('temp_pwg3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def fix_fg_in_content(m):
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

pattern = r'<ls(?: n="([^"]*)")?>([^<]*)</ls>\.\s*<ls(?: n="([^"]*)")?>(fg{1,2}\.\s*)([^<]*)</ls>(\.)?'

result, count = re.subn(pattern, fix_fg_in_content, text)

with open('temp_pwg4.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Done: temp_pwg4.txt written, {count} replacements made")
