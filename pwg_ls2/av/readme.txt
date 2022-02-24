PWG/pwg_ls2/av


Similar to pwg_ls2/av, but for Atharva Veda  (AV.)


Refer:
 https://github.com/sanskrit-lexicon/PWG/issues/51

Start with a copy of csl-orig/v02/pwg/pwg.txt at commit
  6679ae1b71bbe4a9d9f773e7a301b572e5f5cff6
  
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_pwg_00.txt in this spruch directory
  git show 6679ae1b7:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/av/temp_pwg_00.txt
# return to this av directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/av/
# -------------------------------------------------------------
Focus on ls of form '<ls>AV...</ls>'
Also handle those such as '<ls n="AV."'
9961 matches in 9934 lines for "<ls>AV\." in buffer: temp_pwg_00.txt
190 matches in 123 lines for "<ls n="AV\." in buffer: temp_pwg_00.txt

163 matches in 102 lines for "<ls n="AV. PRĀT\." in buffer: temp_pwg_00.txt
9 matches for "<ls>AV. ANUKR\." in buffer: temp_pwg_00.txt

# -------------------------------------------------------------
cp temp_pwg_00.txt temp_pwg_01.txt
We will manually add changes contained in change_01.txt to update
 temp_pwg_01.txt.

# -------------------------------------------------------------


python listls3_abnormal.py 'AV.' temp_pwg_00.txt temp_abnormal_av_00.txt temp_change_abnormal.txt

2643 abnormal ls written to temp_abnormal_av_00.txt
2643 change transactions temp_change_abnormal.txt
    98 <ls n="AV. PRĀT. #, ">#.</ls>
    65 <ls n="AV. PRĀT.">#, #.</ls>
     2 <ls n="AV[.] #, #,">#.</ls>
     3 <ls n="AV[.] #,">#, #.</ls>
    19 <ls n="AV[.]">#, #, #.</ls>
     3 <ls>AV. ANUKR. #, #.</ls>
     5 <ls>AV. ANUKR.</ls>
   516 <ls>AV. PRĀT\. #, #.</ls>
    11 <ls>AV. PRĀT\.</ls>
    52 <ls>AV[.] #, #, #. fgg.</ls>
     4 <ls>AV[.] #, #, #. v. l.</ls>
  6559 <ls>AV[.] #, #, #.</ls>
   171 <ls>AV[.]</ls>
totals= 7508

------------------------------------------------
python make_change3_abnormal.py 'AV.' temp_pwg_00.txt temp_change3_abnormal.txt
2251 records written to temp_change3_abnormal.txt

# insert temp_change3_abnormal.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
2251 change transactions from change_01.txt

python listls3_abnormal.py 'AV.' temp_pwg_01.txt temp_abnormal_av_01.txt temp_change_abnormal_01.txt

1088 abnormal ls written to temp_abnormal_av_01.txt
1088 change transactions temp_change_abnormal_01.txt
     2 <ls n="AV[.] #, #,">#.</ls>
     3 <ls n="AV[.] #,">#, #.</ls>
    19 <ls n="AV[.]">#, #, #.</ls>
    52 <ls>AV[.] #, #, #. fgg.</ls>
     4 <ls>AV[.] #, #, #. v. l.</ls>
  8812 <ls>AV[.] #, #, #.</ls>
   171 <ls>AV[.]</ls>
totals= 9063

# Manual changes from temp_change_abnormal_01.txt inserted into change_01
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
2459 change transactions

------------------------------------------------
python listls3_abnormal.py 'AV.' temp_pwg_01.txt temp_abnormal_av_02.txt temp_change_abnormal_02.txt
97 abnormal ls written to temp_abnormal_av_02.txt
WARNING DBG: write_abnormals_change skipping some
66 change transactions temp_change_abnormal_02.txt

# Manual changes from temp_change_abnormal_02.txt inserted into change_01
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
2503 change transactions

