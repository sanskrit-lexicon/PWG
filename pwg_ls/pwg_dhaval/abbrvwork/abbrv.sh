python abbrv0.py ../../../../pwgxml/pwg.xml abbrvoutput/abbrvlist.txt
python abbrv1.py abbrvoutput/abbrvlist.txt abbrvoutput/improperrefs.txt abbrvoutput/properrefs.txt
python abbrv2.py abbrvoutput/properrefs.txt abbrvoutput/cleanrefs.txt
python abbrv3.py abbrvoutput/properrefs.txt abbrvoutput/sortedcrefs.txt
