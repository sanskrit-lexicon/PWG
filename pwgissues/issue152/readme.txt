issue152/readme.txt
06-13-2025 begun ejf
03364	HIT.	HITOPADEŚA, ed. SCHLEGEL und LASSEN (GIL


Ref: https://github.com/sanskrit-lexicon/PWG/issues/152

This issue152 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue152

-----------------
pdf: hitopadesha.pdf  

source:
https://www.digitale-sammlungen.de/en/view/bsb10219665
  Schlegel and Lassen, 1829
rights:
https://rightsstatements.org/page/NoC-NC/1.0/

----------------------------------------
index_orig.txt
  from ind.hit.1.xlsx: converted to tab-delimited  file using Google Docs
cp index_orig.txt index.txt
 index.txt lightly edited.

# format of index.txt (tab-separated values)
# 5 values per line
pdfpage	adh.	from verse	to verse	ipage
24	prooemium	1	6	3
30	I	1	3	9
66	II	1	5	45
100	III	1	3	79
130	IV	1	4	109
155	--	--	--	--

 
tantra is in roman numerals: prooemium, I, II, III, IV
-------------------------------------------
# construct index.js, and check for internal consistencies
python make_js_index.py index.txt index.js
--- adjustments
1. discard title line
2. discard lines at end with tantra = ''
3. change tantra to 0,1,2,3,4
   0 is the prasTAva

----------------------------------------
local copies of dictionaries with links
----------------------------------------
# get temporary local copy of dictionaries for checking
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt temp_pwkvn.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt temp_sch.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw.txt

----------------------------------------
forms of references for temp_pwg.txt
----
N,N    (ipage, linenum)   
  <ls>HIT. [0-9]+,[0-9]+  count = 1949
  small manual random check ok

----
RN (section, verse)    I, II, III, IV      
  986 matches in 985 lines for "<ls>HIT. \(I\|II\|III\|IV\),[0-9]+"
  small manual random check ok

----
PN Pr. verse
211 matches for "<ls>HIT. Pr\. [0-9]+" in buffer: temp_pwg1.txt

========================================
PWG  look for 'pagerec not found' errors
----------------------------------------
pwgRN <ls>HIT. (I|II|III|IV),([0-9]+)
python generate_random.py ALL pwgRN temp_pwg.txt index.txt check_pwgRN_ALL.txt check_pwgRN_ALL_nopagerec.txt

1 instance:
key (1, 227): pagerec not found
L= 8733, hw= Apad, pc=1-0658
cp temp_pwg.txt temp_pwg1.txt

# manual change to temp_pwg1.txt
8733 : Apad : HIT. I,227. : HIT. I,181 : ApadudDaraRa  pwg printchange
9860 : AsvAdya : HIT. Pr. 49 : HIT. Pr. 47 : pwg printchange

# rerun with temp_pwg1
python generate_random.py ALL pwgRN temp_pwg1.txt index.txt check_pwgRN_ALL_1.txt check_pwgRN_ALL_1_nopagerec.txt
regex_raw = <ls>HIT. (Pr.|I|II|III|IV),([0-9]+)
found 986 instances in kosha
0 instances of 'pagerec not found'  GOOD!

----------------------------------------
pwgPN <ls>HIT. (Pr.) ([0-9]+)
python generate_random.py ALL pwgPN temp_pwg1.txt index.txt check_pwgPN_ALL_1.txt check_pwgPN_ALL_1_nopagerec.txt

regex_raw = <ls>HIT. (Pr.) ([0-9]+)
found 211 instances in kosha
1 instances of 'pagerec not found'
write_examples: 1 written to check_pwgPN_ALL_1_nopagerec.txt
This requires another printchange to temp_pwg1.txt (AsvAdya Pr. 49 -> Pr. 47)

rerun
python generate_random.py ALL pwgPN temp_pwg1.txt index.txt check_pwgPN_ALL_1.txt check_pwgPN_ALL_1_nopagerec.txt

regex_raw = <ls>HIT. (Pr.) ([0-9]+)
found 211 instances in kosha
0 instances of 'pagerec not found'


----------------------------------------
pwgNN <ls>HIT. ([0-9]+),([0-9]+)
ipage, line-number
python generate_random.py ALL pwgNN temp_pwg1.txt index.txt check_pwgNN_ALL.txt check_pwgNN_ALL_nopagerec.txt

regex_raw = <ls>HIT. ([0-9]+),([0-9]+)
found 1949 instances in kosha
found 877 distinct in kosha
write_examples: 1949 written to check_pwgNN_ALL.txt
6 instances of 'pagerec not found'
write_examples: 6 written to check_pwgNN_ALL_nopagerec.txt

41027 : no : HIT. 1,82 : HIT. I,82 : pwg typo
36123 : Danus : HIT. 1,155 : HIT. I,155. : pwg typo
53759 : Bakzya : HIT. 1,158 : HIT. I,158 : pwg typo
36484 : DA : HIT. 1,171 : HIT. I,171 : pwg typo
61162 : muh : HIT. 136,10 : HIT. 116,10 : pwg print change vicAramUQayoH
61203 : mUQatA : HIT. 136,10 : HIT. 116,10 : pwg print change

rerun
python generate_random.py ALL pwgNN temp_pwg1.txt index.txt check_pwgNN_ALL_1.txt check_pwgNN_ALL_1_nopagerec.txt

regex_raw = <ls>HIT. ([0-9]+),([0-9]+)
found 1945 instances in kosha
0 instances of 'pagerec not found'


========================================
PW  look for 'pagerec not found' errors
----------------------------------------
pwRN <ls>HIT. (I|II|III|IV),([0-9]+)
python generate_random.py ALL pwRN temp_pw.txt index.txt check_pwRN_ALL.txt check_pwRN_ALL_nopagerec.txt

regex_raw = <ls>HIT. (I|II|III|IV),([0-9]+)
found 5 instances in kosha
0 instances of 'pagerec not found'

# since so few, manually check all in  check_pwRN_ALL.txt

cp temp_pw.txt temp_pw1.txt
# manual change to temp_pw1.txt
37314 : graB : HIT. II,2 : HIT. II,3 : pw typo

----------------------------------------
pwPN <ls>HIT. (Pr.) [0-9]+)   NONE!
python generate_random.py ALL pwPN temp_pw1.txt index.txt check_pwPN_ALL.txt check_pwPN_ALL_nopagerec.txt

