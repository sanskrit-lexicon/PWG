09-25-2024
issue: https://github.com/sanskrit-lexicon/PWG/issues/76

# This directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue76

# starting point for vntxt digitization of missing VN material.
https://github.com/user-attachments/files/17129810/PWGVN_1-6_reformatted_.dng.txt

# local copy rename
mv PWGVN_1-6_reformatted_.dng.txt vntxt_0_deva_orig.txt
cp vntxt_0_deva_orig.txt vntxt_0_deva.txt


# transcode
mkdir transcode
cd transcode
python mark_deva.py ../vntxt_0_deva.txt vntxt_0_deva_marked.txt
637 lines read from ../vntxt_0_deva.txt
637 lines written to vntxt_0_deva_marked.txt
Devanagari text has been marked and saved to vntxt_0_deva_marked.txt

Note: This step unnecessary!!  AB has alread marked Devanagari as {#X#},
 which is the pwg convention.
rm vntxt_0_deva_marked.txt

# transcode
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue76/transcode
mkdir pwgtranscoder1
cp /c/xampp/htdocs/sanskrit-lexicon/MWS/mwtranscode/transcoder1/deva_slp1.xml pwgtranscoder1/deva_slp1.xml
cp /c/xampp/htdocs/sanskrit-lexicon/MWS/mwtranscode/transcoder1/slp1_deva.xml pwgtranscoder1/slp1_deva.xml

cp /c/xampp/htdocs/sanskrit-lexicon/MWS/mwtranscode/transcoder.py .
cp /c/xampp/htdocs/sanskrit-lexicon/MWS/mwtranscode/mw_transcode.py pwg_transcode.py

# heavily edit pwg_transcode.py

-----------------
Transcode
# Some editing of vntxt_0_deva.txt related to transcoding to get invertibility
See change_vntxt_0_deva.txt

python pwg_transcode.py pwgtranscoder1 deva slp1 ../vntxt_0_deva.txt ../vntxt_0.txt
# check invertibility
python pwg_transcode.py pwgtranscoder1 slp1 deva ../vntxt_0.txt tempchk.txt
diff ../vntxt_0_deva.txt tempchk.txt | wc -l
0  # invertibility checks.

commit repo and sync to github.
--------------------------------------------------------------

The transcoding mishandled the udAtta accent (and maybe others?)
 Correct several errors. Mostly the Devanagari combining U change to /
 e.g. aÃªÂ£Â« -> a/
Also a few unbalanced parens noticed and changed.
See the 'replacements_data' in the program for details.
cd transcode
python make_vntxt_1.py ../vntxt_0.txt ../vntxt_1.txt

--------------------------------------------------------
09-27-2024
Redo transcoding using the pwg slp1_deva1.xml.
Main task is to create an 'inverse' transcoder deva1_slp1.xml.
Do this in a 'transcodepwg' directory

mkdir transcodepwg
cd transcodepwg
mkdir pwgtranscoder2
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva1.xml pwgtranscoder2/slp1_deva1.xml
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/deva_slp1.xml pwgtranscoder2/deva_slp1.xml

# also copy slp1_deva.xml for reference:
cp /c/xampp/htdocs/cologne/csl-websanlexicon/v02/makotemplates/web/utilities/transcoder/slp1_deva.xml pwgtranscoder2/slp1_deva.xml

Of course, deva_slp1.xml was constructed as an inverse for the non-pwg version slp1_deva.xml.
But we need an inverse for the pwg version slp1_deva1.xml.
We will call this inverse deva1_slp1.xml.
It starts as a copy of deva_slp1.xml:
cp pwgtranscoder2/deva_slp1.xml pwgtranscoder2/deva1_slp1.xml
# Manually edit pwgtranscoder2/deva1_slp1.xml

cd pwgtranscoder2
diff slp1_deva.xml slp1_deva1.xml > diff_slp1_deva_deva1.txt

name    slp1  deva      deva1
anudAtta \    u0952     u0952
udAtta   /    u0951     ua8eb  
svarita  ^    u1ce0     u0951

python make_deva1_slp1.py pwgtranscoder2/deva_slp1.xml pwgtranscoder2/deva1_slp1.xml
 a) u0951 -> ua8eb
 b) u1ce0 -> u095a
In addition, manually add the 'special rules ...' section at end of
deva1_slp1.xml.

-------------------------------------------------------
# We want to apply the deva1 transcoding to AB's file.
We had previously used a slightly modified version of AB's file:
  ../vntxt_0_deva.txt (his original file being ../vntxt_0_deva_orig.txt)
However, one of the changes in this file is not needed,
  namely {#रााण꣫#} -> {#राण॑#}  is removed.

In following work will use this as AB version:
  ../vntxt_0_deva_rev.txt
whose changes are noted in change_vntxt_0_deva_rev.txt
  Note: this also corrects a few typos in AB original file.

-------------------------------------------------------
cd transcodepwg
# construct slp1 version ../vntxt_1_rev.txt  from ../vntxt_0_deva_rev.txt
# use the deva1 transcoder files (slp1_deva1.xml and deva1_slp1.xml).
#  these transcoder files are in pwgtranscoder2 sub-directory.

python pwg_transcode.py pwgtranscoder2 deva1 slp1 ../vntxt_0_deva_rev.txt ../vntxt_1_rev.txt
# check invertibility 
python pwg_transcode.py pwgtranscoder2 slp1 deva1 ../vntxt_1_rev.txt tempchk.txt
diff ../vntxt_0_deva_rev.txt tempchk.txt | wc -l
0  # invertibility checks.

# compare to previous vntxt_1.
diff ../vntxt_1.txt ../vntxt_1_rev.txt  > ../diff_vntxt_1-1_rev.txt
64 lines in diff file (so 16 lines changed).
These are corrections to some accents which were incorrect in vntxt_1.txt.

# as a further check, examine the extended ascii charactersin vntxt_1_rev.txt
cd ../
python check_ea.py vntxt_1_rev.txt check_ea_vntxt_1_rev.txt
  Note no Devanagari characters!

conclusion:
vntxt_1_rev.txt looks ok to Jim
----------------------------------------------------------
