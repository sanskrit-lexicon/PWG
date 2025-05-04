issue145/readme.txt
05-04-2025 begun ejf
KĀTYĀYANA'S ŚRAUTASŪTRĀṆI, 2-parameter links

Ref: https://github.com/sanskrit-lexicon/PWG/issues/145
Ref: https://github.com/sanskrit-lexicon/PWG/issues/136

This issue145 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue145

--------------------------------------------------
Changes to pwg.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg0.txt

We begin by focus on two-parameter refereces in pwg:
  'pwg':r'<ls>KĀTY. ŚR. ([0-9]+),([0-9]+)[^0-9,]',

@AnnaRybakovaT pointed out examples like:
 <ls>Schol.</ls> zu <ls>KĀTY. ŚR. 357,12.</ls>
which refers to line 12 of (internal) page 357 of the pdf we are using.

file pwg_2parm.txt shows the 339 matches in pwg.txt of form
 " zu <ls>KĀTY. ŚR. [0-9]+,[0-9]+[^0-9,]"

Technical point:  Software finding such matches may miss cases
  in pwg.txt
  where "zu" is not on same line of pwg.txt as  "<ls>KĀTY. ŚR. ..."

In current pwg.txt markup, there are MANY instances where ' zu' is at
 the end of a line, and the next line starts with '<ls'

5797 matches for " zu *{{LINE_BREAK}}<ls" in buffer: temp_pwg0.txt

Example 1:
OLD:
{#aNgahAri#}¦ <lex>m.</lex> = {#aNgahAra#} Schol. zu
<ls>AK.</ls> im <ls>ŚKDR.</ls>
NEW:
{#aNgahAri#}¦ <lex>m.</lex> = {#aNgahAra#} Schol. zu <ls>AK.</ls>
im <ls>ŚKDR.</ls>

Example 2: intervening [PAGE..]
OLD:
<ls>BHARTṚ. 3,71.</ls> Schol. zu
[Page3-0611]
<ls>AMAR. 54.</ls>
NEW:
<ls>BHARTṚ. 3,71.</ls> Schol. zu <ls>AMAR. 54.</ls>
[Page3-0611]
[BLANK LINE]


python zuchange.py temp_pwg0.txt temp_pwg1.txt
adjust1 change to 5 lines     remove space(s) at end of line
adjust1a change to 60 lines   remove space(s) at start of line
adjust2 change to 11850 lines like example 1 above
adjust3 change to 14 lines    like example 2 above

Remove empty lines in entries.

python remove_blank.py temp_pwg1.txt temp_pwg2.txt
1132563 lines read from temp_pwg1.txt
adjust: 3458 empty body lines dropped
1129105 written to temp_pwg2.txt

12047 matches in 11142 lines for " zu <ls" in buffer: temp_pwg0.txt
18141 matches in 17062 lines for " zu <ls" in buffer: temp_pwg2.txt

No lines in temp_pwg2.txt start or end with a space characters ' '.

367 matches for " zu <ls>KĀTY. ŚR. [0-9]+,[0-9]+[^0-9,]" in buffer: temp_pwg2.tx
  Contrast this with
339 matches for " zu <ls>KĀTY. ŚR. [0-9]+,[0-9]+[^0-9,]" in buffer: temp_pwg0.txt

---------------------------------------
#install temp_pwg2.txt into csl-orig
cp temp_pwg2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
sync csl-orig to github
sync cologne to github.

