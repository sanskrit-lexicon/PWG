
issue124fix

cp temp_pwg_0.txt temp_pwg_1.txt

---------------------------------------------
# VS. corresponds to linktarget
pwg VS. ([0-9]+),([0-9]+),

Other refs starting with 'VS.' (these excluded in further analysis)
1048 matches for "VS. PRĀT."
   2 matches for "VS. ANUKR."

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt
(False,34),(None,187),(True,5375),(fixed,411),(all,6007) lsfix2_pwg_0.txt

cp temp_pwg_0.txt temp_pwg_1.txt
# edit changes to temp_pwg_1.txt

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(None,62),(True,5478),(fixed,436),(all,5976) lsfix2_pwg_1.txt

26483 : jan : (ṚV.) 10,41,4 : (ṚV.) 10,31,4 : print change
26483 : jan : (ṚV.) 8,91,7 : (ṚV.) 8,102,7 : print change

---------------------------
MISC COMMENTS

END MISC COMMENTS

--------------------------------

# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
apply_repls: 436 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt
(None,62),(True,6732),(all,6794) lsfix2_pwg_2.txt

Additional links: (- 6732 5375) 1357
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
189 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
436 changes written to change_pwg_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pwg temp_pwg_2.txt lsfix3_pwg_2.txt
(True,6732),(all,6732) lsfix3_pwg_2.txt

example output line:
860     akAya   <ls>VS. 40,8</ls>       40,8

cp ../issue124/index.txt  index.txt

# modify chkidx.py (Pagerec) for this kosha

python chkidx.py lsfix3_pwg_2.txt index.txt lsfix3_chkidx_pwg_2.txt
6696 instances find ipage out of 6732
36 references NOT FOUND in index

examine the None instances in lsfix3_chkidx_pwg_2.txt

Noticed an error in index:  18,27, 18,28
cp index.txt index_orig.txt
Adjust index.txt and rerun

python chkidx.py lsfix3_pwg_2.txt index.txt lsfix3_chkidx_pwg_2.txt
6713 instances find ipage out of 6732
19 references NOT FOUND in index

38533 : nArASaMsa : VS. 5,53 : VS. 3,53 : print change

98643 : SAkvara : VS. 10,14. 13,85. 15,14. : VS. 10,14. 13,58. 15,14. : print change

Change temp_pwg_1.txt as possible and rerun
