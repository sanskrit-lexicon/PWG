PWG/pwg_ls2/mbh2

Similar to pwg_ls2/hariv, but for MBH.


Refer:
 https://github.com/sanskrit-lexicon/PWG/issues/51

Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  e7b301b97d935d49b020ef3db98ab1f62fba358f
  
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pwg_00.txt in this spruch directory
  git show e7b301b:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/mbh2/temp_pwg_00.txt
# return to this mbh2 directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/mbh2/
# -------------------------------------------------------------
Focus on ls of form '<ls>MBH...</ls>'
Also handle those such as '<ls n="MBH."'
39096 matches in 39015 lines for "<ls>MBH\." in buffer: temp_pwg_00.txt
16745 matches in 8475 lines for "<ls n="MBH\." in buffer: temp_pwg_00.txt
0 matches for " MBH\." in buffer: temp_pwg_00.txt

# -------------------------------------------------------------
cp temp_pwg_00.txt temp_pwg_01.txt
We will manually add changes contained in change_01.txt to update
 temp_pwg_01.txt.


python listls_abnormal.py 'MBH.' temp_pwg_00.txt temp_abnormal_mbh_00.txt

56 abnormal ls written to temp_abnormal_mbh_00.txt
NORMAL:
37696 ls instances of type 1a
854 ls instances of type 1b
26 ls instances of type 1c
452 ls instances of type 1d
23 ls instances of type 1e
9577 ls instances of type 2a
302 ls instances of type 2b
6528 ls instances of type 2d
326 ls instances of type 2e
totals= 55784

# generate prototype change transactions for abnormals
python change_abnormal.py 'MBH.' temp_pwg_01.txt temp_change_abnormal.txt

edit temp_change_abnormal.txt, and insert into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
31 changes
# rerun listls_abnormal
python listls_abnormal.py 'MBH.' temp_pwg_01.txt temp_abnormal_mbh_01.txt

28 abnormal ls written to temp_abnormal_mbh_01.txt
37711  1a <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  854  1b <ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>  
   26  1c <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>  
  456  1d <ls>MBH.</ls> 
   23  1e <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls> 
 9587  2a <ls n="MBH.">([0-9]+), ([0-9]+[.]?)</ls> 
  303  2b <ls n="MBH.">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>  
    0  2c <ls n="MBH.">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>  
 6534  2d <ls n="MBH. ([0-9]+),">([0-9]+[.]?)</ls> 
  326  2e <ls n="MBH. ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>  
    0 2f <ls n="MBH. ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>  
totals 55820

3 incomplete <ls>MBH. added to change_01
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt


; ==================================================
python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_01.txt
4671 records written to temp_change2_01.txt 
   5 changes deferred.

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
4702 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_02.txt
; <ls>X, Y.</ls> -> <ls n="MBH.">X, Y.</ls>  ('.' is optional)
; '^<ls>([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>'
82 changes. insert into change_02.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
4784 lines changed.


python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_03.txt
; <ls>X, Y.</ls> -> <ls n="MBH.">X, Y.</ls>  ('.' is optional)
; '^<ls>([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>'
; r'^<ls>([0-9]+[.]?)</ls>$'
1744 changes not yet done. See tempdbg.txt
5 changes deferred
1767 records written to temp_change2_03.txt

#insert temp_change2_03 into change_01.
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
6551 change transactions from change_01.txt



python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_04.txt
; <ls>X, Y.</ls> -> <ls n="MBH.">X, Y.</ls>  ('.' is optional)
; '^<ls>([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>'
; r'^<ls>([0-9]+[.]?)</ls>$'
; '^<ls>([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>$'
1690 changes not yet done. See tempdbg.txt
1 changes deferred
58 records written to temp_change2_04.txt

# insert temp_change2_04.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
6609 change transactions from change_01.txt


python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_05.txt
; <ls>X, Y.</ls> -> <ls n="MBH.">X, Y.</ls>  ('.' is optional)
; '^<ls>([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>'
; r'^<ls>([0-9]+[.]?)</ls>$'
; '^<ls>([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>$'
; '^<ls>([0-9]+,) ([0-9]+[.]) ([0-9].*$)'
707 changes not yet done. See tempdbg.txt
1 changes deferred
979 records written to temp_change2_05.txt

