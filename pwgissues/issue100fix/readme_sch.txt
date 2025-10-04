
issue100fix

sch link forms:
<ls>RAGH. ([0-9]+),([0-9]+)

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt

(None,5),(True,55),(all,60) lsfix2_sch_0.txt

cp temp_sch_0.txt temp_sch_1.txt

Edit temp_sch_1.txt based on the None cases


----------------------------------
python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
(None,3),(True,59),(all,62) lsfix2_sch_1.txt
  The 3 are:
   2 are Ragh. ed. Calc. links
   1 is harivikrama : <ls>Ragh. XIX,25</ls>  ref. 'Mallin.' no link.

2 additional links
--------------------
# generate temp_sch_2.txt from temp_sch_0.txt and the 'fixed' elements

# python dict_replace2.py temp_sch_0.txt lsfix2_sch_0.txt temp_sch_2.txt
# No 'fixed' to expand.

-----------------------------------------------------------
# remake xml from temp_sch_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix
cp temp_sch_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue100fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

# python lsfix2.py sch temp_sch_1.txt lsfix2_sch_2.txt
Already done

(- 293 274)  19 additional standard links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_2.txt change_sch_2.txt
7 changes written to change_sch_2.txt