------------------------------------------------
python listls3_abnormal.py 'AV.' temp_pwg_01.txt temp_abnormal_av_03.txt temp_change_abnormal_03.txt
54 abnormal ls written to temp_abnormal_av_03.txt
WARNING DBG: write_abnormals_change skipping some
23 change transactions temp_change_abnormal_03.txt
NORMAL
    98 <ls n="AV. PRĀT. #, ">#.</ls>
    65 <ls n="AV. PRĀT.">#, #.</ls>
     3 <ls n="AV[.] #, #,">#.</ls>
     3 <ls n="AV[.] #,">#, #.</ls>
    22 <ls n="AV[.]">#, #, #.</ls>
     3 <ls>AV. ANUKR. #, #.</ls>
     5 <ls>AV. ANUKR.</ls>
    18 <ls>AV. PARIŚ\. #, #.</ls>
     4 <ls>AV. PARIŚ\. #.</ls>
   121 <ls>AV. PARIŚ\.</ls>
   517 <ls>AV. PRĀT\. #, #.</ls>
    22 <ls>AV. PRĀT\.</ls>
    71 <ls>AV[.] #, #, #. fgg.</ls>
     4 <ls>AV[.] #, #, #. v. l.</ls>
  8968 <ls>AV[.] #, #, #.</ls>
   174 <ls>AV[.]</ls>
totals = 10098
# --------------------------------------------------------
Now begin to add markup for ca
------------------------------------------------

python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_01.txt
50 changes not yet done. See tempdbg.txt
15 changes deferred
4011 records written to temp_change3_01.txt

# insert temp_change3_01.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
6514 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_02.txt
68 changes not yet done. See tempdbg.txt
7 changes deferred
1462 records written to temp_change3_02.txt

# insert temp_change3_02.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
7976 change transactions from change_01.txt


------------------------------------------------

python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_03.txt
# also some other forms.
76 changes not yet done. See tempdbg.txt
5 changes deferred
658 records written to temp_change3_03.txt

#insert temp_change3_03 into change_01.
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
8634 change transactions from change_01.txt

# edit tempdbg.txt and insert several more changes into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
8674 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_04.txt
8 changes not yet done. See tempdbg.txt
12 changes deferred
353 records written to temp_change3_04.txt


#insert temp_change3_04 into change_01.
# also a couple from tempdbg.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9028 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_05.txt
3 changes not yet done. See tempdbg.txt
3 changes deferred
137 records written to temp_change3_05.txt


#insert temp_change3_05 into change_01.
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9168 change transactions from change_01.txt


------------------------------------------------

python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_06.txt
0 changes not yet done. See tempdbg.txt
2 changes deferred
76 records written to temp_change3_06.txt

# insert temp_change3_06.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9244 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_07.txt

# insert temp_change3_07.txt into change_01.txt
0 changes not yet done. See tempdbg.txt
1 changes deferred
44 records written to temp_change3_07.txt

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9288 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_08.txt
0 changes not yet done. See tempdbg.txt
1 changes deferred
20 records written to temp_change3_08.txt


# insert temp_change3_08.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9308 change transactions from change_01.txt

------------------------------------------------

python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_09.txt
0 changes not yet done. See tempdbg.txt
1 changes deferred
10 records written to temp_change3_09.txt


# insert temp_change3_09.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9318 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_10.txt
0 changes not yet done. See tempdbg.txt
1 changes deferred
6 records written to temp_change3_10.txt

# insert temp_change3_10.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9324 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_11.txt
0 changes not yet done. See tempdbg.txt
1 changes deferred
5 records written to temp_change3_11.txt


# insert temp_change3_11.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9329 change transactions from change_01.txt


------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_12.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
2 records written to temp_change3_12.txt

# insert temp_change3_12.txt into change_01.txt
# remove 31 transactions that have an error in handling of 'fg.'
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9300 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_13.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
31 records written to temp_change3_13.txt

# insert temp_change3_13.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9331 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_14.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
31 records written to temp_change3_14.txt


# insert temp_change3_14.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9362 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_15.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
16 records written to temp_change3_15.txt


