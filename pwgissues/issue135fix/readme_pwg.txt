
issue135fix

pwg link forms:
2 parameters.

7808  "RĀJA-TAR."   
  11  "RĀJA-TAR. ed. Calc."   a different edition

python lsfix2.py pwg temp_pwg_0.txt lsfix2_pwg_0.txt
(False,11),(None,296),(True,6203),(fixed,1290),(all,7800) lsfix2_pwg_0.txt

cp temp_pwg_0.txt temp_pwg_1.txt

Make changes to temp_pwg_1 and 2 to correct False and None
 
python lsfix2.py pwg temp_pwg_1.txt lsfix2_pwg_1.txt
(None,60),(True,6413),(fixed,1324),(all,7797) lsfix2_pwg_1.txt


A small number of refs to tarangas 7,8 e.g.
durgaGAta <ls>RĀJA-TAR. 7,1175 (1173).</ls>
The index doesn't have these.

980 : ajitApIqa : RĀJA-TAR. IV,689. : RĀJA-TAR. 4,689. : print change


--------------------
# generate temp_pwg_2.txt from temp_pwg_1.txt and the 'fixed' elements
python dict_replace2.py temp_pwg_1.txt lsfix2_pwg_1.txt temp_pwg_2.txt
apply_repls: 1322 lines changed


-----------------------------------------------------------
# remake xml from temp_pwg_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135fix
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue135fix
-- end of 'remake xml ...'

---------------------------------------------------
---- lsfix2 file with pwg_2

python lsfix2.py pwg temp_pwg_2.txt lsfix2_pwg_2.txt
(None,60),(True,10230),(all,10290) lsfix2_pwg_2.txt

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
