
issue100fix

pw link forms:
<ls>RAGH. ([0-9]+),([0-9]+)

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt
(False,1),(True,274),(fixed,7),(all,282) lsfix2_pw_0.txt


False: AtmavittA  : RAGH. 8,10 (ed. Bomb.)  Link works properly

----------------------------------
# python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
no changes to pw_0
--------------------
# generate temp_pw_2.txt from temp_pw_0.txt and the 'fixed' elements

python dict_replace2.py temp_pw_0.txt lsfix2_pw_0.txt temp_pw_2.txt
apply_repls: 7 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pw_2.txt lsfix2_pw_2.txt
(False,1),(True,293),(all,294) lsfix2_pw_2.txt

(- 293 274)  19 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_2.txt change_pw_2.txt
7 changes written to change_pw_2.txt

