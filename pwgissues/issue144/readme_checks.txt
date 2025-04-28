
Manual check for pwg before basicadjust updated.


python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg_man.txt
regex_raw = <ls>TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 2599 instances in kosha

===================================================
Checks for all dictionaries after basicadjust updated.


----------------------------------------------------
First, pwg

python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg_man.txt

regex_raw = <ls>TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 4369 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between pw , the pdf and index

python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt

regex_raw = <ls>TS. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 541 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between pwkvn , the pdf and index

python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt
regex_raw = <ls>TS. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 144 instances in kosha

All in this random sample checked.


-----------------------------------
Random checks between sch , the pdf and index

python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt
regex_raw = <ls>TS. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)
found 139 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between mw , the pdf and index

python generate_random.py 5 mw temp_mw.txt index.txt check_mw.txt
regex_raw = <ls>TS. ([ivx]+), *([0-9]+), *([0-9]+), *([0-9]+)
found 204 instances in kosha

All but 1 in this random sample checked.
key (2, 4, 8, 1): I	206	II	4	8	1	2	191
L= 62958, hw= gaDA, pc=344,3
 NOT FOUND
 

