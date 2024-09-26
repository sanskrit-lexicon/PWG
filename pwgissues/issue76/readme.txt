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
 e.g. a꣫ -> a/
Also a few unbalanced parens noticed and changed.
See the 'replacements_data' in the program for details.
cd transcode
python make_vntxt_1.py ../vntxt_0.txt ../vntxt_1.txt

--------------------------------------------------------
