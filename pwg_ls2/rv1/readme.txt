PWG/pwg_ls2/rv1


Similar to pwg_ls2/mbh2, but for rv  (ṚV.)


Refer:
 https://github.com/sanskrit-lexicon/PWG/issues/?

Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  9a606a70805a950ebdb42bbf44c1c1c4599a7358
  
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pwg_00.txt in this spruch directory
  git show 9a606a7:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/rv1/temp_pwg_00.txt
# return to this rv1 directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/rv1/
# -------------------------------------------------------------
Focus on ls of form '<ls>ṚV...</ls>'
Also handle those such as '<ls n="ṚV."'
20110 matches in 20048 lines for "<ls>ṚV\." in buffer: temp_pwg_00.txt
36106 matches in 21381 lines for "<ls n="ṚV\." in buffer: temp_pwg_00.txt
1 match for "<ls n="ṚV. PRĀTIŚ." in buffer: temp_pwg_00.txt
9 matches for "<ls>ṚV. PRĀTIŚ." in buffer: temp_pwg_00.txt
158 matches for "<ls>ṚV. ANU" in buffer: temp_pwg_00.txt

<ls>ṚV. ANUKRAMAṆIKĀ.*?</ls>
<ls>ṚV. ANUKR..*?</ls>
# -------------------------------------------------------------
cp temp_pwg_00.txt temp_pwg_01.txt
We will manually add changes contained in change_01.txt to update
 temp_pwg_01.txt.


python listls3_abnormal.py 'ṚV.' temp_pwg_00.txt temp_abnormal_rv_00.txt temp_change_abnormal.txt
# cp temp_change_abnormal.txt temp_change_abnormal_edit.txt
# manually edit temp_change_abnormal_edit.txt
# cp temp_change_abnormal_edit.txt change_01.txt
# intall changes into temp_pwg_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
122 changes

python listls3_abnormal.py 'ṚV.' temp_pwg_01.txt temp_abnormal_rv_00.txt temp_change_abnormal.txt

149413 lines read from temp_pwg_01.txt
122736 entries found
501 abnormal ls written to temp_abnormal_rv_00.txt
21 change transactions temp_change_abnormal.txt
   260 <ls n="ṚV. PRĀT. #, ">#.</ls>
   287 <ls n="ṚV. PRĀT.">#, #.</ls>
     1 <ls n="ṚV. PRĀTIŚ. #, ">#.</ls>
  1774 <ls n="ṚV[.] #, #,">#.</ls>
    14 <ls n="ṚV[.] #,">#, #. fgg.</ls>
 10692 <ls n="ṚV[.] #,">#, #.</ls>
    25 <ls n="ṚV[.]">#, #, #. fgg.</ls>
 23111 <ls n="ṚV[.]">#, #, #.</ls>
   155 <ls>ṚV. ANUKR.</ls>
     1 <ls>ṚV. ANUKRAMAṆIKĀ.</ls>
     9 <ls>ṚV. PRĀTIŚ. #, #.</ls>
  1094 <ls>ṚV. PRĀT\. #, #.</ls>
    18 <ls>ṚV. PRĀT\.</ls>
     1 <ls>ṚV[.] #, #, #. fgg.</ls>
 18171 <ls>ṚV[.] #, #, #.</ls>
   276 <ls>ṚV[.]</ls>
totals= 55889

# --------------------------------------------------------

3 incomplete <ls>ṚV. added to change_01
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt


------------------------------------------------

python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_01.txt
; <ls>X, Y, Z.</ls> -> <ls n="ṚV.">X, Y, Z.</ls>  ('.' is optional)
179 records written to temp_change2_01.txt 
  9 changes deferred.
# insert temp_change3_01.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
304 change transactions from change_01.txt

python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_02.txt
; <ls>X, Y, Z.</ls> -> <ls n="ṚV.">X, Y, Z.</ls>  ('.' is optional)
; <ls>X, Y, Z. W</ls> -> <ls n="ṚV.">X, Y, Z. W</ls>  (W = fgg?. or v. l.)
9 changes. insert into change_01.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
313 lines changed.

------------------------------------------------

python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_03.txt
# also some other forms.
91 changes not yet done. See tempdbg.txt
10 changes deferred
191 records written to temp_change3_03.txt

#insert temp_change3_03 into change_01.
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
504 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_04.txt
76 changes not yet done. See tempdbg.txt
10 changes deferred
151 records written to temp_change3_04.txt

#insert temp_change3_04 into change_01.
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
655 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_05.txt
77 changes not yet done. See tempdbg.txt
8 changes deferred
108 records written to temp_change3_05.txt

#insert temp_change3_05 into change_01.
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
763 change transactions from change_01.txt


------------------------------------------------

python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_06.txt
88 changes not yet done. See tempdbg.txt
4 changes deferred
66 records written to temp_change3_06.txt


# insert temp_change3_06.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
829 change transactions from change_01.txt

------------------------------------------------
# manual changes from tempdbg.txt, insert into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
906 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_07.txt
18 changes not yet done. See tempdbg.txt
64 changes deferred
108 records written to temp_change3_07.txt

