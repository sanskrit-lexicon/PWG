

# preliminary check of temp_pwg.txt and index and pdf

ok <L>20<pc>1-0004<k1>aMSu  <ls>VS. 5,7.</ls>
232	5	6	7	130
ok <L>18306<pc>2-0370<k1>kuzWa <ls>VS. 25,6</ls>
853	25	5	6a	751
854	25	6b	7	752
ok <L>34826<pc>3-0766<k1>deSa <ls>VS. 34,11.</ls>
1010	34	10	12	908
ok <L>34990<pc>3-0776<k1>dEvya <ls>VS. 17,54.</ls>
641	17	54	55	539
ok <L>745<pc>1-0056<k1>aNgirasvant <ls>VS. 38,9.</ls>
1063	38	8	9	961
ok <L>12956<pc>1-1043<k1>fju <ls>VS. 37,10.</ls>   fjave
1050	37	10	11a	948
ok <L>9045<pc>1-0677<k1>AyAsa <ls>VS. 39,11.</ls> 
1079	39	10b	13	977
ok <L>2653<pc>1-0192<k1>anila <ls>VS. 40,15.</ls>
1088	40	12	15	986

ok <L>35101<pc>3-0785<k1>dOrvratya <ls>VS. 39,9.</ls>
1078	39	9	10a	976
ok <L>3224<pc>1-0236<k1>antaHparSavya <ls>VS. 39,8.</ls>
1077	39	8	8	975

=====================================================
Checks for all dictionaries after basicadjust updated.

----------------------------------------------------
First, pwg

python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg.txt
regex_raw = <ls>VS. ([0-9]+),([0-9]+)
found 4890 instances in kosha

3 found, 2 NOT FOUND.

#  generate another batch
python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg_a.txt

All in this random sample checked.


-----------------------------------
Random checks between pw , the pdf and index

python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt

regex_raw = <ls>VS. ([0-9]+),([0-9]+)
found 155 instances in kosha
All in this random sample checked.

-----------------------------------
Random checks between pwkvn , the pdf and index

python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt
regex_raw = <ls>VS. ([0-9]+),([0-9]+)
found 11 instances in kosha
All in this random sample checked.


-----------------------------------
Random checks between sch , the pdf and index

python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt
regex_raw = <ls>VS. ([0-9]+),([0-9]+)
found 11 instances in kosha
All in this random sample checked.


-----------------------------------
Random checks between mw , the pdf and index

python generate_random.py 5 mw temp_mw.txt index.txt check_mw.txt
regex_raw = <ls>VS. ([vix]+), *([0-9]+)
found 643 instances in kosha

All in this random sample checked.
  Note: See indumat comment -- probably ok 
