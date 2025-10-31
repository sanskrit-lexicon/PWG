
issue84fix

pwkvn link forms:
ŚAT. BR. 4 parms

python lsfix2.py pwkvn temp_pwkvn_0.txt lsfix2_pwkvn_0.txt
(True,125),(all,125) lsfix2_pwkvn_0.txt

===========================================
 Find some invalid references

python lsfix3.py pwkvn temp_pwkvn_0.txt lsfix3_pwkvn_0.txt
(True,125),(all,125) lsfix3_pwkvn_0.txt

python chkidx.py lsfix3_pwkvn_0.txt SAT.index_edit.txt lsfix3_chkidx_pwkvn_0.txt
125 instances find ipage out of 125
 All references consistent with index

Nothing more to do!