regex_raw = <ls>HIT. (Pr.) ([0-9]+)
found 0 instances in kosha
found 0 distinct in kosha
write_examples: 0 written to check_pwPN_ALL.txt

----------------------------------------
pwNN <ls>HIT. ([0-9]+),([0-9]+)
ipage, line-number
python generate_random.py ALL pwNN temp_pw1.txt index.txt check_pwNN_ALL.txt check_pwNN_ALL_nopagerec.txt
regex_raw = <ls>HIT. ([0-9]+),([0-9]+)
found 50 instances in kosha
0 instances of 'pagerec not found'

========================================
PWKVN  look for 'pagerec not found' errors
----------------------------------------
pwkvnRN <ls>HIT. (I|II|III|IV),([0-9]+)
python generate_random.py ALL pwkvnRN temp_pwkvn.txt index.txt check_pwkvnRN_ALL.txt check_pwkvnRN_ALL_nopagerec.txt

regex_raw = <ls>HIT. (I|II|III|IV),([0-9]+)
found 0 instances in kosha
0 instances of 'pagerec not found'

----------------------------------------
pwkvnNN <ls>HIT. ([0-9]+),([0-9]+)
ipage, line-number
python generate_random.py ALL pwkvnNN temp_pwkvn.txt index.txt check_pwkvnNN_ALL.txt check_pwkvnNN_ALL_nopagerec.txt
regex_raw = <ls>HIT. ([0-9]+),([0-9]+)
found 10 instances in kosha
write_examples: 10 written to check_pwkvnNN_ALL.txt
1 instances of 'pagerec not found'

manual check all instances:
 2 not found pwkvn
 
key (46, 8): 67	II	6	13	46
L= 5084, hw= anupaBujyamAna, pc=4-292-b  pwkvn not found

key (60, 5): 81	II	86	89	60
L= 5008, hw= atipriya, pc=4-291-b  pwkvn not found

cp temp_pwkvn.txt temp_pwkvn1.txt
# manual change to temp_pwkvn1.txt
8637 : Avartin : HIT. 1,201 : HIT. I,201  : pwkvn typo
# similar change for temp_pw1.txt
208637 : Avartin : HIT. 1,201 : HIT. I,201 : pw typo
# similar change for temp_pwg1.txt

# similar change in sch
cp temp_sch.txt temp_sch1.txt
7375 : Avartam : Hit. 1,201 : Hit. I,201  : sch printchange

