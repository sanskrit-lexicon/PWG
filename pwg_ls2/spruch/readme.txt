PWG/pwg_ls2/spruch


Refer:
 https://github.com/

Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  e66d896a3a99e6ba9f5b188220dc78227e57447a
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pw_00.txt in this spruch directory
  git show e66d896a:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/spruch/temp_pwg_00.txt
# return to this spruch directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/spruch/
# -------------------------------------------------------------
Focus on ls of form '<ls>Spr. (II)...</ls>'
# -------------------------------------------------------------
5313 matches in 5307 lines for "<ls>Spr. (II)" in buffer: temp_pwg_00.txt


python listls_abnormal.py 'Spr. (II)' temp_pwg_00.txt listls_abnormal_SprII.txt

 
 1a <ls>Spr. (II) [0-9]+[.]?</ls> 4169
 1b <ls>Spr. (II) [0-9]+[.]? fgg?[.]</ls> 42
 1c <ls>Spr. (II) [0-9]+[.,]? v[.] l[.]</ls> 216
 4427 normal
 2a <ls n="Spr. (II)">[0-9]+[.]?</ls> 0
 2b <ls n="Spr. (II)">[0-9]+[. fgg?]?</ls> 0
 2c <ls n="Spr. (II)">[0-9]+[.,]? v[.] l[.]</ls> 0

  891 abnormal  

# -------------------------------------------------------------
change_01.txt manually constructed in steps
# -------------------------------------------------------------
# 1st step of markup improvement
Separate out the 1st edition references
  <ls>Spr. (II) ... (I) ...</ls ->
  <ls>Spr. (II) ...</ls> <ls n="Spr.">(I) ...N2.</ls> 

python make_change_ls.py 1 temp_pwg_00.txt temp_change_01.txt
 110 lines changed
 
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt

# -------------------------------------------------------------
# 2nd step of markup improvement
python make_change_ls.py 2 temp_pwg_01.txt temp_change_02.txt
  generates prototype changes.
  <ls>Spr. (II) N1. N2. ... Nk.</ls ->
  <ls>Spr. (II) N1.</ls> <ls n="Spr. (II)">N2.</ls> ... <ls n="Spr. (II)">Nk.</ls>
 682 changes
 
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt

python listls_abnormal.py 'Spr. (II)' temp_pwg_01.txt temp_listls_abnormal_SprII.txt

4897 ls instances of type 1a
43 ls instances of type 1b
213 ls instances of type 1c
1229 ls instances of type 2a

6382 (+ 4897 43 213 1229) normal
160 abnormal ls written to temp_listls_abnormal_SprII.txt


# -------------------------------------------------------------
# 2a step of markup improvement
 '</ls> <ls>v. l.'  -> ' v. l.'  
  ('</ls> <ls>fgg.',' fgg.'),
  ('</ls> <ls>fg.',' fg.'),
python make_change_ls.py 2a temp_pwg_01.txt temp_change_02a.txt
# update change_01.txt with temp_change_02a.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt

# -------------------------------------------------------------
# 3rd step of markup improvement
# handle cases like
 <ls>Spr. (II) N1. N2, v. l.</ls> or
 <ls>Spr. (II) N1. N2. fg.</ls> or
 <ls>Spr. (II) N1. N2. fgg.</ls> or

python make_change_ls.py 3 temp_pwg_01.txt temp_change_03.txt
 42
 # append temp_change_03 to change_01
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 898 changes
 
python listls_abnormal.py 'Spr. (II)' temp_pwg_01.txt temp_listls_abnormal_SprII.txt

4939 ls instances of type 1a
43 ls instances of type 1b
213 ls instances of type 1c
1279 ls instances of type 2a
15 ls instances of type 2b
27 ls instances of type 2c

6516 (+ 4939 43 213 1279 15 27)
118 abnormal ls written to temp_listls_abnormal_SprII.txt

# -------------------------------------------------------------
# 4th step of markup improvement
# handle cases like
 <ls>Spr. (II) N1. N2, v. l. N3.</ls> or

python make_change_ls.py 4 temp_pwg_01.txt temp_change_04.txt
 45 
# append temp_change_04 to change_01
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 943 changes
 
