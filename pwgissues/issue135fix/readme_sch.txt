
issue135fix

sch link forms:
2 parameters.

73  "Rājat."   

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt

(None,4),(True,68),(fixed,1),(all,73) lsfix2_sch_0.txt


cp temp_sch_0.txt temp_sch_1.txt

Make changes to temp_sch_1 to correct  None
 
python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
(True,77),(fixed,1),(all,78) lsfix2_sch_1.txt

To correct the 'fixed' item, number of lines will change (2 new headwords)

cp temp_sch_1.txt temp_sch_1a.txt

python lsfix2.py sch temp_sch_1a.txt lsfix2_sch_1a.txt
(True,78),(all,78) lsfix2_sch_1a.txt

(- 78 68) 10  additional links
-----------------------------------------------------------
# remake xml from temp_sch_1a.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135fix
cp temp_sch_1a.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135fix
-- end of 'remake xml ...'

---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
4 changes written to change_sch_1.txt

# python diff_to_changes_dict.py temp_sch_1.txt temp_sch_1a.txt change_sch_1a.txt
diff temp_sch_1.txt temp_sch_1a.txt > changediff_sch_1a.txt 
32 changes written to change_sch_2.txt
