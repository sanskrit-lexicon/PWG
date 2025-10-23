
issue101fix

pwg link forms:
 1 or 2 parameters

  "SĀH. D."
  
</ls> <ls n="SĀH. D.">

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt
(False,91),(None,22),(True,1059),(True,2230),(fixed,203),(fixed,233),(all,3838) lsfix2_pwg_0.txt

Total True: (+ 1059 2230) = 3289

cp temp_pwg_0.txt temp_pwg_1.txt

Make changes to temp_pwg_1 and 2 to correct False and None

"<ls>SĀH.</ls> <ls>D."  -> "<ls>SĀH. D."  (10)

11 references to an 1828 edition
  10 matches for "<ls>SĀH. D. [^<]*1828"
  1 match for "<ls n="SĀH. D.[^<]*1828" 

61706 : mfdu : SĀH. D. p. 65 : SĀH. D. 65,14 : print change

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(True,1131),(True,2320),(fixed,227),(fixed,264),(all,3942) lsfix2_pwg_1.txt

--------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements
python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt

apply_repls: 480 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue101fix
-- end of 'remake xml ...'

---------------------------------------------------
---- lsfix2 file with pwg_2

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt

(True,1720),(True,2899),(all,4619) lsfix2_pwg_2.txt

Total True: (+ 1720 2899) 4619

(- 4619 3289) 1330  additional links


---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
123 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
480 changes written to change_pwg_2.txt

==============================================================
THE END
