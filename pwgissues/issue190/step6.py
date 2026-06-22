import re

with open('temp_pwg5.txt', 'r', encoding='utf-8') as f:
    text = f.read()

result = text

result, c1 = re.subn(r'fg\.\.\s*fg', 'fg', result)
result, c2 = re.subn(r'fgg\.\.\s*fg', 'fg', result)

with open('temp_pwg6.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Done: temp_pwg6.txt written, {c1 + c2} total replacements made")
print(f"  fg.. fg: {c1}, fgg.. fg: {c2}")
