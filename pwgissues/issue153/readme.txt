06-22-2025
Gitagovinda link targer

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153

https://github.com/sanskrit-lexicon/pwg/issues/153


/e/pdfwork/gitagovinda/readme.txt

/e/pdfwork/gitagovinda/gitagov.pdf


pdf: /e/pdfwork/gitagovinda/gitagov.pdf

source: https://www.digitale-sammlungen.de/en/view/bsb10219656

rights:  https://rightsstatements.org/page/NoC-NC/1.0/

Title: Gitagovinda, ed. Lassen, 1836

223 pages in pdf

----------------------------------------
index_orig.txt
/e/pdfwork/gitagovinda/
ind.git.xlsx download from links in issue153
  Google docs convert ind.git.xlsx  to ind.git.tsv
  index_orig.txt Minor edit of ind.git.tsv

cp /e/pdfwork/gitagovinda/index_orig.txt /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153/index_orig.txt


pdfpage	adh.	Prabandha	from verse	to verse	ipage
46	1	1	1	4a	1
47	1	1	4b	8a	2
48	1	1	8b	13	3
49	1	1->2	14	18a	4
50	1	2	18b	23	5
51	1	2->3	24	28a	6

The 'arrow' notation is not used

changes to index.txt

---
old: 64	3	7->8	15	16	19
new: 64	4	7->8	1	3a	18
---
old: 98	12	23->24	12b	27	53
new: 98	12	23->24	12b	17	53

-------------------------------------

