
10-05-2025 begin ejf
 Andhrabharati submits  Oxf.H.links.to.rework.txt (184 items)
 for further possible revision.
 This pertains to pwg kosha.
 

sanskrit-lexicon-scans/

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issue69fixa
this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fixa

-------------------------------------
# get temporary local copy of pwg kosha
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

We will edit temp_pwg_1.txt
cp temp_pwg_0.txt temp_pwg_1.txt

examine AB's rework file
--------------------------------------
First subgroup: Reference starts with No\.

15 "<ls>Verz. d. Oxf. H. No."
 7 "<ls n="Verz. d. Oxf. H.">No."

All remaining 37 'No.' are after [ab],
 i.e. 37 matches in 28 lines for "[ab], No\."
--------------------------------------
91 "<ls>Verz. d. Oxf. H. [0-9]+,[ab],"
66 "<ls n="Verz. d. Oxf. H.">[0-9]+,[ab],"
 2 misc similar:
   <ls n="Verz. d. Oxf. H. 294,">b,12. 25. 27. 35. 47.</ls>
   <ls n="Verz. d. Oxf. H. 66,a,">29. fg. 39.</ls>

----
 3 remaining 
-----
old: <ls n="Verz. d. Oxf. H.">23. fg. 26.</ls>
   k1 = tulasI
   References found: 23,a,3 v.u.; 26,b,2
new: <ls n="Verz. d. Oxf. H.">23. fg.</ls> <ls n="Verz. d. Oxf. H.">26.</ls>

-----
old: <ls n="Verz. d. Oxf. H.">392 (No. 68. 69.)</ls>
   k1 = bfhadAraRyaka
   reference occurs on page 392, in section labeled 68, 69.
new: No change 

-----
old: <ls>Verz. d. Oxf. 11. 128,b,16.</ls>
   k1 = virasa
   The '11.' is typo (poor print)
new: <ls>Verz. d. Oxf. H. 128,b,16.</ls>  
-------------------------------------------------
Examined all 159 remaining excluding
  the 22 "H. No.'
  the 3 'remaining'
Here are questionable ones
-----
old: <ls>Verz. d. Oxf. H. 56,a,10. 12. 378.</ls>
   k1 = AraRyaka  The 378 is page number.
   Word AraRyaka appears in section 380 of this page 378!
new: <ls>Verz. d. Oxf. H. 56,a,10. 12.</ls> <ls n="Verz. d. Oxf. H.">378.</ls>
-----
old: <ls n="Verz. d. Oxf. H. 294,">b,12. 25. 27. 35. 47.</ls>
  Page should be 284
new: <ls n="Verz. d. Oxf. H. 284,">b,12. 25. 27. 35. 47.</ls>
-----
old: <ls n="Verz. d. Oxf. H.">210,b, No. 496, Z. 6. 14.</ls>
  k1 = vANmaya
  No. 496 -> No. 497
new: <ls n="Verz. d. Oxf. H.">210,b, No. 497, Z. 6. 14.</ls>

89436 : vANmaya : 210,b, No. 497, Z. 6. 14. : 210,b, No. 496, Z. 6. 14. : print change

-----
old: <ls n="Verz. d. Oxf. H.">22,b,27. 29. fg. 3</ls>
old: <ls n="Verz. d. Oxf. H.">9,b,6.</ls>

new: <ls n="Verz. d. Oxf. H.">22,b,27. 29. fg.</ls>
new: <ls n="Verz. d. Oxf. H.">39,b,6.</ls>

-----
old: <ls n="Verz. d. Oxf. H.">283,a, No. 661. b, No. 62.</ls>
typo
new: <ls n="Verz. d. Oxf. H.">283,a, No. 661. b, No. 662.</ls>
===================

python lsfix2_alt.py 14 pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(None,9),(True,17941),(all,17950) 14 lsfix2_pwg_1.txt

compare to ../issue69fix/lsfix2_pwg_2.txt
(None,9),(True,17938),(all,17947) 14 lsfix2_pwg_2.txt

------------------------------------------
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
8 changes written to change_pwg_1.txt

-----------------------------------------------------------
# remake xml from temp_pwg_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fixa
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fixa

================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fixa
diff temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue69fixa  splitting 'Verz. d. Oxf. H.' refs rework
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fixa

------------------------
# csl-corrections
cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "issue69fixa  splitting 'Verz. d. Oxf. H.' rework
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fixa

---------------------------------------------------
# sync to Cologne, pull changed repos, redo displays for
pwg, pw

---------------
csl-orig #pull
# csl-websanlexicon #pull
# csl-apidev #pull
csl-corrections #pull
# csl-pywork # pull

---------------
# update displays 
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------------------------------------------
# sync issue69fixa to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue69fixa
git pull
git add .
git commit -m "issue69fixa 'Verz. d. Oxf. H.' link splitting
Ref: https://github.com/sanskrit-lexicon/pwg/issues/160"
git push

------------------------------------------------------------
THE END
