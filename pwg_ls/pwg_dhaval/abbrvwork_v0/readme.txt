
Analysis of literary source abbreviations in PWG.
02-28-2017  ejf

abbrv.py
--------
This code originally developed for PW. 
It was first run with minimal changes for PWG.
There are over 5 times as many LS sections in PWG as in PW; over 400,000.
A computational side effect is that it took about 1.5 HOURS to run abbrv.py
python abbrv.py ../../../../pwgxml/pwg.xml
From abbrv_log_timing.txt, here is timing of original (about 1.5hr as stated)
Begin: 21:53:10
  End: 23:22:10

The reason is believed to be related to the use of list operations on
the 400k long lists.
After the changes described below, the timing is 1m25sec (a factor of 60+):
(/ (* 1.5 60  60) (+ 60.0 25.0)) = 63.5


The first order of business is to change the code so it is more efficient.
Save a copy of the original code:
cp abbrv.py abbrv_orig.py

The code of abbrv.py operates in phases, with the results of previous
phases being shared with later phases via global variables.
It seems better to disaggregate these phases, so they can be optimized
independently.  The data of the global variables can be shared by
files.

abbrv0 generates abbrvlist.txt, all LS abbreviations, in order by headword
output consists of lines with '@' separated fields:
  abbreviation text (contents of '<ls>'
  key1
  key2
  L-number

python abbrv0.py ../../../../pwgxml/pwg.xml abbrvoutput/abbrvlist.txt
10 sec.

abbrv1 separates abbrvlist into two parts, 
 proper references and 'number' references
python abbrv1.py abbrvoutput/abbrvlist.txt abbrvoutput/purenumberabbrvlist.txt abbrvoutput/properrefs.txt

abbrv2 generates an (unsorted) list of unique proper references (without counts)
python abbrv2.py abbrvoutput/properrefs.txt abbrvoutput/cleanrefs.txt

abbrv3 generates a sorted list of unique proper references, with counts
python abbrv3.py abbrvoutput/properrefs.txt abbrvoutput/sortedcrefs.txt

abbrv.sh
python abbrv0.py ../../../../pwgxml/pwg.xml abbrvoutput/abbrvlist.txt
python abbrv1.py abbrvoutput/abbrvlist.txt abbrvoutput/purenumberabbrvlist.txt abbrvoutput/properrefs.txt
python abbrv2.py abbrvoutput/properrefs.txt abbrvoutput/cleanrefs.txt
python abbrv3.py abbrvoutput/properrefs.txt abbrvoutput/sortedcrefs.txt
19:01:05
19:02:30
Elapsed time 1:25  (1 min. 25 sec.)
