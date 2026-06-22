import re

with open('temp_pwg8.txt', 'r', encoding='utf-8') as f:
    text = f.read()

changes = 0

# Specific: Verz. d. Oxf. H. 102,b, fg -> Verz. d. Oxf. H.
old = '<ls n="Verz. d. Oxf. H. 102,b, fg">11,a, N. 1</ls>'
new = '<ls n="Verz. d. Oxf. H.">11,a, N. 1</ls>'
c = text.count(old)
if c:
    text = text.replace(old, new)
    changes += 1

# General: remove trailing fg/fgg from any n attribute
text, c = re.subn(r'<ls n="([^"]*?) fg{1,2}">', r'<ls n="\1">', text)
changes += c

with open('temp_pwg9.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Done: temp_pwg9.txt written, {changes} changes made")
