
issue169


=====================
mw Rājat. 7/8,N
   Rājat. (C)   one instance in hw 'jagat'

python lsfix2.py mw temp_mw_0.txt lsfix2_mw_0.txt
(None,684),(all,684) lsfix2_mw_0.txt

--- 2 parameters
512 matches for "<ls>Rājat. [iv]+, [0-9]+\( f+\)?\.?</ls>"
 46 matches for "<ls n="Rājat.">[iv]+, [0-9]+\( f+\)?\.?</ls>"
 51 matches for "<ls n="Rājat. [iv]+,">[0-9]+\( f+\)?\.?</ls>"
609 Total -- these link
--- 1 parameter - no link
 59 matches for "<ls>Rājat. [iv]+\( f+\)?\.?</ls>"
 15 matches for "<ls n="Rājat.">[iv]+\( f+\)?\.?</ls>"
 74 total

(+ 609 74) = 683

1 other:
tipya	<ls>Rājat. viii, 15, 5.</ls>  This is malformed. It links to
 rajatarcalc at  8,15 but (of course) tipya is not found


Checks of taranga 7
81 matches for "\( vii,\|>vii,\)"
karRIraTa	<ls>Rājat. vii, 479.</ls>
Garawwa	<ls>Rājat. vii, 1244</ls>
janaSruti	<ls>Rājat. vii, 133.</ls>


Checks of taranga 8
78 matches for "\( viii,\|>viii,\)"
kapAwita	<ls>Rājat. viii, 321.</ls>
catuzka	<ls n="Rājat. viii,">2931</ls>
nididrAsu	<ls>Rājat. viii, 2130</ls>  :  mw error, see below
108577 : nididrAsu : Rājat. viii, 2130 : Rājat. viii, 2139 : cf. PW : print change
darpitapura	<ls n="Rājat.">viii, 1942.</ls>


-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue169

---------------------------------------
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
1 changes written to change_mw_1.txt
