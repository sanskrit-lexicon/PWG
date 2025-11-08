
issue124fix

cp temp_sch_0.txt temp_sch_1.txt

---------------------------------------------
# VS. corresponds to linktarget
sch VS. ([0-9]+),([0-9]+),

Other refs starting with 'VS.' (these excluded in further analysis)
2 matches for "VS. Prāt."

python lsfix2.py sch temp_sch_0.txt lsfix2_sch_0.txt
(True,11),(all,11) lsfix2_sch_0.txt

===========================================

chkidx compares the kosha references and the link target index.

lsfix3.py is variation of lsfix2.py.  It prepares the input to chkidx.

python lsfix3.py sch temp_sch_0.txt lsfix3_sch_0.txt
(True,11),(all,11) lsfix3_sch_0.txt

cp ../issue124/index.txt  index.txt

# modify chkidx.py (Pagerec) for this kosha

python chkidx.py lsfix3_sch_0.txt index.txt lsfix3_chkidx_sch_0.txt
11 instances find ipage out of 11
0 references NOT FOUND in index