From issue94/lsexamine2.txt (pwg <ls>AK.  references
* 01140	GĪT.	GĪTAGOVINDA, ed. LASSEN (GILD. Bibl. 168
** !(1028) GĪT. with 2 numeric parameters 
** (96) GĪT. with OTHER parameters 
** (12) GĪT. with 1 numeric parameters
** (4) GĪT. with 0 numeric parameters 
======================================================
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

======================================================
preliminary checks with temp_pwg.txt

The references
The (predominant) 2-parameter references seem to be based on adhy,verse
  i.e., the 'prabandha' field does not appear


---
<L>2951<pc>1-0215<k1>anuraYjana : GĪT. 1,46. : ok
55	1	4	42b	47	10 
---
<L>15142<pc>2-0110<k1>karabAla : GĪT. 1,14 :  OK
49	1	1->2	14	18a	4
---
<L>17034<pc>2-0272<k1>kASmIra : GĪT. 1,25. : ok
51	1	2->3	24	28a	6
---
<L>17112<pc>2-0278<k1>kAsAra : GĪT. 2,20. :  ok
60	2	6->7	19	21	15
---
<L>91127<pc>6-1010<k1>vicAra : GĪT. 2,15. :  ok
59	2	6	13b	18	14
---
<L>15603<pc>2-0150<k1>kal : GĪT. 3,7. : ok
61	3	7	3	9a	16 
---
<L>54703<pc>5-0261<k1>BAvana : GĪT. 4,2. : ok
 This exposes an index error:
60	3	6->7	1	2	15
61	3	7	3	9a	16
62	3	7	9b	14	17
63	3	7->8	15	16	18

64	3	7->8	15	16	19 old
64	4	7->8	1	3a	18 new

64	4	8	3b	8a	19
65	4	8->9	8b	13	20
66	4	9	14	20	21
67	4	9->10	21	23	22
---
<L>51271<pc>4-1181<k1>prodboDa : GĪT. 5,18 : ok
70	5	11	13b	19a	25
---
<L>90819<pc>6-0984<k1>vikala : GĪT. 5,3 : ok
68	5	10->11	2	7a	23
---
<L>52760<pc>5-0091<k1>bisa : GĪT. 6,4 : ok
72	6	12	3b	8	27
---
<L>19011<pc>2-0423<k1>ketana : GĪT. 7,5. : ok
74	7	13	1	6a	29
<L>21311<pc>2-0620<k1>KyA : GĪT. 8,10. :  ok
83	8	17	5b	10	38
---
<L>24112<pc>2-0890<k1>GUrRana : GĪT. 9,11 : ok
86	9	18->19	11	11	41
---
<L>19241<pc>2-0441<k1>kokanada : GĪT. 10,5 : ok
87	10	19	3b	8a	42
---
<L>49630<pc>4-1058<k1>prayAsa : GĪT. 11,32 : ok
95	11	22	31b	34	50
---
<L>17399<pc>2-0303<k1>kIlita : GĪT. 12,13 : ok
98	12	23->24	12b	27	53
===========================================

python make_js_index.py index.txt index.js
64 Success: Page records read from index.txt
json data written to index.js
p
========================================
PWG  look for 'pagerec not found' errors
----------------------------------------
4 numeric parameters
python generate_random.py ALL pwg2 temp_pwg.txt index.txt check_pwg2_ALL.txt check_pwg_ALL_nopagerec.txt

found 1030 instances in kosha
found 254 distinct in kosha
write_examples: 1030 written to check_pwg2_ALL.txt
0 instances of 'pagerec not found'

===================================================
pw2  2-parameter references for pw.txt

python generate_random.py ALL pw2 temp_pw.txt index.txt check_pw2_ALL.txt check_pw2_ALL_nopagerec.txt

write_examples: 43 written to check_pw2_ALL.txt
0 instances of 'pagerec not found'

===================================================
pwkvn2  2-parameter references for pwkvn.txt

python generate_random.py ALL pwkvn2 temp_pwkvn.txt index.txt check_pwkvn2_ALL.txt check_pwkvn2_ALL_nopagerec.txt

write_examples: 24 written to check_pwkvn2_ALL.txt
0 instances of 'pagerec not found'

Gīt.
===================================================
sch2   2-parameter references for sch.txt

python generate_random.py ALL sch2 temp_sch.txt index.txt check_sch2_ALL.txt check_sch2_ALL_nopagerec.txt

write_examples: 23 written to check_sch2_ALL.txt
0 instances of 'pagerec not found'

=======================================================

cp temp_mw.txt temp_mw1.txt  # correct one error in mw

33390 : udBf : Gīt. 1, 16 : Gīt. i, 16 : mw typo
mw2   2-parameter references for mw1.txt

python generate_random.py ALL mw2 temp_mw1.txt index.txt check_mw2_ALL.txt check_mw2_ALL_nopagerec.txt

write_examples: 92 written to check_mw2_ALL.txt
0 instances of 'pagerec not found'

Note: There are 3 references with adhyAya but no verse.

=======================================================
  repo  sanskrit_lexicon_scans/gitagov
  install app1. See readme_app1.txt  
=======================================================
  links from kosha(s) to repo
edit  /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php


  cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02/
  sh generate_web.sh X  ../../X  (for X = pwg, pw, pwkvn, sch, ms)
  sh apidev_copy.sh  # for csl-apidev copy of basicadjust.php
  
# check local display links to gitagov for a few in  check_pwg2_ALL.txt,
# and similarly for the other dictionaries.


=======================================================
=======================================================
Everthing seems to work as needed.

Finish installation
-----------------------------
revisions to csl-orig local and Github

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153

cp temp_mw1.txt   /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt

cd /c/xampp/htdocs/cologne/csl-orig/v02
git add, commit, push to github

--------------------------------
# make change files
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue153

python diff_to_changes_dict.py  temp_mw.txt temp_mw1.txt change_mw_mw1.txt
 1 changes 


--------------------------------
sync csl-websanlexicon to github

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
git add, commit, push

sh apidev_copy.sh  # so csl-apidev has same basicadjust.php

--------------------------------
sync csl-apidev to github

cd /c/xampp/htdocs/cologne/csl-apidev
git add, commit, push

-------------------------------
regenerate local displays for mw, pwg, pw, pwkvn, sch
----------------------------------

==================================
sync local repos to github
csl-orig
csl-websanlexicon
csl-apidev

==================================
sync github to cologne
pull: csl-orig, csl-websanlexicon, csl-apidev

regenerate displays at cologne
cd csl-pywork/v02
sh generate_dict.sh pwg  ../../PWGScan/2020/
sh generate_dict.sh pw  ../../PWScan/2020/
sh generate_dict.sh pwkvn  ../../PWKVNScan/2020/
sh generate_dict.sh sch  ../../SCHScan/2020/
sh generate_dict.sh mw  ../../MWScan/2020/

----------------------------------
THE END

