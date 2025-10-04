
issue100fix

pwg link forms:
<ls>RAGH. ([0-9]+),([0-9]+)

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt
(False,3),(None,18),(True,9695),(all,9716) lsfix2_pwg_0.txt

cp temp_pwg_0.txt temp_pwg_1.txt

Edit temp_pwg_1.txt to resolve the None and False

113928 : sTA : RAGH. 12,12,49 : RAGH. 12,49 : print change

----------------------------------
python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(None,15),(True,9702),(all,9717) lsfix2_pwg_1.txt

Explanation of None:
12 references with 1 parameter.
  Note all followed by 'in der Unterschr.' What does the meaning?
The remain 3 None are 'ok'.

Revise pwgbib_input.txt in csl-pywork (for "RAGH. ed. ST.")
Revise csl-websanlexicon (basicadjust)
Revise csl-apidev basicadjust)

--------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements
# Nothing to fix.
# python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt

-----------------------------------------------------------
# remake xml from temp_pwg_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix
-- end of 'remake xml ...'

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
7 changes written to change_pwg_1.txt