--rerun
python generate_random.py ALL pwkvnNN temp_pwkvn1.txt index.txt check_pwkvnNN_ALL_1.txt check_pwkvnNN_ALL_1_nopagerec.txt

========================================
SCH  look for 'pagerec not found' errors
----------------------------------------
schRN
python generate_random.py ALL schRN temp_sch.txt index.txt check_schRN_ALL.txt check_schRN_ALL_nopagerec.txt
regex_raw = <ls>Hit. (I|II|III|IV),([0-9]+)
found 0 instances in kosha
found 0 distinct in kosha
w
----------------------------------------
After Avartam change, there is 1 of this form in sch1

python generate_random.py ALL schRN temp_sch1.txt index.txt check_schRN_ALL_1.txt check_schRN_ALL_1_nopagerec.txt
regex_raw = <ls>Hit. (I|II|III|IV),([0-9]+)
found 1 instances in kosha
found 1 distinct in kosha
write_examples: 1 written to check_schRN_ALL_1.txt
0 instances of 'pagerec not found'

------------------------------------
schNN <ls>HIT. ([0-9]+),([0-9]+)
ipage, line-number
python generate_random.py ALL schNN temp_sch.txt index.txt check_schNN_ALL.txt check_schNN_ALL_nopagerec.txt

regex_raw = <ls>Hit. ([0-9]+),([0-9]+)
found 10 instances in kosha
0 instances of 'pagerec not found'

manual check all instances:
 
2 not found in sch:
key (46, 8): 67	II	6	13	46
L= 2724, hw= anupaBujyamAna, pc=037-2

key (60, 5): 81	II	86	89	60
L= 1139, hw= atipriya, pc=016-2

========================================
MW  look for 'pagerec not found' errors
------------------------------------
cp temp_mw.txt temp_mw1.txt
# print changes
18726 : avicArita : Hit. xii, 16 : Hit. 12, 16 : mw printchange (line 16 page 12)
48891 : kAryaparicCeda : Hit. xxxii, 22 : Hit. 32, 22 : mw printchange (line 22 page 32)
117806 : pariDvaMsin : Hit. v, 118 : Hit. ii, 118 : mw printchange
90640 : darSana : Hit. iii, 0/1 : Hit. Introd. 9, 0/1 : mw printchange?
   Scan MAY have: Hit. iii, 9, 0/1
   PWG under darSana has 'HIT. Pr. 9'
76735 : jan : Hit. <ab>Introd.</ab> 14</ls> : Hit. Introd. 14</ls> mw typo markup
90608 : darSaka : Hit. <ab>Introd.</ab> 10</ls> : Hit. Introd. 10</ls> mw typo markup
----------------------------------------
mwRN

mwRN <ls>Hit. (i|ii|iii|iv), *([0-9]+)
python generate_random.py ALL mwRN temp_mw.txt index.txt check_mwRN_ALL.txt check_mwRN_ALL_nopagerec.txt
regex_raw = <ls>Hit. (|i|ii|iii|iv), *([0-9]+)
found 98 instances in kosha
1 instances of 'pagerec not found'
write_examples: 1 written to check_mwRN_ALL_nopagerec.txt
  key (3, 0): pagerec not found
L= 90640, hw= darSana, pc=471,1


# rerun using mw1
python generate_random.py ALL mwRN temp_mw1.txt index.txt check_mwRN_ALL_1.txt check_mwRN_ALL_1_nopagerec.txt

regex_raw = <ls>Hit. (Introd.|i|ii|iii|iv), *([0-9]+)
found 97 instances in kosha
0 instances of 'pagerec not found'

----------------------------------------
mwPN   the prastAva.  This requires separate regex since there is no
  comma after 'Introd.'

mwPN <ls>Hit. (Introd.) *([0-9]+)
python generate_random.py ALL mwPN temp_mw1.txt index.txt check_mwPN_ALL_1.txt check_mwPN_ALL_1_nopagerec.txt

regex_raw = <ls>Hit. (Introd.) *([0-9]+)
found 3 instances in kosha
0 instances of 'pagerec not found'


----------------------------------------
After correction, there are a couple of NN (ipage, line-number) references
mwNN <ls>Hit. ([0-9]+),([0-9]+)

python generate_random.py ALL mwNN temp_mw1.txt index.txt check_mwNN_ALL_1.txt check_mwNN_ALL_1_nopagerec.txt

