
issue149fix

pw link forms:
MĀLAV.  1 parm or 2 parms
<ls>MĀLAV. ([0-9]+),([0-9]+)

python lsfix2.py pw temp_pw_0.txt lsfix2_pw_0.txt

87 lines written to lsfix2_pw_0.txt
(True, 2) 33
(True, 1) 37
(None, 1) 16
('fixed', 2) 1

cp temp_pw_0.txt temp_pw_1.txt

Edit temp_pw_1.txt to resolve the None and False

10 of the None are other editions (Bollensen, Bombay, Calcutta)
 6 are of form like <ls>MĀLAV. 10,4 (11,1)</ls>.
   The displays catch link 10,4; the 11,1 link is to some other edition.
  
NO changes made.
