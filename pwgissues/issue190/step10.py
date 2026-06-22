with open('temp_pwg9.txt', 'r', encoding='utf-8') as f:
    text = f.read()

changes = 0

# (1) <ls n="Spr.">2354</ls>. <ls n="Spr.">fg 2358</ls>. -> <ls n="Spr.">2354 fg.</ls> <ls n="Spr.">2358</ls>.
old1 = '<ls n="Spr.">2354</ls>. <ls n="Spr.">fg 2358</ls>.'
new1 = '<ls n="Spr.">2354 fg.</ls> <ls n="Spr.">2358</ls>.'
assert text.count(old1) == 1
text = text.replace(old1, new1)
changes += 1

# (2) <ls n="TS. PRĀT. fg 14,">13</ls>. -> <ls n="TS. PRĀT. 14,">13</ls>.
old2 = '<ls n="TS. PRĀT. fg 14,">13</ls>.'
new2 = '<ls n="TS. PRĀT. 14,">13</ls>.'
assert text.count(old2) == 1
text = text.replace(old2, new2)
changes += 1

# (3) <ab>Z.</ab> 11. fgg {#asi#} -> <ab>Z.</ab> 11. <ab>fgg.</ab> {#asi#}
old3 = '<ab>Z.</ab> 11. fgg {#asi#}'
new3 = '<ab>Z.</ab> 11. <ab>fgg.</ab> {#asi#}'
assert text.count(old3) == 1
text = text.replace(old3, new3)
changes += 1

with open('temp_pwg10.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Done: temp_pwg10.txt written, {changes} changes made")