python listls_abnormal.py 'Spr. (II)' temp_pwg_01.txt temp_listls_abnormal_SprII.txt

python listls_abnormal.py 'Spr.' temp_pwg_01.txt temp_listls_abnormal_Spr.txt
4964 ls instances of type 1a
43 ls instances of type 1b
233 ls instances of type 1c
1395 ls instances of type 2a
15 ls instances of type 2b
62 ls instances of type 2c

6712 normal (+ 4964 43 233 1395 15 62)
73 abnormal ls written to temp_listls_abnormal_SprII.txt

# -------------------------------------------------------------
# 5th step of markup improvement
# handle cases like
 <ls>Spr. (II) N1. N2. fg. N3.</ls> or
 <ls>Spr. (II) N1. N2. fgg. N3.</ls> or

python make_change_ls.py 5 temp_pwg_01.txt temp_change_05.txt
 28
# append temp_change_05 to change_01
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 971 changes
 
python listls_abnormal.py 'Spr. (II)' temp_pwg_01.txt temp_listls_abnormal_SprII.txt

4979 ls instances of type 1a
56 ls instances of type 1b
233 ls instances of type 1c
1510 ls instances of type 2a
37 ls instances of type 2b
62 ls instances of type 2c

6877 (+ 4979 56 233 1510 37 62)
46 abnormal ls written to temp_listls_abnormal_SprII.txt
# -------------------------------------------------------------
6th step
Handle 46 remaining abnormals manually

# generate the prototype changes.
python make_change_ls.py x temp_pwg_01.txt temp_change_x.txt

; <L>94861<pc>6-1327<k1>vfdDacARakya
<ls>Spr. (II) Vorwort S. XVI.</ls>

; <L>97703<pc>7-0056<k1>Satruka<k2>Satruka
<ls>Spr. (II)</ls> {#yaM dfzwvA varDate kroDaH#} .

; <L>110848<pc>7-1091<k1>suBAzita
<ls>Spr. (II) Th. 1, S. XV.</ls>

; <L>97703<pc>7-0056<k1>Satruka
<ls>Spr. (II)</ls> {#yaM dfzwvA varDate kroDaH#} .
<ls>Spr. (II) 5299</ls> {#yaM dfzwvA varDate kroDaH#} .
  print change
  
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
 1022 lines changed

python listls_abnormal.py 'Spr. (II)' temp_pwg_01.txt temp_listls_abnormal_SprII.txt

5011 ls instances of type 1a
57 ls instances of type 1b
237 ls instances of type 1c
1528 ls instances of type 2a
40 ls instances of type 2b
67 ls instances of type 2c
totals= 6940

9 abnormal ls written to temp_listls_abnormal_SprII.txt
<ls>Spr. (II) 4111, N.</ls> satyavAcaka 104150
<ls n="Spr. (II)">4977, N.</ls> satyavAdin 104153
<ls>Spr. (II) 4111, N.</ls> sadAkArin 104296
<ls>Spr. (II) 6841, N.</ls> hayaSAstra 116065
<ls>Spr. (II) 7265; vgl. N.</ls> kfpAlutA 119576
<ls>Spr. (II) 2533, N.</ls> bAhya 121285
<ls>Spr. (II) 5249, N.</ls> rUpasanAtana 121798
These two cannot be linked
<ls>Spr. (II) Vorwort S. XVI.</ls> vfdDacARakya 94861
<ls>Spr. (II) Th. 1, S. XV.</ls> suBAzita 110848 

# -------------------------------------------------------------
install temp_pwg_01.txt into csl-orig.

cp temp_pwg_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'

Make csl-websanlexicon changes to refer to web1.

cp temp_pwg.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
# -------------------------------------------------------------
python listls_instances.py 'Spr. (II)' temp_pwg_01.txt listls_instances_SprII.txt

6949 instances written to listls_instances_SprII.txt
NOTE: the 'verse' is set to '0' for the 2 that don't have links (see above)


# The next run shows that the markup changes increase the number of
# linkable verse from 5308 to the 6949 after changes.
python listls_instances.py 'Spr. (II)' temp_pwg_00.txt temp_listls_instances_SprII_00.txt
5308 instances written to temp_listls_instances_SprII_00.txt