regex_raw = <ls>Hit. ([0-9]+), *([0-9]+)
found 2 instances in kosha
0 instances of 'pagerec not found'
These two check.

----------------------------------------
----------------------------------------
app construction.
2 apps are needed:
app1 -- (tantra,shloka) see readme_app1.txt
app2 -- (ipage,line-number)  see readme_app2.txt

=============================================================
move corrections to csl-orig and regen local displays

cp temp_pwg1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cp temp_pw1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt
cp temp_pwkvn1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwkvn/pwkvn.txt
cp temp_sch1.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt
cp temp_mw1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt

make change files
python diff_to_changes_dict.py temp_pwg.txt temp_pwg1.txt change_pwg_pwg1.txt
10 changes written to change_pwg_pwg1.txt

python diff_to_changes_dict.py temp_pw.txt temp_pw1.txt change_pw_pw1.txt
2 changes written to change_pw_pw1.txt

python diff_to_changes_dict.py temp_pwkvn.txt temp_pwkvn1.txt change_pwkvn_pwkvn1.txt
1 changes written to change_pwkvn_pwkvn1.txt

python diff_to_changes_dict.py temp_sch.txt temp_sch1.txt change_sch_sch1.txt
1 changes written to change_sch_sch1.txt

python diff_to_changes_dict.py temp_mw.txt temp_mw1.txt change_mw_mw1.txt
6 changes written to change_mw_mw1.txt

=============================================================
regenerate all checks with version1 of koshas
python generate_random.py ALL mwNN temp_mw1.txt index.txt check_mwNN_ALL_2.txt check_mwNN_ALL_2_nopagerec.txt
python generate_random.py ALL mwRN temp_mw1.txt index.txt check_mwRN_ALL_2.txt check_mwRN_ALL_2_nopagerec.txt
python generate_random.py ALL mwPN temp_mw1.txt index.txt check_mwPN_ALL_2.txt check_mwPN_ALL_2_nopagerec.txt

python generate_random.py ALL pwNN temp_pw1.txt index.txt check_pwNN_ALL.txt check_pwNN_ALL_nopagerec.txt
python generate_random.py ALL pwRN temp_pw1.txt index.txt check_pwRN_ALL.txt check_pwRN_ALL_nopagerec.txt
python generate_random.py ALL pwPN temp_pw1.txt index.txt check_pwPN_ALL.txt check_pwPN_ALL_nopagerec.txt

python generate_random.py ALL pwgNN temp_pwg1.txt index.txt check_pwgNN_ALL.txt check_pwgNN_ALL_nopagerec.txt
python generate_random.py ALL pwgRN temp_pwg1.txt index.txt check_pwgRN_ALL_2.txt check_pwgRN_ALL_2_nopagerec.txt
python generate_random.py ALL pwgPN temp_pwg1.txt index.txt check_pwgPN_ALL_2.txt check_pwgPN_ALL_2_nopagerec.txt

python generate_random.py ALL pwkvnNN temp_pwkvn1.txt index.txt check_pwkvnNN_ALL_2.txt check_pwkvnNN_ALL_2_nopagerec.txt
python generate_random.py ALL pwkvnRN temp_pwkvn1.txt index.txt check_pwkvnRN_ALL_2.txt check_pwkvnRN_ALL_2_nopagerec.txt
python generate_random.py ALL pwkvnPN temp_pwkvn1.txt index.txt check_pwkvnPN_ALL_2.txt check_pwkvnPN_ALL_2_nopagerec.txt

python generate_random.py ALL schNN temp_sch1.txt index.txt check_schNN_ALL_2.txt check_schNN_ALL_2_nopagerec.txt
python generate_random.py ALL schRN temp_sch1.txt index.txt check_schRN_ALL_2.txt check_schRN_ALL_2_nopagerec.txt
python generate_random.py ALL schPN temp_sch1.txt index.txt check_schPN_ALL_2.txt check_schPN_ALL_2_nopagerec.txt


=============================================================
activate links from koshas.
revise basicadjust.php, using the various regex patterns above.

Regenerate local copies:

cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh pwg  ../../pwg
sh generate_web.sh pw  ../../pw
sh generate_web.sh pwkvn  ../../pwkvn
sh generate_web.sh sch  ../../sch
sh generate_web.sh mw  ../../mw

sh apidev_copy.sh

Samples:


----------------------------------------
=============================================================
sync to github:  csl-websanlexicon, csl-apidev, csl-orig

install to cologne:
 csl-orig
 etc....
