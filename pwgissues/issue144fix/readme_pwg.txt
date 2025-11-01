
issue144fix

pwg link forms:

TAITTIRĪYA  # no parms

@ pwga TAITT. BR.
#  this refers to some other edition.
# does not refer to cdsl link target
python lsfix2.py pwga temp_pwg_0.txt lsfix2_pwga_0.txt
(None,2),(True,62),(fixed,4),(all,68) lsfix2_pwga_0.txt

cp temp_pwg_0.txt temp_pwg_1.txt

edit temp_pwg_1.txt;
  fix 1 of the None
  Apply the 4 'fixed'

python lsfix2.py pwga temp_pwg_1.txt lsfix2_pwga_1.txt
(None,1),(True,70),(all,71) lsfix2_pwga_1.txt

The 1 None:  hiraRyakaSipu	<ls>TAITT. BR. 1,237,16.</ls>

---------------------------------------------
# TBR. corresponds to linktarget
@ pwg TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)  
python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt
(False,6),(None,237),(True,2289),(fixed,357),(all,2889) lsfix2_pwg_0.txt


python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(None,133),(True,2378),(fixed,372),(all,2883) lsfix2_pwg_1.txt

None info:
74 matches for "TBR. Comm."  added to pwgbib_input.txt in pywork.
14 matches for "<ls>TBR. [0-9]+,[0-9]+\.?</ls>"
16 matches for "TBR..*?[I]"
20 matches for "<ls>TBR. [0-9]+,[0-9]+,[0-9]+\.?</ls>"
 3 matches for "<ls n="TBR.">[0-9]+,[0-9]+,[0-9]+\.?</ls>"
 6 misc:
308177	daRqapAta	<ls>TBR. S. 120, N.</ls>	
426075	paryudAsa	<ls>TBR. 184.</ls>	
988077	saMmArga	<ls>TBR. 3,497,14. 500,1.</ls>	
997762	sava	<ls>TBR. 2</ls>	
997762	sava	<ls n="TBR.">2,750. fgg.</ls>	
1040943	sUnfta	<ls>TBR. v. l.</ls>	

---------------------------
MISC COMMENTS
  Many of the 133 None are associated with a commentary
END MISC COMMENTS

--------------------------------

# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
apply_repls: 372 lines changed

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt
(None,133),(True,3210),(all,3343) lsfix2_pwg_2.txt

Additional links: (- 3210 2289)  921
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
127 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
372 changes written to change_pwg_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pwg temp_pwg_2.txt lsfix3_pwg_2.txt
(True,3210),(all,3210) lsfix3_pwg_2.txt

example output line:
191643  kzuD    <ls n="TBR. 2,2,">11,5.</ls>    2,2,11,5

cp ../issue144/index.txt  index.txt
index1.txt  # revise by removing first field (volume)
  Note: kanda 1,2  from volume I (ipage 1-361)
        kanda 3 from volume III (ipage 1-293)
 
python chkidx.py lsfix3_pwg_2.txt index1.txt lsfix3_chkidx_pwg_2.txt
3163 instances find ipage out of 3210
 (- 3210 3163)  47 references NOT FOUND in index

