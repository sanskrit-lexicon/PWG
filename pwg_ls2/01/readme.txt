Ref: https://github.com/sanskrit-lexicon/PWG/issues/35

Markup revisions involving 'Sch.' abbreviation.


# assume we are in a temp directory of v02/ in csl-orig repository.

cp ../pwg.txt pwg_0.txt
This work was done with pwg.txt at commit 2f3d57b51c81d46e972632951e9e80b08253f0a2

The work proceeds by generating three temporary intermediate versions:
pwg_1.txt, pwg_2.txt, and pwg_3.txt.
Each intermediate version is created in two steps:
a. generate change transactions (change1.txt, etc)
b. apply change transactions to prior version of pwg.txt

The latest version of pwg then installed in csl-orig
Install pwg_3.txt
## recall assumption this work done in temporary subdirectory of
## csl-orig/v02/pwg
cp pwg_3.txt ../pwg.txt

Do usual installation steps locally and on Cologne server.

# --------------------------------------------------------------
  TODO
python sch_change_remain.py pwg_3.txt change_todo.txt
152 written to change_todo.txt
These are all the 'unmarked'  "Sch." instances.
Corrections could be made manually -- they are too complex to
correct by a program.

# --------------------------------------------------------------
Details of the changes
# --------------------------------------------------------------
pwg_1.txt
# Generate change transactions 
python change1.py pwg_0.txt change1.txt 
591 written to change1.txt
## apply the change transactions to the digitization
python updateByLine.py pwg_0.txt change1.txt pwg_1.txt

Three types of changes appear in change1.txt
Type 1:  552 instances
Example:
OLD:
<ls>P. 1, 4, 37, Sch.</ls>
NEW:
<ls>P. 1, 4, 37</ls>, <ls>Sch.</ls>

Type 2: 15 instances. 'Sch.' at end of line
Example:
OLD:
<ls>PAT.</ls> {#atipadA gAyatrI#} Sch.
NEW:
<ls>PAT.</ls> {#atipadA gAyatrI#} <ls>Sch.</ls>

Type 3: 24 instances.  <ls>?(Sch.</ls>
Example:
OLD:
<ls>?(Sch.</ls> {#SastramatikrAnto 'tiSastro naKAnAM nyAsaH#}) 
NEW:
(<ls>Sch.</ls> {#SastramatikrAnto 'tiSastro naKAnAM nyAsaH#})

# --------------------------------------------------------------
pwg_2.txt

# generate change transactions
python change2.py pwg_1.txt change2.txt 
335 written to change2.txt
## apply the change transactions to the digitization
python updateByLine.py pwg_1.txt change2.txt pwg_2.txt

Four types of changes appear in change2.txt
Type 1: 243 instances ' Sch. ' NOT appearing in '<ls>...</ls>'
Example:
OLD:
<ls>VAIJ.</ls> beim Sch. zu <ls>ŚIŚ. 12, 2.</ls> ({#akzaScakraDAraRe#}) und zu 
NEW:
<ls>VAIJ.</ls> beim <ls>Sch.</ls> zu <ls>ŚIŚ. 12, 2.</ls> ({#akzaScakraDAraRe#}) und zu

Type 2: 79 instances "(Sch.: "
Example:
OLD:
(Sch.: {#varRAnAloqayanniva SanEH . aNKatirgatyarTaH#}) 
NEW:
(<ls>Sch.</ls>: {#varRAnAloqayanniva SanEH . aNKatirgatyarTaH#})

Type 3: 8 instances.  "Sch. " at beg of line
Example:
OLD:
Sch. {%ungewöhnlich, extraordinär%}
NEW:
<ls>Sch.</ls> {%ungewöhnlich, extraordinär%} 

Type 4: 5 instances: "(Sch.:</ls>"
Example:
OLD:
<ls>?3, 3, 44 (Sch.:</ls> = {#kriyAyAH kArtsnyena saMbanDaH#}). 
NEW:
<ls>?3, 3, 44</ls> (<ls>Sch.</ls>: = {#kriyAyAH kArtsnyena saMbanDaH#}).



# --------------------------------------------------------------
pwg_3.txt

Generate manual transaction file for remaining unmarked 'Sch.'
python sch_change_remain.py pwg_2.txt temp.txt
191 cases found.
cp temp.txt change3_edit.txt.
Some of these (39) were changed manually in change3_edit.txt.
# apply these 39 changes
python updateByLine.py pwg_2.txt change3_edit.txt pwg_3.txt


