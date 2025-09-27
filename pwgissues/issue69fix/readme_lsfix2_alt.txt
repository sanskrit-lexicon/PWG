
Brief discussion of lsfix2_alt.py


first usage for temp_pwg_1.txt

python lsfix2_alt.py 01 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_01.txt
output:
(None,5999),(True,8087),(fixed,783),(all,14869) 01 fixwork/lsfix2_pwg_1_01.txt


last usage for temp_pwg_1.txt
python lsfix2_alt.py 14 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_14.txt
(None,9),(True,13068),(fixed,1796),(all,14873) 14 fixwork/lsfix2_pwg_1_14.txt

THe parameter fixopt (01, 02, ..., 14) determines the regex in
routine fix_get_start function.

The intermediate parameters (01 - 13) are incomplete for the present task.
As the fixopt increases, the regex get more complex.
fixopt = 14 is the best (and final) regex used.

-------------
test usage.
python lsfix2_alt.py 14
reads a string from lsfix2_alt_test.py and tries to parse the string
using fixopt = 14.  Writes results to terminal.

example:
python lsfix2_alt.py 14
body = "31,a,4. 6. 87,a,4. 6. 87,b. 32. 97,b,38."   # the string to parse
0000 "31,a,4. 6."
0001 "87,a,4. 6."
0002 "87,b. 32."
0003 "97,b,38."
rest = ""

=======================================================
regex construction.

The regexes are constructed using two features of python,
which are new to me.

---- f-strings
Example python code:

N = '[0-9]+'
A = '[abc]'
P = '\.'
F = 'fg+'
r = f'{N},{A},{N}{P}'
print(r) # [0-9]+,[abc],[0-9]+\.

---- regex non-capturing groups
import re
N = '[0-9]+'
A = '[abc]'
P = '\.'
F = 'fg+'
g1 = f'{N},{A},{N}{P}'
g2 = f'{N},{A}{P}'
g0 = f'(?:{g1}|{g2})' # non-capturing group
h1 = f' {F}{P}'
h0 = f'(?:{h1})'  # non-capturing group
regex = f'^({g0}{h0}*)(.*)$'  # two capturing roups
m = re.search(regex,'12,b,5. fg. 13.a.')
print(m.group(1))  # 12,b,5. fg.
print(m.group(2))  #  13.a.
print(regex)  # ^((?:[0-9]+,[abc],[0-9]+\.|[0-9]+,[abc]\.)(?: fg+\.)*)(.*)$

-------------------------
There are other python parsing libraries for complex tasks
For example
pyparsing
plpy  # python lex-yacc

