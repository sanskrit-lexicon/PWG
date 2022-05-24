Cases where <lang n="greek">X</lang> in pwg.txt and
X is a single Greek letter
31 matches for ">[αβγεδθιζ]<" in buffer: pwg.txt


temp_pwg_0.txt   latest from csl-orig:
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt
  At csl-orig commit baf520659e8f4474eb905ba737695e1d3911b572

make prototype changes which removes the markup on the greek letter.
Also show the prior line.

python onegreekletter.py temp_pwg_0.txt temp_change_1.txt
31 changes written to temp_change_1.txt

cp temp_change_1.txt change_1.txt
# We will manually adjust the resulting changes.

When searching for 2-letter greek strings, discovered some where 2nd
letter was period.

python onegreekletter_a.py temp_pwg_0.txt temp_change_1a.txt
12 cases
Append these to change_1.txt and adjust manually

python updateByLine.py temp_pwg_0.txt change_1.txt temp_pwg_1.txt
==================================================================
Move punctuation from end of greek text
<lang n="greek">XY</lang> -> <lang n="greek">X</lang>Y,
where Y is one of 5 characters:  [,.:;)]
python greek_end_punct.py temp_pwg_1.txt change_2.txt
203 changes

python updateByLine.py temp_pwg_1.txt change_2.txt temp_pwg_2.txt
203 changes

==================================================================
install into csl-orig and check validity
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
  OK as hoped!


cd /c/xampp/htdocs/sanskrit-lexicon/pwg/misc/greek
python proof.py greek temp_pwg_2.txt proof_greek.txt
==============================================================
