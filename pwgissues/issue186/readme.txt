
06-14-2026 begin ejf

PWG tooltip cleanup for global abbreviations.


Ref: https://github.com/sanskrit-lexicon/PWG/tree/master/pwgissues/issues/186


this directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue186

* temp_pwg_0.txt

# get temporary local copy of kosha
  (at commit c671ad1b9)
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

-------------------------------------
* pwgab_input_0.txt
current tooltip file (at commit 513e2e2 of csl-pywork)

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgab/pwgab_input.txt pwgab_input_0.txt

-------------------------------------
* count_ab_0.txt  global <ab>X</ab> with counts
# count_ab.py from issue180

python count_ab.py temp_pwg_0.txt count_ab_0.txt
789 lines written to count_ab_0.txt
180304 = total number of <ab>X</ab>

* count_lex_0.txt  global <lex>X</lex> with counts
# count_lex.py from issue180

python count_lex.py temp_pwg_0.txt count_lex_0.txt
9 lines written to count_lex_0.txt
131614 = total number of <lex>X</lex>

The 9 lex abbreviations are:
adj. adv. f. ind. indecl. interj. m. n. neutr. 

* pwgab_input_1.txt
# update tooltips for counts.
python update_tips.py pwgab_input_0.txt count_ab_0.txt pwgab_input_1.txt warnings_0_1.txt
791 lines read from pwgab_input_0.txt
789 lines read from count_ab_0.txt
809 lines written to pwgab_input_1.txt
20 lines written to warnings_0_1.txt

These warnings are for abbreviations appearing in pwgab_input_0.txt
but not appearing in count_ab_0.txt.  

There are two types:  
LEX   : 9 abbreviations in count_lex_0.txt
        adj. adv. f. ind. indecl. interj. m. n. neutr.
        pwgab_input.txt is used for tooltips for these.
WARN  : 11 cases. 

* WARNINGS TO KEEP
These 4 are marked as <lang>X</lang>.

engl. : KEEP:  <lang>engl.</lang>  
franz. : KEEP: <lang>franz.</lang>
lith.  : KEEP : <lang>lith.</lang>  tooltip 'Lithuanian';  Also appears in <ls> not as abbrev
ved.   : KEEP : <lang>ved.</lang>

Why keep?  So tooltips of pwgab_input.txt will be available in displays.
This requires a change to basicadjust.php in csl-websanlexicon
which I am making.


* Suggestions to handle warnings
DEL means "DELETE from pwgab_input".  KEEP means retain in pwgab_input
aa. : DEL : local abbrev.  
Adhy. : DEL : 1 local abbrev, 6 within <ls>
Gegend. : DEL : not an abbreviation
N.N.   : DEL : N. N. local abbreviation
Padap. : DEL : 1 local abbrev in 'is' tag;  pwg to add  local abbrev for 4 other <is>Padap.</is>
Trigl. : DEL : 1 instance in <ls>
urpsr. : DEL : (a spelling error)

* Suggestion for 'u.'
old: <disp>unter - under </disp>
new: <disp>unter / und - under, and</disp>

* Suggestions to handle warnings
DEL means "DELETE from pwgab_input".  KEEP means retain in pwgab_input
aa. : DEL : local abbrev.  
Adhy. : DEL : 1 local abbrev, 6 within <ls>
engl. : KEEP:  <lang>engl.</lang>  
franz. : KEEP: <lang>franz.</lang>
Gegend. : DEL : not an abbreviation
lith.  : KEEP : <lang>lith.</lang>  tooltip 'Lithuanian';  Also appears in <ls> not as abbrev
N.N.   : DEL : N. N. local abbreviation
Padap. : DEL : 1 local abbrev in 'is' tag;  pwg to add  local abbrev for 4 other <is>Padap.</is>
Trigl. : DEL : 1 instance in <ls>
urpsr. : DEL : (a spelling error)
ved.   : KEEP : <lang>ved.</lang>

* <disp>?</disp>  18  case in pwgab_input_1.txt
These are abbreviations not in pwgab_input_0.txt.
Tooltips need to be developed, by reference to pwg.txt context
ad.	<id>ad.</id> <disp>?</disp>  <N>18</N> UNCHECKED
auf.	<id>auf.</id> <disp>?</disp>  <N>36</N> UNCHECKED
Auf.	<id>Auf.</id> <disp>?</disp>  <N>2</N> UNCHECKED
Chr.	<id>Chr.</id> <disp>?</disp>  <N>2</N> UNCHECKED
d. f.	<id>d. f.</id> <disp>?</disp>  <N>1</N> UNCHECKED
d. fg.	<id>d. fg.</id> <disp>?</disp>  <N>1</N> UNCHECKED
d. folg.	<id>d. folg.</id> <disp>?</disp>  <N>14</N> UNCHECKED
d. vor.	<id>d. vor.</id> <disp>?</disp>  <N>1</N> UNCHECKED
d. vorang.	<id>d. vorang.</id> <disp>?</disp>  <N>1</N> UNCHECKED
d. vorherg.	<id>d. vorherg.</id> <disp>?</disp>  <N>1</N> UNCHECKED
excl.	<id>excl.</id> <disp>?</disp>  <N>1</N> UNCHECKED
genet.	<id>genet.</id> <disp>?</disp>  <N>1</N> UNCHECKED
imperatt.	<id>imperatt.</id> <disp>?</disp>  <N>6</N> UNCHECKED
Nom. ag.	<id>Nom. ag.</id> <disp>?</disp>  <N>1</N> UNCHECKED
Sp.	<id>Sp.</id> <disp>?</disp>  <N>282</N> UNCHECKED
v.	<id>v.</id> <disp>?</disp>  <N>4</N> UNCHECKED
v. Chr.	<id>v. Chr.</id> <disp>?</disp>  <N>4</N> UNCHECKED
Z. B.	<id>Z. B.</id> <disp>?</disp>  <N>1</N> UNCHECKED

* Additional '?' in tooltip  (8)
an.	<id>an.</id> <disp>anders? - otherwise </disp> <INFER/> <N>3</N> UNCHECKED
beim.	<id>beim.</id> <disp>Beiname? - epithet  / (preposition) at the</disp> <INFER/> <N>5</N> UNCHECKED
Beim.	<id>Beim.</id> <disp>Beiname? - epithet</disp>  <N>1</N> UNCHECKED
Es.	<id>Es.</id> <disp>? - ?</disp> <INFER/> <N>2</N> UNCHECKED
geder.	<id>geder.</id> <disp>gedeutet? - interpreted (?)</disp> <INFER/> <N>1</N> UNCHECKED
w.	<id>w.</id> <disp>Wort? - word? </disp> <INFER/> <N>2</N> UNCHECKED
Wortm.	<id>Wortm.</id> <disp>Wortmasse? - word material (?)</disp> <INFER/> <N>1</N> UNCHECKED

* Finally 238 additional 'UNCHECKED' tooltips
These to be checked by some means, and changed to CHECKED.



* installed change in basicadjust.php
in csl-websanlexicon and in csl-apidev.
To handle tooltip for <lang>X</lang>.  More X will be found later, in another issue.
