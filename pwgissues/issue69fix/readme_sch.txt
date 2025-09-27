
issue69fix

sch link forms:
Verz. d. Oxf. H. ([0-9]+)

python lsfix2_alt.py 14 pw temp_sch_0.txt lsfix2_sch_0.txt
(None,25),(True,1),(all,26) 14 lsfix2_sch_0.txt

The None cases are due to a slight difference between sch and pwg/pw
sch: "141, a,20."
pwg: "141,a,20."
The link uses only the number 141 (in either sch or pwg/pw).
Thus for purpose of links, both sch and pwg/pw are equivalent

No changes needed.

====================================================
