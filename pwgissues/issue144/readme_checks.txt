
Manual check for pwg before basicadjust updated.


python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg_man.txt
regex_raw = <ls>TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 2599 instances in kosha

===================================================
Checks for all dictionaries after basicadjust updated.

----------------------------------------------------
First, pwg

python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg.txt

regex_raw = <ls>TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 2599 instances in kosha

One NOT FOUND: key (3, 1, 1, 7): III	10	3	1	1	6b	9a	3
L= 24902, hw= car, pc=2-0952


-----------------------------------
Random checks between pw , the pdf and index

python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt

regex_raw = <ls>TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 266 instances in kosha

All in this random sample checked.
  One uncertain:
  key (2, 4, 5, 7): I	252	2	4	5	4b	7a	245
L= 130470, hw= staraRa, pc=7-201-c
check: ? stfRanti

-----------------------------------
Random checks between pwkvn , the pdf and index

python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt
regex_raw = <ls>TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 45 instances in kosha

All in this random sample checked.


-----------------------------------
Random checks between sch , the pdf and index

python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt

regex_raw = <ls>TBr. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 48 instances in kosha

All in this random sample checked.

NOTE: Typo in schmit upatApant -> upata/pant L=8531

-----------------------------------
Random checks between mw , the pdf and index

python generate_random.py 5 mw temp_mw.txt index.txt check_mw.txt

regex_raw = <ls>TBr. ([i]+), *([0-9]+), *([0-9]+), *([0-9]+)
found 124 instances in kosha

All in this random sample checked.

- One uncertain:
key (2, 2, 9, 7): I	212	2	2	9	5	8a	205
L= 80806, hw= jyotsnA, pc=427,3
check: ok ? found jotsnA -- typo in pdf?

 

