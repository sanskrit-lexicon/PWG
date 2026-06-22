with open('temp_pwg7.txt', 'r', encoding='utf-8') as f:
    data = f.read()

with open('log.txt', 'r', encoding='utf-8') as f:
    orig_lines = f.read().splitlines()

with open('log1.txt', 'r', encoding='utf-8') as f:
    corr_lines = f.read().splitlines()

changes = 0
for orig, corr in zip(orig_lines, corr_lines):
    if orig != corr:
        data = data.replace(orig, corr)
        changes += 1

with open('temp_pwg8.txt', 'w', encoding='utf-8') as f:
    f.write(data)

print(f"Done: temp_pwg8.txt written, {changes} changes made")
