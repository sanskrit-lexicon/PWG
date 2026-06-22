import re

with open('temp_pwg0.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def replace_adjacent_fg(m):
    first_attrs = m.group(1) or ''
    first_content = m.group(2)
    fg_word = m.group(4)

    if first_attrs:
        first_attrs = ' n="' + first_attrs + '"'
    return f'<ls{first_attrs}>{first_content}. {fg_word}.</ls>'

# first <ls> may or may not have n attribute
pattern = r'<ls(?: n="([^"]*)")?>([^<]*)</ls>\.\s*<ls n="([^"]*)">(fg{1,2})</ls>(\.)?'

result, count = re.subn(pattern, replace_adjacent_fg, text)

with open('temp_pwg1.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Done: temp_pwg1.txt written, {count} replacements made")
