
issue84fix

sch link forms:
Śat. Br. 4 parms

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt
(False,1),(None,6),(True,98),(fixed,5),(all,110) lsfix2_sch_0.txt

cp temp_sch_0.txt temp_sch_1.txt
# edit temp_sch_1.txt for manual changes
</ls>; <ls n="Śat. Br.">
</ls> <ls n="Śat. Br.">

Note later print chg at aRupriyaNgu

python lsfix2.py sch temp_sch_1.txt lsfix2_sch_1.txt
(True,118),(fixed,5),(all,123) lsfix2_sch_1.txt

No None, False remain

--------------------
# generate temp_sch_2.txt from temp_sch_1.txt and the 'fixed' elements

python dict_replace2.py temp_sch_1.txt lsfix2_sch_1.txt temp_sch_2.txt
apply_repls: 5 lines changed

-----------------------------------------------------------
# remake xml from temp_sch_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix
cp temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh sch  ../../sch
sh xmlchk_xampp.sh sch
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue84fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py sch temp_sch_2.txt lsfix2_sch_2.txt
(True,129),(all,129) lsfix2_sch_2.txt

Additional links: (- 129 98) 31 additional links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_sch_0.txt temp_sch_1.txt change_sch_1.txt
8 changes written to change_sch_1.txt

python diff_to_changes_dict.py temp_sch_1.txt temp_sch_2.txt change_sch_2.txt
5 changes written to change_sch_2.txt

===========================================
 Find some invalid references

python lsfix3.py sch temp_sch_2.txt lsfix3_sch_2.txt
(True,129),(all,129) lsfix3_sch_2.txt
example output line:
32      aMSu    <ls n="Śat. Br. 4,">6,1,1</ls>  4,6,1,1


python chkidx.py lsfix3_sch_2.txt SAT.index_edit.txt lsfix3_chkidx_sch_2.txt
129 instances find ipage out of 129
 1 problematic

None    2823    aRupriyaNgu     <ls>Śat. Br. 14,9,3,32.</ls>    14,9,3,32
From pw,  14,9,3,22    Make a print chg  in temp_pwg_1.txt 
905 : aRupriyaNgu : Śat. Br. 14,9,3,32. : Śat. Br. 14,9,3,32. : cf. PW(K) : print change

rerun intermediate steps, then check again
129 instances find ipage out of 129
0 problematic

python chkidx.py lsfix3_sch_2.txt SAT.index_edit.txt lsfix3_chkidx_sch_2.txt