# insert temp_change3_15.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9378 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_16.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
7 records written to temp_change3_16.txt


# insert temp_change3_16.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9385 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_17.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
4 records written to temp_change3_17.txt


# insert temp_change3_17.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9389 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_18.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
2 records written to temp_change3_18.txt

# insert temp_change3_18.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9391 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_19.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
2 records written to temp_change3_19.txt

# insert temp_change3_19.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9393 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_20.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
2 records written to temp_change3_20.txt

# insert temp_change3_20.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9395 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_21.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
1 records written to temp_change3_21.txt

# insert temp_change3_21.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9396 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_22.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
1 records written to temp_change3_22.txt

# insert temp_change3_22.txt into change_01.txt
python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt
9397 change transactions from change_01.txt

------------------------------------------------
python make_change3_ls.py 'AV.' temp_pwg_01.txt temp_change3_23.txt
0 changes not yet done. See tempdbg.txt
0 changes deferred
0 records written to temp_change3_23.txt

DONE!!

------------------------------------------------

python ../01/updateByLine.py temp_pwg_00.txt change_01.txt temp_pwg_01.txt


------------------------------------------------
python listls3_abnormal.py 'AV.' temp_pwg_01.txt abnormal_av_01.txt change_abnormal.txt

48 abnormal ls written to abnormal_av_01.txt
48 change transactions change_abnormal.txt
    98 <ls n="AV. PRĀT. #, ">#.</ls>
    65 <ls n="AV. PRĀT.">#, #.</ls>
     9 <ls n="AV[.] #, #,">#. fgg.</ls>
  1011 <ls n="AV[.] #, #,">#.</ls>
    14 <ls n="AV[.] #,">#, #. fgg.</ls>
   959 <ls n="AV[.] #,">#, #.</ls>
    62 <ls n="AV[.]">#, #, #. fgg.</ls>
  4830 <ls n="AV[.]">#, #, #.</ls>
     3 <ls>AV. ANUKR. #, #.</ls>
     5 <ls>AV. ANUKR.</ls>
     3 <ls>AV. PAR.</ls>
     2 <ls>AV. PARIŚ. #, #, #.</ls>
    18 <ls>AV. PARIŚ. #, #.</ls>
     4 <ls>AV. PARIŚ. #.</ls>
   121 <ls>AV. PARIŚ.</ls>
   517 <ls>AV. PRĀT. #, #.</ls>
    22 <ls>AV. PRĀT\.</ls>
    72 <ls>AV[.] #, #, #. fgg.</ls>
     4 <ls>AV[.] #, #, #. v. l.</ls>
  8968 <ls>AV[.] #, #, #.</ls>
   174 <ls>AV[.]</ls>
totals= 16961

python ../mbh1/lsextract_all.py temp_pwg_01.txt ../mbh1/pwg_tooltip.txt lsextract_pwg.txt
 Before: 09283	AV. links
 After : 16149  AV. links



# -------------------------------------------------------------
install temp_pwg_01.txt into csl-orig.

cp temp_pwg_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/av

# -------------------------------------------------------------


; -----------------------------------------------
misc text for copy/paste manual changes
</ls> <ls>
</ls> <ls n="AV.">
</ls> <ls n="AV.">
<ls n="AV. ,">
<ls n="R.">
</ls> <ls n="AV.">
</ls> <ls n="AV.">
</ls> <ls n="P.">
</ls> <ls n="M.">

</ls> <ls n="AV.">

<ls\([^>]*>[^<]*\)</ls> → LSBEG\1LSEND

\(\(<ls n="AV..*?">.*?</ls>\)\|\(<ls>AV..*?</ls>\)\) +\(\(<ls n="AV..*?">.*?</ls>\)\|\(<ls>AV..*?</ls>\)\)

\(\(\(<ls n="AV.[^"]*">[^<]*</ls>\)\|\(<ls>AV.[^<]*</ls>\)\) *\)\{2,99\}
