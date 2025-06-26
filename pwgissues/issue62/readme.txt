
04-01-2025
 see cd /c//xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ak
 https://archive.org/download/ColebrookeAmarakosha1891_201809/Colebrooke_Amarakosha_1891.pdf
 cd /e/pdfwork/amarakosha
 Colebrooke_Amarakosha_1891.pdf
 Not further used?
=========================================================
06-16-2025

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue62

Amarakosha (AK.) link target 
https://github.com/sanskrit-lexicon/pwg/issues/62


deslongchamps of 1839
Ref: /e/pdfwork/amarakosha/readme.txt
index_orig.txt
cp /e/pdfwork/amarakosha/AMARAKO.A.1839.Deslongchamps.ed.1.tsv index_1839.txt

pdf:
/e/pdfwork/amarakosha/delong1839.pdf

-------------------------------------
cp index_1839.txt index.txt

Allow manual changes to index.txt
---
old: I	63	1	1	5	1a	1a	34	
new: I	63	1	1	5	1	1a	34	
---
old: I	369	3	4	28	220a	220a	340	
new: I	369	3	4	28	219	220a	340	
---
old: I	82	1	2	1	6b	11	53	
new: I	82	1	2	1	6b	12	53	AhituRqika '12' missing in scan
---
old: I	137	2	4	4	21b	22	108	v. 22 repeated
new: I	137	2	4	4	21b	23	108	v. 22 repeated
---
old: I	336	3	4	17	102	104	307
new: I	336	3	4	18	102	104	307
---
old: I	337	3	4	17	105	107a	308	
new: I	337	3	4	18	105	107a	308	
---
old: I	343	3	4	18	126b	130a	314	
I	343	3	4	18	126b	129	314	change so next page works
---
old: I	344	3	4	18	130b	130b	315	
new: I	344	3	4	18	130	131	315	131 in sec. 18 and 19!
---
old: I	370	3	4	29	222	225a	341	
new: I	370	3	4	29	222	224	341	
---
old: I	371	3	4	29	225	227	342	
new: I	371	3	4	30	225	227	342	
---
old: I	371	3	4	30	228a	228a	342	line deleted
---
old: I	372	3	4	30	228b	231	343	
new: I	372	3	4	30	228	231	343	
---
old: I	374	3	4	30	235	237	345
new: I	374	3	4	30	235	237	345
---
old: I	374	3	4	31	238a	238a	345	line deleted
---
old: I	375	3	4	31	238b	241	346	
new: I	375	3	4	31	238	241	346	

cp index.txt index_v1.txt  # in case there are more changes.

-------------------------------------
Format of index_1839.txt

vol.	page	book	chapter	section	from v.	to v.	ipage	remark(s)
I	30	---	---	---	1	5	1	Introductory part
I	31	---	---	---	---	---	2	
I	32	1	1	1	1	4	3	


