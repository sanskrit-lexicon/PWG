
issue169

pwg link forms:
2 parameters.
I have already made a change in temp_pwg_1.txt.

=====================
pwg RĀJA-TAR. ed. Calc N,N
pwga RĀJA-TAR. 7/8,N
pwgb RĀJAT. 7/8,N  (no examples in pwg)

====================
pwg RĀJA-TAR. ed. Calc N,N
python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt

cp temp_pwg_0.txt temp_pwg_1.txt

python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(True,11),(all,11) lsfix2_pwg_1.txt

check: pwg
mummuni	<ls n="RĀJA-TAR. ed. Calc.">8,2180.</ls>

====================
pwga RĀJA-TAR. 7/8,N

python lsfix2.py pwga temp_pwg_1.txt lsfix2_pwg_1_a.txt
(None,49),(True,10230),(all,10279) lsfix2_pwg_1_a.txt

check: pwga
vijayeSa	<ls n="RĀJA-TAR. 1,">105. fg.</ls>
durgaGAta	<ls n="RĀJA-TAR. 7,">1173</ls>  1175 (1173)
durgaGAta	<ls>RĀJA-TAR. 7,1175</ls>    NOT FOUND Could this be Kern?
simba	<ls>RĀJA-TAR. 8,1004.</ls>

28 matches in 27 lines for "[IV]+," in buffer: tempwork_lsfix2_pwg_1_a.txt
example: maRipUra	<ls>RĀJA-TAR. I,570</ls>

What are these ?

====================
pwgb RĀJAT. 7/8,N

python lsfix2.py pwgb temp_pwg_1.txt lsfix2_pwg_1_b.txt
(all,0) lsfix2_pwg_1_b.txt

No examples.


-----------------------------------------------------------
# remake xml from temp_pwg_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169
-- end of 'remake xml ...'

---------------------------------------------------
---- lsfix2 file with pwg_2

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt

(- 10230 6203)  4027 additional links


---- documentation in change files
python diff_to_changes_dict.py temp_pwg_0.txt temp_pwg_1.txt change_pwg_1.txt
252 changes written to change_pwg_1.txt

python diff_to_changes_dict.py temp_pwg_1.txt temp_pwg_2.txt change_pwg_2.txt
1322 changes written to change_pwg_2.txt

==============================================================
discuss remaining issues
==============================================================
Following analysis based on lsfix2_pwg_2.txt


---- 552 taranga 7 or 8.  
552 matches for "RĀJA-TAR. [78]," in buffer: lsfix2_pwg_2.txt
These may be from a 2nd volume, not part of rajatar
These are linked (classified as 'True')
  but the link 'fails' (shows page 1)

--------------------------------------
60 Classified as 'None'   These can be separated into several groups
They are not linked currently.

---- 8+ page refs to volume I. Not linked or split.
8 grep -E "<ls>RĀJA-TAR. t. I, p. [0-9]+" lsfix2_pwg_2.txt
  Could be linked (using app0 - page) and split (manually)

---- 5+ page refs to volume II.  Not linked or split.
5 matches for "<ls>RĀJA-TAR. t. II, p. [0-9]+"
  Volume II not covered by rajatar 

---- 5 volume I page refs
5 "<ls>RĀJA-TAR. I,[0-9]+"

---- 6 volume II page refs.  Unknown, not linkable with rajatar
6 matches for "<ls>RĀJA-TAR. II,[0-9]+"

---- 1 volume III page ref  unknown, not linkable with rajatar
1 matches for "<ls>RĀJA-TAR. III,[0-9]+"

---- 19 1-parameter references
13 "<ls>RĀJA-TAR. [0-9]+\."
 3 "<ls>RĀJA-TAR. [0-9]+[^0-9.]"
 3 "<ls n="RĀJA-TAR.">[0-9]+\."
  Interpretation of these is unknown

---- 11 'ed. Calc.' Not linkable
 A different edition.


---- 3 RĀJA-TAR. S.  unknown
3 "<ls>RĀJA-TAR. S."

---- 2 miscellaneous
azwama	<ls>RĀJA-TAR. I, p. 371, N.</ls>	
kAraskara	<ls>RĀJA-TAR. I, p. 554,41.</ls>	

(+ 8 5 5 6 1 19 11 3 2) == 60
