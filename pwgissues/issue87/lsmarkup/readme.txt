issue87/lsmarkup/readme.txt
02-12-2025 begun ejf
Indische Spruche 1st ed. link target

Ref: https://github.com/sanskrit-lexicon/PWG/issues/87

This issue87 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87/lsmarkup

----------------------
copy temp_pwg_0.txt from csl-orig at commit
9dfc1998a78962ef82cec37184024e01353351b7

---------------------
Also get local copy of pwgbib_input.txt

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt .

1 addition made to pwgbib file

----------------------
cp temp_pwg_0.txt temp_pwg_1.txt
manual changes to ls markup for Spr2parm.txt
Ref: https://github.com/sanskrit-lexicon/PWG/issues/87#issuecomment-2652340500

print changes:
81815 : yA : Spr. 1926, l. l. : Spr. 1926, v. l.
46573 : pUj : Spr. 7,2230, v. l. : Spr. 2230, v. l.

----------------------
install temp_pwg_1.txt locally

cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

# regen local displays

cd  /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87/lsmarkup

---
cp Spr_other.txt lsother_0.txt
There are some additional manual corrections in temp_pwg_1.txt
 These will change lsother_0.txt
15 instances matching ",[0-9]"
<ls>Spr. 1,467. 468.</ls> + 
<ls>Spr. I,513. fgg.</ls> +
<ls>Spr. I,453</ls> + 
<ls>Spr. I,123. fgg.</ls> +
<ls>Spr. I,123. fgg.</ls> +
<ls>Spr. I,505.</ls> + <L>38407<pc>4-0107<k1>nApita<k2>nApita
  old: s. Beitr. z. vgl. <ls>Spr. I,505.</ls>  -
  new:  s. <ls>Beitr. z. vgl. Spr. 1,505.</ls>
  New source? Add to pwgbib_input.txt: 
<ls>Spr. 2331). 116,21.</ls> +
  old: <ls>MĀRK. P. 17,12. 27,22</ls> (<ls>Spr. 2331). 116,21.</ls>
  new: <ls>MĀRK. P. 17,12. 27,22</ls> (<ls>Spr. 2331</ls>). <ls n="MĀRK. P.">116,21.</ls> 
<ls>Spr. VIII,10</ls> + new lsname: Zeitschr. f. vgl. Spr.
<ls>Spr. 1,200. 7,183.</ls> +
<ls>Spr. 70,305. 672.</ls> + typo
 new: <ls>Spr. 70.</ls> <ls n="Spr.">305.</ls> <ls n="Spr.">672.</ls>
<ls>Spr. 2053,2074. 4678.</ls> + typo
 new: <ls>Spr. 2053.</ls> <ls n="Spr.">2074.</ls> <ls n="Spr.">4678.</ls>
<ls>Spr. 5251) und 5,272.</ls> +
 old: <ls>RĀJA-TAR. 3,215</ls> (<ls>Spr. 5251) und 5,272.</ls>
 new: <ls>RĀJA-TAR. 3,215</ls> (<ls>Spr. 5251</ls>) und <ls n="RĀJA-TAR.">5,272.</ls>
<ls>Spr. 3474). 3,13983</ls> +
 old: <ls>MBH. 5,1503</ls> (<ls>Spr. 3474). 3,13983</ls>
 new: <ls>MBH. 5,1503</ls> (<ls>Spr. 3474</ls>). <ls n="MBH.">3,13983</ls>
<ls n="Spr.">217,a,10.</ls> +
 new: <ls n="Verz. d. Oxf. H.">217,a,10.</ls> 
   <L>78835<pc>5-1607<k1>pustaka
<ls>Spr. I,442.</ls>
 new: <ls>Z. f. vgl. Spr. 1,442.</ls>




old: <ls>Spr. 1445, v. l. (Th. III, S. 371).</ls>
new: <ls>Spr. 1445, v. l. (Th. III, S. 371).</ls> +