From issue94/lsexamine2.txt (pwg <ls>AK.  references
16155	AK.	AMARAKOṢA nach der Ausgabe von COLEBROOK
** (9473) AK. with 4 numeric parameters
** (5378) AK. with 3 numeric parameters
** (1137) AK. with 0 numeric parameters
** (131) AK. with OTHER parameters
** (20) AK. with 1 numeric parameters
** (16) AK. with 2 numeric parameters


======================================================
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

======================================================
preliminary checks with temp_pwg.txt

4-parameter sample references
# application of index is straightforward

---
<L>17557<pc>2-0315<k1>kuwwanI :  AK. 2,6,1,19 :
I	159	2	6	1	18b	22a	130	
---
<L>21861<pc>2-0693<k1>garala : AK. 1,2,1,10
I	82	1	2	1	6b	11	53	
---
<L>31993<pc>3-0512<k1>dantAvala : AK. 2,8,2,2
I	211	2	8	2	1	3	182	
---
<L>44404<pc>4-0654<k1>pAdANgada : AK. 2,6,3,11
I	181	2	6	3	9b	13a	152	
---
<L>56079<pc>5-0412<k1>BrURa : AK. 3,4,13,48
I	321	3	4	13	48	51a	292	
---
<L>60621<pc>5-0790<k1>mihira : AK. 1,1,2,31
I	49	1	1	2	27	32	20	
---
<L>84942<pc>6-0386<k1>rudra : AK. 1,1,1,30
I	36	1	1	1	25	31	7	
---
<L>89222<pc>6-0871<k1>vahni : AK. 2,4,2,60
I	125	2	4	2	56b	60	96	

========================================================
3-parameter references
<L>3986<pc>1-0295<k1>apasada : AK. 2,10,16
I	261	2	10	---	14b	20a	232	
---
<L>4034<pc>1-0298<k1>apahnava : AK. 3,4,210  nihnava found ?
I	366	3	4	27	208	211	337	
---
<L>40375<pc>4-0264<k1>nihnava : AK. 3,4,27,210
I	366	3	4	27	208	211	337	
---
<L>6847<pc>1-0504<k1>avyakta : AK. 3,4,64.
I	325	3	4	14	62b	65a	296	
---
<L>11559<pc>1-0936<k1>unduru : AK. 2,5,12
I	147	2	5	---	8	12a	118	unduru here
I	148	2	5	---	12b	16a	119	
---
<L>21893<pc>2-0696<k1>gargara : AK. 2,9,75
I	249	2	9	---	73b	77	220	
---
<L>38508<pc>4-0118<k1>nArAca : AK. 2,10,32
I	264	2	10	---	29b	33a	235	
---
<L>52832<pc>5-0096<k1>bIjya : AK. 2,7,2
I	188	2	7	---	1	2a	159	
I	189	2	7	---	2b	6a	160	vIjyas
---
<L>83009<pc>6-0234<k1>rajaka : AK. 2,10,10
I	259	2	10	---	6	10a	230	
I	260	2	10	---	10b	14a	231	rajaka
---
<L>101905<pc>7-0392<k1>SreyaMs : AK. 3,2,8
I	282	3	2	---	7b	12a	253	

============================================================

========================================
PWG  look for 'pagerec not found' errors
----------------------------------------
4 numeric parameters
python generate_random.py ALL pwg4 temp_pwg.txt index.txt check_pwg4_ALL.txt check_pwg4_ALL_nopagerec.txt

69 instances of pagerec not found

make changes to index.txt  (see above)
cp temp_pwg.txt temp_pwg1.txt

# make changes to temp_pwg1.txt


26 pwg print
 8 pwg typo
25 index (change/error)
 3 ? unsolved problem
62 All nopagerec

Make the 34 (26+8) changes to temp_pwg1.txt

+ 86101 : lavaRa : AK. 1,1,14,18 :  AK. 1,1,4,18 :  pwg typo
+ 43758 : pavanASana : AK. 1,2,1,19 :  AK. 1,2,1,9 : pwg printchange
+ 4482  : aBikrama : AK. 2,8,3,64 :  AK. 2,8,2,64 :  pwg print change
+ 5780  : arkaparRa : AK. 2,4,2,68 :  AK. 2,4,2,61 : pwg printchange
+ 102132 : SvaBra : AK. 3,6,1,22 :  AK. 3,6,3,22 : pwg printchange
+ 104058 : satya : AK. 3,4,25,156 :  AK. 3,4,24,156 : pwg printchange
+ 113947 : sTAna : AK. 3,4,22,212 :  AK. 3,4,27,212 : pwg typo
+ 116463 : hava : AK. 3,4,17,209 :  AK. 3,4,27,209 : pwg printchange
+ 12196  : upasTa : AK. 6,2,2,26 :  AK. 2,6,2,26 : pwg printchange
+ 14988  : kam : AK. 2,4,32,11 :  AK. 3,4,32,11 : pwg printchange
+ 15427  : kartar : AK. 3,6,1,15 :  AK. 3,6,2,15 : pwg printchange
+ 15523  : karman : AK. 3,4,21,157 :  AK. 3,4,24,157 : pwg printchange
+ 20033  : klIba : AK. 3,4,22,215 :  AK. 3,4,27,215 : pwg typo
+ 20107  : kzattar : AK. 3,4,11,65 :  AK. 3,4,14,65 : pwg typo
+ 21814  : gam : AK. 3,4,18,131 :  3,4,19,131 :  pwg print change ?
+ 26424  : jawAmAMsI : AK. 2,4,4,32 :  AK. 2,4,4,22 : pwg printchange
+ 34348  : dfzwAnta : AK. 3,4,19,65 :  AK. 3,4,14,65 : pwg printchange
+ 38752  : nigama : AK. 3,4,22,142 :  AK. 3,4,23,142 :  pwg print change
+ 39609  : niryAsa : AK. 3,4,34,155 :  AK. 3,4,24,155 : pwg typo
+ 39754  : nirvyApAra : AK. 3,4,12,50 :  AK. 3,4,13,50 : pwg typo
+ 42709  : parigraha : AK. 3,4,21,239 :  AK. 3,4,31,239 : pwg printchange
+ 47639  : prakarza : AK. 3,2,2,61 :  AK. 3,2,61 :  pwg print change
+ 53377  : brahman : AK. 3,4,18,147 :  AK. 3,4,18,117 : pwg typo
+ 54454  : BAgya : AK. 3,1,24,157 :  AK. 3,4,24,157 :  pwg printchange
+ 83607  : raya : AK. 3,4,24,28 :  AK. 3,4,4,28 : pwg printchange
+ 85738  : laGu : AK. 3,4,4,29 :  AK. 3,4,4,28 : pwg printchange. index irregular!
+ 86636  : loka : AK. 3,4,4,2 :  AK. 3,4,1,2 :  pwg printchange
+ 88102  : var : AK. 3,4,24,175 :  AK. 3,4,25,175 :  pwg printchange
+ 91865  : viDA : AK. 3,3,18,104 :  AK. 3,4,17,104 : pwg printchange
+ 94954  : vfndAraka : AK. 3,2,2,62 :  AK. 3,2,62 : pwg print change
+ 94959  : vfndizWa : AK. 3,2,2,62 :  AK. 3,2,62 : pwg print change
+ 95073  : vfzAkapi : AK. 3,4,29,132 :  AK. 3,4,19,132 : pwg printchange
+ 96240  : vyaqambaka : AK. 2,4,3,32 :  AK. 2,4,2,32 : pwg typo
+ 96445  : vyasana : AK. 3,4,14,28 :  AK. 3,4,4,28 : pwg printchange

# Rerun using (revised) index.txt and temp_pwg1.txt

python generate_random.py ALL pwg4 temp_pwg1.txt index.txt check_pwg4_ALL_1.txt check_pwg4_ALL_1_nopagerec.txt

36 instances of 'pagerec not found'
write_examples: 36 written to check_pwg4_ALL_1_nopagerec.txt
This is much more than expected!!! What's going on?

more changes to temp_pwg1.txt

47791 : pragalBa : AK. 3,4,16,98 :  AK. 3,4,17,98 : pwg printchange
48865 : pratyagra : (AK.) 3,4,16,98  : (AK.) 3,4,17,98  : pwg printchange
91865 : viDA : AK. 3,3,17,104 :  AK. 3,4,18,104 : pwg printchange
50870 : prArTana : AK. 3,4,17,102 :  AK. 3,4,18,102 : pwg print
56888 : maDu : AK. 3,4,17,105 :  AK. 3,4,18,105 : pwg print
104717 : saMDA : AK. 3,4,17,105 :  AK. 3,4,18,105 : pwg print
106122 : saMpratyaya : AK. 3,4,17,105 :  AK. 3,4,18,105 : pwg print
22040 : garvita AK. 3,4,17,106 :  AK. 3,4,18,106 :  pwg printhange 
38095 : nah AK. 3,4,17,106 :  AK. 3,4,18,106 :  pwg printhange 
39476 : nirdeSa AK. 3,4,17,106 :  AK. 3,4,18,106 :  pwg printhange 
41760 : paRqitaMmanya : AK. 3,4,17,106 :  AK. 3,4,18,106 :  pwg printhange 
53415 : brahmabanDu : AK. 3,4,17,106 :  AK. 3,4,18,106 :  pwg printhange 
86010 : lamb : AK. 3,4,17,106 :  AK. 3,4,18,106 :  pwg printhange 
113579 : staB : AK. 3,4,17,106 :  AK. 3,4,18,107 :  pwg printhange 
109441 : siD : AK. 3,4,17,107 :  AK. 3,4,18,107 :  pwg printhange 
54690 : BAva : AK. 3,4,29,225 :  AK. 3,4,30,225 :  pwg printhange 
68443 : upAdAna : AK. 3,4,29,225 :  AK. 3,4,30,225 :  pwg printhange 
93719 : viza : AK. 3,4,29,225 :  AK. 3,4,30,225 :  pwg printhange 
40656 : nftya : AK. 3,4,29,226 :  AK. 3,4,30,226 :  pwg printhange 
51117 : prekzA : AK. 3,4,29,226 :  AK. 3,4,30,226 :  pwg printhange 
54824 : BikzA : AK. 3,4,29,226 :  AK. 3,4,30,226 :  pwg printhange 
86663 : lokaDAtu : AK. 3,4,29,226 :  AK. 3,4,30,226 :  pwg printhange 
41066 : nyakza : AK. 3,4,29,227 :  AK. 3,4,30,227 :  pwg printhange 
48832 : pratyakza : (AK.) 3,4,29,227 : (AK.) 3,4,30,227 : pwg printchange
15590 : karz : (AK.) 3,4,29,227 : (AK.) 3,4,30,227 : pwg printchange
85099 : rUkza : AK. 3,4,29,227 :  AK. 3,4,30,227 :  pwg printhange 
114795 : srotas : AK. 3,4,31,235 :  AK. 3,4,30,235 : pwg printchange
30476 : tejas : AK. 3,4,31,236 :  AK. 3,4,30,236 : pwg printchange
52834 : bIBatsa : AK. 3,4,31,236 :  AK. 3,4,31,236 : pwg printchange
91581 : vid : AK. 3,4,31,236 :  AK. 3,4,30,236 : pwg printchange

# Rerun using (revised) index.txt and revised temp_pwg1.txt

python generate_random.py ALL pwg4 temp_pwg1.txt index.txt check_pwg4_ALL_2.txt check_pwg4_ALL_2_nopagerec.txt

10 instances of 'pagerec not found'

# Rerun using  revised temp_pwg1.txt

python generate_random.py ALL pwg4 temp_pwg1.txt index.txt check_pwg4_ALL_3.txt check_pwg4_ALL_3_nopagerec.txt
2 pagerec not found

13545 : elA : AK. 2,2,4,13 :  AK. 2,4,4,13 :  pwg printchange
94971 : vfza : AK. 3,4,22,229 :  AK. 3,4,29,222 : pwg printchange

# Rerun using  revised temp_pwg1.txt

python generate_random.py ALL pwg4 temp_pwg1.txt index.txt check_pwg4_ALL_4.txt check_pwg4_ALL_4_nopagerec.txt

0 instances of 'pagerec not found'

===================================================
pwg3   3-parameter references

python generate_random.py ALL pwg3 temp_pwg1.txt index.txt check_pwg3_ALL.txt check_pwg3_ALL_nopagerec.txt

found 668 distinct in kosha
write_examples: 5067 written to check_pwg3_ALL.txt
4 written to check_pwg3_ALL_nopagerec.txt

20742 : kzveqa : AK. 2,8,275 :  AK. 2,8,2,75 : pwg printchange
54198 : BarUjA : AK. 2,24,8 :  AV. 2,24,8 : pwg typo
116720 : hA : AK. 4,4,32 (28),18. : AK. 3,4,32,18 (28). : pwg printchange
51847 : barjahya : AK. 11,8,14 :  AV. 11,8,14 : pwg printchange (cf. PW)

# Rerun with revised temp_pwg1

python generate_random.py ALL pwg3 temp_pwg1.txt index.txt check_pwg3_ALL_1.txt check_pwg3_ALL_1_nopagerec.txt

0 instances of 'pagerec not found'


===================================================
pw4   4-parameter references for pw.txt

python generate_random.py ALL pw4 temp_pw.txt index.txt check_pw4_ALL.txt check_pw4_ALL_nopagerec.txt

cp temp_pw.txt temp_pw1.txt
# edit temp_pw1.txt

129163 : sfzwi : AK. 3,4,9,4 :  AK. 3,4,9,41 : pw typo

# Rerun with temp_pw1.txt
python generate_random.py ALL pw4 temp_pw1.txt index.txt check_pw4_ALL_1.txt check_pw4_ALL_1_nopagerec.txt

0 instances of 'pagerec not found'

===================================================
pw3   3-parameter references for pw.txt

python generate_random.py ALL pw3 temp_pw1.txt index.txt check_pw3_ALL.txt check_pw3_ALL_nopagerec.txt

found 17 instances in kosha
found 17 distinct in kosha
write_examples: 17 written to check_pw3_ALL.txt
0 instances of 'pagerec not found'

===================================================
sch4   4-parameter references for sch.txt

python generate_random.py ALL sch4 temp_sch.txt index.txt check_sch4_ALL.txt check_sch4_ALL_nopagerec.txt
found 4 instances in kosha

0 instances of 'pagerec not found'
All 4 instances checked.

===================================================
sch3   3-parameter references for sch.txt

python generate_random.py ALL sch3 temp_sch.txt index.txt check_sch3_ALL.txt check_sch3_ALL_nopagerec.txt

found 1 instances in kosha

0 instances of 'pagerec not found'

cp temp_sch.txt temp_sch1.txt
edit temp_sch1.txt

2923 : anUQa : AK. 2,7,35 ; AK. 2,7,55 : sch printchange
206242 : anUQa : AK. 2,7,35 : AK. 2,7,55 : pw printchange


=======================================================
pwkvn4  look for 'pagerec not found' errors
----------------------------------------
4 numeric parameters
python generate_random.py ALL pwkvn4 temp_pwkvn.txt index.txt check_pwkvn4_ALL.txt check_pwkvn4_ALL_nopagerec.txt

write_examples: 4 written to check_pwkvn4_ALL.txt
0 instances of 'pagerec not found'


=======================================================
pwkvn3

python generate_random.py ALL pwkvn3 temp_pwkvn.txt index.txt check_pwkvn3_ALL.txt check_pwkvn3_ALL_nopagerec.txt

found 2 distinct in kosha
write_examples: 2 written to check_pwkvn3_ALL.txt
0 instances of 'pagerec not found'



cp temp_pwkvn.txt temp_pwkvn1.txt
# this one not found, so change made.
6242 : anUQa : AK. 2,7,35 : AK. 2,7,55 : pwkvn printchange

=======================================================
MW has one (titular) reference paruzIkfta  with abbrev. <ls>Am.</ls>

=======================================================

Finish installations
-----------------------------

revise index for app1 (see readme_app1.txt)

cd /c/xampp/htdocs/sanskrit-lexicon-scans/amara_dlc
commit and push this repo

-----------------------------
revisions to csl-orig
temp_pwg1.txt, temp_pw1.txt, temp_pwkvn1.txt, temp_sch1.txt

cp temp_pwg1.txt   /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cp temp_pw1.txt    /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cp temp_pwkvn1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cp temp_sch1.txt   /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt

cd /c/xampp/htdocs/cologne/csl-orig/v02
git add, commit, push to github

--------------------------------
# make change files

python diff_to_changes_dict.py  temp_pwg.txt temp_pwg1.txt change_pwg_pwg1.txt
 77 changes

python diff_to_changes_dict.py  temp_pw.txt temp_pw1.txt change_pw_pw1.txt
 2 changes

python diff_to_changes_dict.py  temp_pwkvn.txt temp_pwkvn1.txt change_pwkvn_pwkvn1.txt
 1 change

python diff_to_changes_dict.py  temp_sch.txt temp_sch1.txt change_sch_sch1.txt
 1 change
 
-------------------------------
change_notes.txt is extracted from readme.txt, and has all the kosha changes

-------------------------------
regenerate local displays for pwg, pw, pwkvn, sch
----------------------------------

use change_notes.txt to update the printchanges files in csl-corrections repo

==================================
sync local repos to github
csl-orig
csl-websanlexicon
csl-apidev

==================================
sync github to cologne
csl-orig, csl-websanlexicon, csl-apidev

regenerate displays at cologne
----------------------------------
sync csl-corrections

=================================
See readme1.txt for further changes

