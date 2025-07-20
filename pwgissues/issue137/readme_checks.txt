
pancar checks.


--------------------------
pwg3:  ratra,adhy,verse

python generate_random.py ALL pwg3 temp_pwg1.txt index.txt check_pwg3_ALL_1.txt check_pwg3_ALL_1_nopagerec.txt

regex_raw = <ls>PAÑCAR. ([0-9]+),([0-9]+),([0-9]+)
2093 written to check_pwg3_ALL_1.txt

manual check of a few, mark
- check : ?    Not checked.
- check : ok   The headword checked and found in verse
- check : not found   The headword checked and NOT found in verse

--------------------------
pwg1:  S. N

--------------------------
pw3:  ratra,adhy,verse

python generate_random.py ALL pw3 temp_pw.txt index.txt check_pw_ALL.txt check_pw3_ALL_nopagerec.txt

write_examples: 92 written to check_pw_ALL.txt
0 instances of 'pagerec not found'

6 examples checked, 5  ok and 1 not found

--------------------------
pwkvn3:  ratra,adhy,verse

python generate_random.py ALL pwkvn3 temp_pwkvn.txt index.txt check_pwkvn3_ALL.txt check_pwkvn3_ALL_nopagerec.txt

write_examples: 15 written to check_pwkvn3_ALL.txt
0 instances of 'pagerec not found'

checked all.  14 ok, one 'not found'

--------------------------
sch3:  ratra,adhy,verse

python generate_random.py ALL sch3 temp_sch.txt index.txt check_sch3_ALL.txt check_sch3_ALL_nopagerec.txt

write_examples: 15 written to check_sch3_ALL.txt
0 instances of 'pagerec not found'

Exactly same list as for pwkvn3 !

checked all.  14 ok, one 'not found'

--------------------------
mw3:  ratra,adhy,verse

python generate_random.py ALL mw3 temp_mw.txt index.txt check_mw3_ALL.txt check_mw3_ALL_nopagerec.txt

write_examples: 14 written to check_mw3_ALL.txt
0 instances of 'pagerec not found'

checked all: 13 ok, 1 'not found'
