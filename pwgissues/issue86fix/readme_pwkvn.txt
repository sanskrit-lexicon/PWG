issue86fix/readme_pwkvn.txt
09-29-2025 begun ejf
fix pwkvn references to  Pa�catantra, Kosegarten, 1848  

--------------------------------------
forms of reference:
 pwkvn: 
  PA�CAT. N,N  : ipage, linenum
  PA�CAT. R,N  : tantra, verse  R is roman numeral. I,II,III,IV,V
  Pa�cat. Pr. N : prastava N = verse

We use lsfix2_r1.py, with parmfile lsfix2_parm.py
 This version handles both N,N and R,N.
 It is specific to PA�CAT.

============================================================
# split work for pwkvn
python lsfix2_r1.py pwkvn2 temp_pwkvn_0.txt lsfix2_pwkvn2_0_r1.txt
(True,37),(all,37) lsfix2_pwkvn2_0_r1.txt

 So there is nothing to do for pwkvn