# insert temp_change3_07.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
1013 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_08.txt
8 changes not yet done. See tempdbg.txt
10 changes deferred
91 records written to temp_change3_08.txt

# insert temp_change3_08.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
1111 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_09.txt
2 changes not yet done. See tempdbg.txt
13 changes deferred
49 records written to temp_change3_09.txt

# insert temp_change3_09.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
1161 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_10.txt
2 changes not yet done. See tempdbg.txt
3 changes deferred
35 records written to temp_change3_10.txt

# insert temp_change3_10.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
1196 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_11.txt
1 changes not yet done. See tempdbg.txt.  Some problem here. Not RV.
; ---------------------------
; <L>20332<pc>2-0555<k1>kzipra
; prev = <ls>ṚV. 2, 24, 8.</ls>
; todo = <ls>1, 2, 1, 1</ls>
193642 old <ls>1, 2, 1, 1</ls>) <ls>TS. 3, 4, 3, 2.</ls> {#yadvE kzipraM tattUrtamaTa yatkziprAtkzepIyastatpratUrtam#} 

0 changes deferred
20 records written to temp_change3_11.txt

# insert temp_change3_11.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
1216 change transactions from change_01.txt


------------------------------------------------
python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_12.txt
2 changes not yet done. See tempdbg.txt
0 changes deferred
12 records written to temp_change3_12.txt

# insert temp_change3_12.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
1228 change transactions from change_01.txt


------------------------------------------------
python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_13.txt
2 changes not yet done. See tempdbg.txt
0 changes deferred
6 records written to temp_change3_13.txt

# insert temp_change3_13.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
1234 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_14.txt
1 changes not yet done. See tempdbg.txt
0 changes deferred
2 records written to temp_change3_14.txt

# insert temp_change3_14.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
1236 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_15.txt
1 changes not yet done. See tempdbg.txt
0 changes deferred
1 records written to temp_change3_15.txt

# insert temp_change3_15.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
1236 change transactions from change_01.txt

------------------------------------------------
------------------------------------------------
python make_change3_ls.py 'ṚV.' temp_pwg_01.txt temp_change3_16.txt

1 changes not yet done. See tempdbg.txt
0 changes deferred
0 records written to temp_change3_16.txt

WE ARE DONE!

------------------------------------------------
python listls3_abnormal.py 'ṚV.' temp_pwg_01.txt abnormal_rv_01.txt change_abnormal.txt

501 abnormal ls written to abnormal_rv_01.txt
501 change transactions change_abnormal.txt
   260 <ls n="ṚV. PRĀT. #, ">#.</ls>
   287 <ls n="ṚV. PRĀT.">#, #.</ls>
     1 <ls n="ṚV. PRĀTIŚ. #, ">#.</ls>
  1820 <ls n="ṚV[.] #, #,">#.</ls>
    14 <ls n="ṚV[.] #,">#, #. fgg.</ls>
 10985 <ls n="ṚV[.] #,">#, #.</ls>
    25 <ls n="ṚV[.]">#, #, #. fgg.</ls>
 23810 <ls n="ṚV[.]">#, #, #.</ls>
   155 <ls>ṚV. ANUKR.</ls>
     1 <ls>ṚV. ANUKRAMAṆIKĀ.</ls>
     9 <ls>ṚV. PRĀTIŚ. #, #.</ls>
  1094 <ls>ṚV. PRĀT\. #, #.</ls>
    18 <ls>ṚV. PRĀT\.</ls>
     1 <ls>ṚV[.] #, #, #. fgg.</ls>
 18171 <ls>ṚV[.] #, #, #.</ls>
   276 <ls>ṚV[.]</ls>
totals= 56927

So we have increased the number of linkable RV from 55889 to 56927,
1000+ additional.

# -------------------------------------------------------------
install temp_pwg_01.txt into csl-orig.

cp temp_pwg_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/rv1

# -------------------------------------------------------------
python ../mbh1/lsextract_all.py temp_pwg_01.txt ../mbh1/pwg_tooltip.txt lsextract_pwg.txt


; -----------------------------------------------
misc text for copy/paste manual changes
</ls> <ls>
</ls> <ls n="ṚV.">
</ls> <ls n="ṚV.">
<ls n="ṚV. ,">
<ls n="R.">
</ls> <ls n="ṚV.">
</ls> <ls n="ṚV.">
</ls> <ls n="P.">
</ls> <ls n="M.">

</ls> <ls n="AV.">

<ls\([^>]*>[^<]*\)</ls> → LSBEG\1LSEND

\(\(<ls n="ṚV..*?">.*?</ls>\)\|\(<ls>ṚV..*?</ls>\)\) +\(\(<ls n="ṚV..*?">.*?</ls>\)\|\(<ls>ṚV..*?</ls>\)\)

\(\(\(<ls n="ṚV.[^"]*">[^<]*</ls>\)\|\(<ls>ṚV.[^<]*</ls>\)\) *\)\{2,99\}
