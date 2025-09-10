
pwg link forms:
<ls>KĀTY. ŚR. ([0-9]+),([0-9]+),([0-9]+)

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

6731 lines written to lsfix2_pwg_0.txt
(True, 3) 5361
('fixed', 3) 775
(None, 3) 121
(False, 3) 24
('fixed', 2) 145
(True, 2) 305


240 matches for "<ls>KĀTY. ŚR. [0-9]+,[0-9]+\.?</ls>
These may be references of form (ipage,linenum) We have no such app!
Examples:
maRika KĀTY. ŚR. 728,2.  ok
tArtIya <ls>KĀTY. ŚR. 357,12.</ls> ok
vakala KĀTY. ŚR. 305,7.  ok find 'vakula'  Schol. on
sapaSuka KĀTY. ŚR. 549,17  ok
varDApana Schol. zu <ls>KĀTY. ŚR. 358, N.</ls>

----------------------------------
Resolve the None and False (145) by edits to temp_pwg_1.txt
cp temp_pwg_0.txt temp_pwg_1.txt

print changes
24861 : camasa : KĀTY. ŚR. S. 182,4. : KĀTY. ŚR. 182,4. : print change (S. = page )
25167 : cAndra : KĀTY. ŚR. S. 331,23. : KĀTY. ŚR. 331,23. : print change
30273 : tUla : KĀTY. ŚR. p. 55,17. : KĀTY. ŚR. 55,17. : print change
30682 : tolana : KĀTY. ŚR. p. 52,4. : KĀTY. ŚR. 52,4. : print change
31889 : daDIy : KĀTY. ŚR. p. 648,2 : KĀTY. ŚR. 648,2  : print change
32399 : dA : KĀTY. ŚR. p. 67,8. : KĀTY. ŚR. 67,8. : print change
32399 : dA : KĀTY. ŚR. p. 67,10. : KĀTY. ŚR. 67,10. : print change
32401 : dA : KĀTY. ŚR. p. 125,21. : KĀTY. ŚR. 125,21. : print change
36569 : DAnyaka : KĀTY. ŚR. p. 946 : KĀTY. ŚR. 946,25 : print change
82520 : yogyatA : KĀTY. ŚR. S. 22,4. : KĀTY. ŚR. 22,4. : print change
82521 : yogyatva : >KĀTY. ŚR. S. 22,9. : >KĀTY. ŚR. 22,9.
28552 : tan : KĀTY. ŚR. S. {#286#} : KĀTY. ŚR. S. 286
------------------------------------------------
# Many None and False now corrected in temp_pwg_1.txt
python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt

6756 lines written to lsfix2_pwg_1.txt
(True, 3) 5423
('fixed', 3) 817
('fixed', 2) 157
(True, 2) 322
(None, 3) 37

----------------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt

6756 lines read from lsfix2_pwg_1.txt
967 lines to change
apply_repls: 967 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue136fix
-- end of 'remake xml ...'


-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt


(True, 3) 7877
(True, 2) 732
(None, 3) 37

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
136 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
967 changes written to change_pwg_2.txt