old: <ls>Spr. 1753, v. l. Th. II, S. 340</ls>
new: <ls>Spr. 1753, v. l. (Th. II, S. 340</ls> +

old: <ls>Spr. 2636, v. l. (Th. III, S. 378).</ls>
new: <ls>Spr. 2636, v. l.</ls> (Th. III, S. 378). +

old: <ls>Spr. 571. Th. 2, S. 327.</ls>
new: <ls>Spr. 571.</ls> Th. 2, S. 327. +

old: <ls>Spr. 59, v. l. (Th. 2, S. 323).</ls>
new: <ls>Spr. 59, v. l.</ls> (Th. 2, S. 323). +

old: <ls>Spr. 608, v. l. (Th. I, S. 320).</ls>
new: <ls>Spr. 608, v. l.</ls> (Th. I, S. 320). +

old: <ls>Spr. 660. 1678, v. l. (Th. III, S. 372). 2042, v. l. 2935, v. l.</ls>
new: <ls>Spr. 660. 1678, v. l.</ls> (Th. III, S. 372). <ls n="Spr.">2042, v. l.</ls> <ls n="Spr.">2935, v. l.</ls> +

old: <ls>Spr. 814, v. ( Th. 2, S. 330).</ls>
new: <ls>Spr. 814, v. l.</ls> (Th. 2, S. 330). +



----------------------------------------------

python lsother.py 1 lsother_0.txt lsother_1.txt lsother_1a.txt
1455 lines read from lsother_0.txt
1062 cases written to lsother_1.txt
393 cases written to lsother_1a.txt

------------------
# handle fg., fgg., v. l.
python lsother.py 2 lsother_1a.txt lsother_2.txt lsother_2a.txt
393 lines read from lsother_1a.txt
149 cases written to lsother_2.txt
244 cases written to lsother_2a.txt

------------------
# handle missing period at end
python lsother.py 3 lsother_2a.txt lsother_3.txt lsother_3a.txt
244 lines read from lsother_2a.txt
42 cases written to lsother_3.txt
202 cases written to lsother_3a.txt

------------------
# handle ).</ls>
python lsother.py 4 lsother_3a.txt lsother_4.txt lsother_4a.txt
202 lines read from lsother_3a.txt
21 cases written to lsother_4.txt
181 cases written to lsother_4a.txt

------------------
https://funderburkjim.github.io/boesp-prep/web1/boesp.html?185

<ls n="Spr.">747 (II). 3266.</ls> <L>90958<pc>6-0996<k1>vikriyA<k2>vikriyA
  747 is in Spr. (II)
  3266 NOT in Spr. (II)
  3266 in Spr. 1

python lsother.py 5 lsother_4a.txt lsother_5.txt lsother_5a.txt
181 lines read from lsother_4a.txt
73 cases written to lsother_5.txt
108 cases written to lsother_5a.txt

python lsother.py 6 lsother_5a.txt lsother_6.txt lsother_6a.txt
108 lines read from lsother_5a.txt
12 cases written to lsother_6.txt
96 cases written to lsother_6a.txt

------------------
python lsother.py 7 lsother_6a.txt lsother_7.txt lsother_7a.txt
96 lines read from lsother_6a.txt
48 cases written to lsother_7.txt
48 cases written to lsother_7a.txt

------------------
python manual_prep.py 1 lsother_7a.txt lsother_7a_edit.py 

Additional:
,
 '<ls n="Spr.">1895.</ls>' :
 '<ls n="Spr. (II)">1895.</ls>'

------------------
# note: option 8 imports 'd' from lsother_7a_edit.py 
python lsother.py 8 lsother_7a.txt lsother_8.txt lsother_8a.txt 
48 lines read from lsother_7a.txt
48 cases written to lsother_8.txt
0 cases written to lsother_8a.txt   #  no remaining cases!



------------------
$ wc -l lsother_?.txt
  1455 lsother_0.txt
  1062 lsother_1.txt
   149 lsother_2.txt
    42 lsother_3.txt
    21 lsother_4.txt
    73 lsother_5.txt
    12 lsother_6.txt
    48 lsother_7.txt
    48 lsother_8.txt
  2910 total

cat lsother_1.txt lsother_2.txt lsother_3.txt lsother_4.txt lsother_5.txt lsother_6.txt lsother_7.txt lsother_8.txt > lsother_all.txt

 wc -l lsother_all.txt
1455 lsother_all.txt  # ok, same as lsother_0.txt

------------------
# construct temp_pwg_2.txt by applying all the changes
# in lsother_all.txt
python lsother_process.py temp_pwg_1.txt lsother_all.txt temp_pwg_2.txt
1132566 lines read from temp_pwg_1.txt
1455 lines read from lsother_all.txt
0 problematic duplicates
1451 lines changed
1132566 cases written to temp_pwg_2.txt
ntot=1455, notused=0

-----------------
install temp_pwg_1.txt locally

cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

# regen local displays

cd  /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87/lsmarkup



----------------------------------------------


----------------------------
# make change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt changes_1.txt
# 97 changes written to changes_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt changes_2.txt
# 1451 changes written to changes_2.txt


----------------------------
commit temp_pwg_1.txt to github

cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

cd /c/xampp/htdocs/cologne/csl-orig
git pull
git add v02/pwg/pwg.txt
git commit -m "Spr. markup standardization change_1.txt
Ref: #87"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87/lsmarkup

----------------------------
# commit temp_pwg_2.txt to github

cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt

cd /c/xampp/htdocs/cologne/csl-orig
git pull
git add v02/pwg/pwg.txt
git commit -m "Spr. markup standardization change_2.txt
Ref: #87"
git push

------------------------
revise pwgbib
add one line
c.1542a	Beitr. z. vgl. Spr.	Beitr. z. vgl. Spr.	Beitr. z. vgl. Spr. = ? [Cologne Addition]

# copy to pywork repo
cp pwgbib_input.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt

# regen local displays of pwg (to check form of pwgbib_input)

cd  /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok
--------------
# commit csl-pywork to github
cd  /c/xampp/htdocs/cologne/csl-pywork/v02
git add .
git commit -m "Revise pwgbib_input.txt"
git push

-----------------------------
# revise pwg_printchange.txt in csl-corrections repo
81815 : yA : Spr. 1926, l. l. : Spr. 1926, v. l.
46573 : pUj : Spr. 7,2230, v. l. : Spr. 2230, v. l.

cd  /c/xampp/htdocs/cologne/csl-corrections
git pull  # picks up commit from Dhaval
git add .
git commit -m "PWG print changes.
> Ref: https://github.com/sanskrit-lexicon/PWG/issues/87
git push

START: cologne update csl-orig, csl-pywork, csl-corrections
This PWG repo.

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue87/lsmarkup

-----------------------------
-----------------------------
push this 'PWG' repository to github

