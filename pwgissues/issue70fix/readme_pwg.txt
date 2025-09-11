
issue70fix

pwg link forms:
<ls>KATHĀS. ([0-9]+),([0-9]+)

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

25004 lines written to lsfix2_pwg_0.txt
(True, 2) 24994
(None, 2) 8
('fixed', 2) 2

----------------------------------
No immediate fixes seen for the 8 'None' cases.
One example:
3450 : andolana : KATHĀS. S. 96. : internal page 96 = pdf
   https://sanskrit-lexicon-scans.github.io/kss/pdfpages/1117.pdf
   

# generate temp_pwg_2.txt from temp_pwg_0.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_0.txt lsfix2_pwg_0.txt temp_pwg_2.txt

25004 lines read from lsfix2_pwg_0.txt
2 lines to change
apply_repls: 2 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue70fix
-- end of 'remake xml ...'


-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt

25007 lines written to lsfix2_pwg_2.txt
(True, 2) 24999
(None, 2) 8


---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_2.txt change_pwg_2.txt
2 changes written to change_pwg_2.txt
