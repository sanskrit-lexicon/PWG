
Analysis of literary source abbreviations in PWG.
Revised to take into account particulars of PWG that were not 
present for PW.
This work is still based on pwg.xml.

02-28-2017  ejf

abbrv.sh
--------

abbrv0 generates abbrvlist.txt, all LS abbreviations, in order by headword
output consists of lines with '@' separated fields:
  Note we remove key2
  abbreviation text (contents of '<ls>'
  key1
  L-number

python abbrv0.py ../../../../pwgxml/pwg.xml abbrvoutput/abbrvlist.txt
10 sec.

abbrv1 separates abbrvlist into two parts, 
 proper references and 'improper' references
 In this version, we take a restrictive definition of 'proper' ref:
   the text of the 'LS' entry must start with a Capital letter A-Z.
   NOTE: This assumes the AS-coding , so for instance 
    'A10C2V. GR2HJ.' instead of the Roman spelling 'ĀŚV. GṚHY.'.


python abbrv1.py abbrvoutput/abbrvlist.txt abbrvoutput/improperrefs.txt abbrvoutput/properrefs.txt

abbrv2 generates an (unsorted) list of unique proper references (without counts)
python abbrv2.py abbrvoutput/properrefs.txt abbrvoutput/cleanrefs.txt

abbrv3 generates a sorted list of unique proper references, with counts
 fields are:
 cleaned abbrev Roman
 cleaned abbrev AS
 count

python abbrv3.py abbrvoutput/properrefs.txt abbrvoutput/sortedcrefs.txt

abbrv4
------
match sortedcrefs with pwbib14
python abbrv4.py abbrvoutput/sortedcrefs.txt ../../pwgbib/digitization/pwgbib14_roman.txt abbrvoutput/matchcrefs.txt


abbrv.sh
python abbrv0.py ../../../../pwgxml/pwg.xml abbrvoutput/abbrvlist.txt
python abbrv1.py abbrvoutput/abbrvlist.txt abbrvoutput/purenumberabbrvlist.txt abbrvoutput/properrefs.txt
python abbrv2.py abbrvoutput/properrefs.txt abbrvoutput/cleanrefs.txt
python abbrv3.py abbrvoutput/properrefs.txt abbrvoutput/sortedcrefs.txt
19:01:05
19:02:30
Elapsed time 1:25  (1 min. 25 sec.)


database
---------
This constructs a database:
  key = the text of ls elements for proper ls elements
        - text is NOT cleaned
        - text is in the form of PWG (i.e., currently AS-coding)
  value = The Roman abbreviation code, per pwgbib14_roman.txt
Reason: This table can be used by disp.php display program at Cologne
        to construct link to a display of pwgbib14_roman.txt

Choice:  The data input is pwg.xml.   We incorporate (by module inclusion)
  the various algorithms in abbrvX.py for:
  a) deciding if link is proper (abbrv1.py)
  b) constructing abbreviation via:
     - cleaning link text (abbrv3.py)
     - converting cleaned link text to Roman (abbrv3.py)
     - matching (abbrv4.py)

python pwgls.py ../../../../pwgxml/pwg.xml ../../pwgbib/digitization/pwgbib14_roman.txt pwgls.txt

pwgbib.txt
 Currently, a copy of ../../pwgbib/digitization/pwgbib14_roman.txt
