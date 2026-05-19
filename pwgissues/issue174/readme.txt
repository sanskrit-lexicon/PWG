
05-14-2026 begun ejf

enhance PWG markup for common abbreviations

Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issues/174


this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174

-------------------------------------
# get temporary local copy of kosha
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

# local copy of pwgab_input.txt
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgab/pwgab_input.txt pwgab_input.txt
pwgab_input.txt 54 
-------------------------------------
# Files from Andhrabharati
PWG_abbr_global.txt   787
PWG_abbr_local.txt

Ref: https://github.com/sanskrit-lexicon/PWG/issues/174#issuecomment-4462624587
-------------------------------------
xml tags
python xmltag.py temp_pwg_0.txt xmltag_pwg_0.txt
12 distinct tags written to xmltag_pwg_0.txt

-------------------------------------
# stats on <ab>X</ab>
python count_ab.py temp_pwg_0.txt count_ab_0.txt
1129105 read from temp_pwg_0.txt
59 lines written to count_ab_0.txt
1755 = total number of <ab>X</ab>

# stats on <ab n="Y">X</ab>
python count_ab_local.py temp_pwg_0.txt count_ab_local_0.txt
1129105 read from temp_pwg_0.txt
27 lines written to count_ab_local_0.txt

-------------------------------------
# temp_pwg_2.txt
# remove all 'ab' markup in pwg, for both local and global
python remove_ab.py temp_pwg_0.txt temp_pwg_1.txt
# manual changes to temp_pwg_1.txt
v.l. -> v. l.   (782)
s.u. -> s. u.   (2)
<lex>n</lex> -> <lex>n.</lex>  (1)

-------------------------------------
pwgab_input_1.txt
 cp pwgab_input.txt pwgab_input_1.txt
# manual changes
 in particular, lower case versions added for many abbreviations.
Question re 'Mpt'
-------------------------------------
temp_pwg_2.txt
python mark_ab.py temp_pwg_1.txt pwgab_input_1.txt temp_pwg_2.txt markcount_a_2.txt

86 lines read from pwgab_input_1.txt
1129105 lines read from temp_pwg_1.txt
99485 lines changed
1129105 lines written to temp_pwg_2.txt
86 lines written to markcount_a_2.txt
111590 = total number of <ab>X</ab>

-------------------------------------
pwgab_input_2.txt
  Reformatting of Andhrabharati's file PWG_abbr_global.txt
-------------------------------------
python mark_ab.py temp_pwg_1.txt pwgab_input_2.txt temp_pwg_3.txt markcount_a_3.txt

787 lines read from pwgab_input_2.txt
1129105 lines read from temp_pwg_1.txt
119390 lines changed
1129105 lines written to temp_pwg_3.txt
787 lines written to markcount_a_3.txt
143949 = total number of <ab>X</ab>


-------------------------------------
comparison of version 2 (cdsl) and version 3 (AB)
cdsl:
AB  : 

-------------------------------------
# abdiff.py  NOT USED
# python abdiff.py pwgab_input_1.txt count_ab_2.txt abdiff_cdsl_2.txt
******************************************************
NOTES FROM ANOTHER PROJECT FOLLOW
******************************************************
# Andhrabharati's solution files

=======================================================================

================================================
INSTALLATION
sync to github:

------------------
# csl-orig 
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/
diff temp_pwg_3b.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "issue84pwg  #170  pwg refs inconsistent with index"

git push
#    3d3d805..14553c5  master -> master
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/
------------------------

# csl-corrections
# use printchange_pwg_3a.txt  printchange_pwg_3b.txt to modify
# dictionaries/pwg/pwg_printchange.txt

cd /c/xampp/htdocs/cologne/csl-corrections
git pull
git add .
git commit -m "Ref: https://github.com/sanskrit-lexicon/PWG/issues/170 (issue84pwg)"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/

---------------------------------------------------
# sync to Cologne, pull changed repos, redo display
---------------
csl-orig #pull
csl-corrections #pull

---------------
# update displays for pwg
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/

-----------------------------------------------------
# sync issue174/ to github.
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174/
git pull
git add .
git commit -m "#170 issue84pwg"
git push

------------------------------------------------------------
THE END
