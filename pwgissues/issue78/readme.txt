10-06-2024
issue: https://github.com/sanskrit-lexicon/PWG/issues/78

# This directory
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue78

# proposed enhancement of slp1 transcoding for vowel-markers.

https://github.com/user-attachments/files/17129810/PWGVN_1-6_reformatted_.dng.txt

There is a 'special' transcoding of slp1 to Devanagari
that is used in dictionaries:  pwg, pw, sch, pwkvn
The transcoding files are slp1_deva1.xml and its inverse deva1_slp1.xml
We start with the versions of these two files in transcode0 directory.

The revision is in transcode1 directory.

python debug_transcode.py transcode1 slp1 deva1 test01_in.txt test01_out.txt
python debug_transcode.py transcode1 deva1 slp1 test01_out.txt test01_in_out.txt

test01_in_out.txt is different than test01_in.txt.
The invertibility fails.

Note that deva1_slp1.xml defines a finite-state machine with only one state,
  the INIT state.

