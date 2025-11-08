
issue124fix

cp temp_pwkvn_0.txt temp_pwkvn_1.txt

---------------------------------------------
# VS. corresponds to linktarget
pwkvn VS. ([0-9]+),([0-9]+),

Other refs starting with 'VS.' (these excluded in further analysis)
2 matches for "VS. PRĀT."

python lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt
(True,11),(all,11) lsfix2_pwkvn_0.txt

python lsfix3.py pwkvn temp_pwkvn_0.txt lsfix3_pwkvn_0.txt
(True,11),(all,11) lsfix3_pwkvn_0.txt

python chkidx.py lsfix3_pwkvn_0.txt index.txt lsfix3_chkidx_pwkvn_0.txt
167 instances find ipage out of 167
0 references NOT FOUND in index
