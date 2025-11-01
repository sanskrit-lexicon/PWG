
issue144fix

pw link forms:

TAITTIRĪYA  # no parms

@ pwa TAITT. BR.
#  1 instance in pw. 
  anuvatsarIRa <ls>TAITT. BR. 1,4,10,3</ls>.
# This DOES refer to cdsl linktarget 
python lsfix2.py pwa temp_pw_0.txt lsfix2_pwa_0.txt
(True,1),(all,1) lsfix2_pwa_0.txt

In contrast to pwg,  this TAITT. BR. references DOES resolve in
  our link target.
  
---------------------------------------------
# TBR. corresponds to linktarget
pw TBR. ([0-9]+),([0-9]+),([0-9]+),([0-9]+)  
python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt
(None,17),(True,250),(fixed,19),(all,286) lsfix2_pw_0.txt

cp temp_pw_0.txt temp_pw_1.txt
correct a few

python lsfix2.py pw temp_pw_1.txt lsfix2_pw_1.txt
(None,9),(True,259),(fixed,20),(all,287) lsfix2_pw_1.txt

None info:
7 matches for "<ls>TBR. <ab>Comm.</ab>"
1 misc:
  438664	viSvaprI	<ls>TBR. 3,11,5</ls>	

---------------------------

# generate temp_pw_2.txt from temp_pw_1.txt and the 'fixed' elements

python dict_replace2.py temp_pw_1.txt lsfix2_pw_1.txt temp_pw_2.txt
apply_repls: 20 lines changed

-----------------------------------------------------------
# remake xml from temp_pw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
cp temp_pw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pw  ../../pw
sh xmlchk_xampp.sh pw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue144fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2.py pw temp_pw_2.txt lsfix2_pw_2.txt
(None,8),(True,299),(all,307) lsfix2_pw_2.txt

Additional links: (- 299 250) 49
---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pw_0.txt temp_pw_1.txt change_pw_1.txt
12 changes written to change_pw_1.txt

python diff_to_changes_dict.py temp_pw_1.txt temp_pw_2.txt change_pw_2.txt
20 changes written to change_pw_2.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py pw temp_pw_2.txt lsfix3_pw_2.txt
(True,299),(all,299) lsfix3_pw_2.txt
example output line:
3700    aNgahoma        <ls>TBR. 3,8,17,4</ls>  3,8,17,4

# cp ../issue144/index.txt  index.txt
# index1.txt  # revise by removing first field (volume)
  Note: kanda 1,2  from volume I (ipage 1-361)
        kanda 3 from volume III (ipage 1-293)
 
python chkidx.py lsfix3_pw_2.txt index1.txt lsfix3_chkidx_pw_2.txt
297 instances find ipage out of 299
 (- 299 297)  2 references NOT FOUND in index