# insert temp_change2_05.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
7588 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06.txt
; <ls>X, Y.</ls> -> <ls n="MBH.">X, Y.</ls>  ('.' is optional)
; '^<ls>([0-9]+,) ([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>'
; r'^<ls>([0-9]+[.]?)</ls>$'
; '^<ls>([0-9]+[.]) ((fgg?\.)|(v\. l\.))</ls>$'
; '^<ls>([0-9]+,) ([0-9]+[.]) ([0-9].*$)'
; '^<ls>([0-9]+[.]) ([0-9].*$)'
201 changes not yet done. See tempdbg.txt
2 changes deferred
1483 records written to temp_change2_06.txt

# insert temp_change2_06.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9071 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06a.txt
; same rules as for 06 above
219 changes not yet done. See tempdbg.txt
1 changes deferred
839 records written to temp_change2_06a.txt

# insert temp_change2_06a.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9910 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06b.txt
; same rules as for 06 above
325 records written to temp_change2_06b.txt

# insert temp_change2_06b.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10235 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06c.txt
; same rules as for 06 above
156 records written to temp_change2_06c.txt

# insert temp_change2_06c.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10391 change transactions from change_01.txt


python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06d.txt
; same rules as for 06 above
82 records written to temp_change2_06d.txt

# insert temp_change2_06d.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10473 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06e.txt
; same rules as for 06 above
42 records written to temp_change2_06d.txt

# insert temp_change2_06e.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10515 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06f.txt
22 records written to temp_change2_06f.txt

# insert temp_change2_06f.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10537 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06g.txt
13 records written to temp_change2_06g.txt

# insert temp_change2_06g.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10550 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06h.txt
10 records written to temp_change2_06h.txt

# insert temp_change2_06h.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10560 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06i.txt
4 records written to temp_change2_06i.txt

# insert temp_change2_06i.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10564 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp_change2_06j.txt
1 records written to temp_change2_06j.txt

# insert temp_change2_06j.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10565 change transactions from change_01.txt

# Try one more time --
python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp.txt
 0 CHANGES

232 changes not yet done. See tempdbg.txt
Handle these separately
tempdbg_edit.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10797 change transactions from change_01.txt

python make_change2_ls.py 'MBH.' temp_pwg_01.txt temp.txt
5
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
10900


python listls_abnormal.py 'MBH.' temp_pwg_01.txt abnormal_mbh_01.txt

NORMAL:
37711  1a <ls>MBH. ([0-9]+), ([0-9]+[.]?)</ls>
  854  1b <ls>MBH. ([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>  
   26  1c <ls>MBH. ([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>  
  457  1d <ls>MBH.</ls> 
   23  1e <ls>MBH.[^<]*ed[.] Bomb[.].*?</ls> 
16942  2a <ls n="MBH.">([0-9]+), ([0-9]+[.]?)</ls> 
  433  2b <ls n="MBH.">([0-9]+), ([0-9]+[.]?) fgg?[.]</ls>  
    3  2c <ls n="MBH.">([0-9]+), ([0-9]+[.,]?) v[.] l[.]</ls>  
 9902  2d <ls n="MBH. ([0-9]+),">([0-9]+[.]?)</ls> 
  427  2e <ls n="MBH. ([0-9]+),">([0-9]+[.]?) fgg?[.]</ls>  
    0  2f <ls n="MBH. ([0-9]+),">([0-9]+[.,]?) v[.] l[.]</ls>  
totals= 66778
33 abnormal ls written to abnormal_mbh_01.txt

# -------------------------------------------------------------
install temp_pwg_01.txt into csl-orig.

cp temp_pwg_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/mbh2

# -------------------------------------------------------------
python ../mbh1/lsextract_all.py temp_pwg_01.txt ../mbh1/pwg_tooltip.txt lsextract_pwg.txt


; -----------------------------------------------
misc text for copy/paste manual changes
</ls> <ls>
</ls> <ls n="MBH.">
</ls> <ls n="MBH.">
<ls n="MBH. ,">
<ls n="R.">
</ls> <ls n="ṚV.">
</ls> <ls n="MBH.">
</ls> <ls n="P.">
</ls> <ls n="M.">

</ls> <ls n="AV.">

<ls\([^>]*>[^<]*\)</ls> → LSBEG\1LSEND

\(\(<ls n="MBH..*?">.*?</ls>\)\|\(<ls>MBH..*?</ls>\)\) +\(\(<ls n="MBH..*?">.*?</ls>\)\|\(<ls>MBH..*?</ls>\)\)

\(\(\(<ls n="MBH.[^"]*">[^<]*</ls>\)\|\(<ls>MBH.[^<]*</ls>\)\) *\)\{2,99\}
