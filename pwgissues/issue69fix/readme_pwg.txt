
issue69fix

pwg link forms:
Verz. d. Oxf. H. ([0-9]+)


cp temp_pwg_0.txt temp_pwg_1.txt

python lsfix2_alt.py 01 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_01.txt 
(None,5999),(True,8087),(fixed,783),(all,14869) 01 fixwork/lsfix2_pwg_1_01.txt

python lsfix2_alt.py 02 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_02.txt 
(None,5733),(True,8325),(fixed,811),(all,14869) 02 fixwork/lsfix2_pwg_1_02.txt

python lsfix2_alt.py 03 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_03.txt 
(None,5528),(True,8529),(fixed,812),(all,14869) 03 fixwork/lsfix2_pwg_1_03.txt

python lsfix2_alt.py 04 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_04.txt 
(None,4972),(True,9014),(fixed,883),(all,14869) 04 fixwork/lsfix2_pwg_1_04.txt

python lsfix2_alt.py 05 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_05.txt 
(None,4436),(True,9423),(fixed,1010),(all,14869) 05 fixwork/lsfix2_pwg_1_05.txt

python lsfix2_alt.py 05 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_05.txt 
(None,4436),(True,9423),(fixed,1010),(all,14869) 05 fixwork/lsfix2_pwg_1_05.txt

python lsfix2_alt.py 06 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_06.txt 
(None,3466),(True,10286),(fixed,1117),(all,14869) 06 fixwork/lsfix2_pwg_1_06.txt

python lsfix2_alt.py 07 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_07.txt 
(None,3321),(True,10384),(fixed,1164),(all,14869) 07 fixwork/lsfix2_pwg_1_07.txt

python lsfix2_alt.py 08 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_08.txt 
(None,2870),(True,10753),(fixed,1246),(all,14869) 08 fixwork/lsfix2_pwg_1_08.txt

python lsfix2_alt.py 09 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_09.txt 
(None,781),(True,12396),(fixed,1692),(all,14869) 09 fixwork/lsfix2_pwg_1_09.txt

python lsfix2_alt.py 10 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_10.txt 
(None,531),(True,12499),(fixed,1839),(all,14869) 10 fixwork/lsfix2_pwg_1_10.txt

python lsfix2_alt.py 11 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_11.txt 
(None,382),(True,12748),(fixed,1739),(all,14869) 11 fixwork/lsfix2_pwg_1_11.txt

python lsfix2_alt.py 12 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_12.txt
(None,124),(True,12971),(fixed,1784),(all,14879) 12 fixwork/lsfix2_pwg_1_12.txt

python lsfix2_alt.py 13 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_13.txt
(None,105),(True,12984),(fixed,1790),(all,14879) 13 fixwork/lsfix2_pwg_1_13.txt

python lsfix2_alt.py 14 pwg temp_pwg_1.txt fixwork/lsfix2_pwg_1_14.txt
(None,9),(True,13068),(fixed,1796),(all,14873) 14 fixwork/lsfix2_pwg_1_14.txt

# fixwork/lsfix2_pwg_1_14.txt is the one finally used.
# copy it to main directory
cp fixwork/lsfix2_pwg_1_14.txt lsfix2_pwg_1.txt

</ls> <ls n="Verz. d. Oxf. H.">

python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
apply_repls: 1765 lines changed

print changes

46055 : purAvftta : Verz. d. Oxf. H. 54,28. : Verz. d. Oxf. H. 54,a,28. : print change
43174 : pariSIlana : Verz. d. Oxf. H. 173,4 v. u. : Verz. d. Oxf. H. 173,b,4 v. u. : print change
51759 : banDana : Verz. d. Oxf. H. 321,3 v. u. : Verz. d. Oxf. H. 321,b,3  v. u. : print change
53444 : brahmamImAMsA : 622 (246,b) : 246,b,2. v. u. : print change
93582 : viSvarUpa : 227,13. : 227,b,13. : reference to Verz. d. Oxf. H. : print change
104317 : sadAnandamaya : 192,2 v. u. : 192,b,2 v. u. : print change
62487 : akrama : Verz. d. Oxf. H. 232,11. 16. : Verz. d. Oxf. H. 232,a,11. 16. : print change
82477 : yogANga : Verz. d. Oxf. H. 233,2. fgg. : Verz. d. Oxf. H. 233,b,2. fgg. : print change
94545 : vIravarapratApa : Verz. d. Oxf. H. 181,9.: Verz. d. Oxf. H. 181,b,9. : print change
106434 : saraRi : Verz. d. Oxf. H. 170,5 : Verz. d. Oxf. H. 170,b,5 : print change
112918 : somayAjin : Verz. d. Oxf. H. 219,7. 8. : Verz. d. Oxf. H. 219,b,7. 8. : print change
85667 : lakzmI : Verz. d. Oxf. H. 97,a, No. 151,1 v. u. : Verz. d. Oxf. H. 97,a,,1 No. 151 v. u. : print change
103508 : saMkrama : {#SuBavikrama#} 49,35 : {#SuBavikrama#} 49,b,35 : print change
113280 : sOra : {#sparSAH#} 104,34. : {#sparSAH#} 104,b,34. : print change
92581 : vimalanATapurARa : Verz. d. Oxf. H. 372. 6, No. 267. : Verz. d. Oxf. H. 372,b, No. 267.

bad print: 
https://www.sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpdf/pwg1-0011.pdf


=====================
cannot find turazka at https://sanskrit-lexicon-scans.github.io/Oxf_Cat_Aufrecht/index.html?30

The forms are not purely numerical.
Standard forms are
7546  <ls>Verz. d. Oxf. H. [0-9]+,[ab],[0-9]+\.?</ls>
1277  <ls n="Verz. d. Oxf. H.">[0-9]+,[ab],[0-9]+\.?</ls>
cp temp_pwg_0.txt temp_pwg_1.txt

Edit temp_pwg_1.txt to resolve the None and False

--------------

-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fix
-- end of 'remake xml ...'

-------------------------------------------------------------
Create Some documentation files

python lsfix2_alt.py 14 pwg temp_pwg_2.txt lsfix2_pwg_2.txt
17947 lines written to lsfix2_pwg_2.txt
(None,9),(True,17938),(all,17947) 14 lsfix2_pwg_2.txt

compare to initial fixwork/lsfix2_pwg_1_01.txt
(None,5999),(True,8087),(fixed,783),(all,14869) 01 fixwork/lsfix2_pwg_1_01.txt


(- 17938  8087) 9851 additional "standard" links

---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
933 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
1765 lines  changed and written to change_pwg_2.txt

====================================================
