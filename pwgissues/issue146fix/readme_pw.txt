
issue146fix

pw link forms:
<ls>KUMĀRAS. ([0-9]+),([0-9]+)

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt

130 lines written to lsfix2_pw_0.txt
(True, 2) 121
('fixed', 2) 5
(None, 2) 4


cp temp_pw_0.txt temp_pw_1.txt

Edit temp_pw_1.txt to resolve the None and False

97800 : Sabda : KUMĀRAS. 1,1,46. : KUMĀRAS. 1,46. : print change
59121 : niruYCana : KUMĀRAS. 13,18,22 : KUMĀRAS. (1868) 13,18. 22 : print change

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt

129 lines written to lsfix2_pw_1.txt
(True, 2) 121
('fixed', 2) 5
(None, 2) 3

The 3 'None' items are "KUMĀRAS. (1868) ... ", another edition.
Maybe: https://archive.org/details/in.ernet.dli.2015.513902/page/n5/mode/2up
  (pub. date 1871)



--------------------
# generate temp_pw_2.txt from temp_pw_0.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
129 lines read from lsfix2_pw_1.txt
5 lines to change
apply_repls: 5 lines changed
6

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue146fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt

134 lines written to lsfix2_pw_2.txt
(True, 2) 131
(None, 2) 3
 (- 131 121) == 10  additional standard links

---------------------------------------------------
First parm should be 1-7 in our (1838) edition.
But 33 exceptions probably refer to unknown 1868 edition.

27 matches for "<ls>KUMĀRAS. [0-9][0-9]," in buffer: lsfix2_pw_2.txt
1 match for "<ls n="KUMĀRAS.">[0-9][0-9]," in buffer: lsfix2_pw_2.txt
2 match for "<ls n="KUMĀRAS. [0-9][0-9],">" in buffer: lsfix2_pw_2.txt
3 matches for "[89]," in buffer: lsfix2_pw_2.txt

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
2 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
5 changes written to change_pw_2.txt

