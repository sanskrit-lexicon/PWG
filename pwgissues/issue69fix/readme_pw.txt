
issue69fix

pw link forms:
Verz. d. Oxf. H. ([0-9]+)

python lsfix2_alt.py 14 pw temp_pw_0.txt lsfix2_pw_0.txt 
(None,5),(True,155),(fixed,6),(all,166) 14 lsfix2_pw_0.txt

cp temp_pw_0.txt temp_pw_1.txt

edit temp_pw_1.txt to resolve the None

46941 : tEtiri : Verz. d. Oxf. H. 55,3 : Verz. d. B. H. 55,3 : cf. pwg tEttiri : print change
131712 : smAram : Verz. d. Oxf. H. 161,2. v. u. : Verz. d. Oxf. H. 161,b,2. v. u. : print change

-------
Cannot find haRqaka or kaRqikA at
 https://sanskrit-lexicon-scans.github.io/Oxf_Cat_Aufrecht/index.html?153

------------
python lsfix2_alt.py 14 pw temp_pw_1.txt lsfix2_pw_1.txt 
(None,1),(True,158),(fixed,6),(all,165) 14 lsfix2_pw_1.txt

------------
# expand the 'fixed'
python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
apply_repls: 6 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2_alt.py 14 pwg temp_pw_2.txt lsfix2_pw_2.txt
(None,1),(True,172),(all,173) 14 lsfix2_pw_2.txt

compare to initial lsfix2_pw_0.txt

(- 172 155) = 16 additional standard links.

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
4 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
6 changes written to change_pw_2.txt

====================================================
