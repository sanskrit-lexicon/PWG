
issue124fix

cp temp_pw_0.txt temp_pw_1.txt

---------------------------------------------
# VS. corresponds to linktarget
pw VS. ([0-9]+),([0-9]+),

Other refs starting with 'VS.' (these excluded in further analysis)
32 matches for "VS. PRĀT."

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt
(None,7),(True,145),(fixed,5),(all,157) lsfix2_pw_0.txt

cp temp_pw_0.txt temp_pw_1.txt
# edit changes to temp_pw_1.txt

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
(None,2),(True,156),(fixed,5),(all,163) lsfix2_pw_1.txt

None: 
473386	Sukriya	<ls>VS. 36</ls>	
473386	Sukriya	<ls n="VS.">40</ls>	

---------------------------
MISC COMMENTS

END MISC COMMENTS

--------------------------------

# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
apply_repls: 5 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue124fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt
(None,2),(True,167),(all,169) lsfix2_pw_2.txt

Additional links: (- 167 145) 22
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
8 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
5 changes written to change_pw_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pw temp_pw_2.txt lsfix3_pw_2.txt
(True,167),(all,167) lsfix3_pw_2.txt

example output line:
38891   avatAna <ls n="VS. 16,">63</ls> 16,63

cp ../issue124/index.txt  index.txt

# modify chkidx.py (Pagerec) for this kosha

python chkidx.py lsfix3_pw_2.txt index.txt lsfix3_chkidx_pw_2.txt
167 instances find ipage out of 167
0 references NOT FOUND in index

119709 : sabva<k2> : VS. 10,84 : VS. 19,84 : cf. pwg : print change

