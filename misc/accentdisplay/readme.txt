
Display various spellings with 3 fonts (siddhanta, adhishila, default);
python example1.py example1.txt example1.html

--- rest of file for later use
python changes_1.py pwg.txt changes_1.txt
 12 cases
 These cases currently display wrongly.
 How to change slp1_deva1.xml so these display properly?
; x = na\dya1^\H
; x = sva1^\H
; x = ta\nva1^\H
; x = pariva\rgya1^\H
; x = viSvE^rvI\ryE\3^\H
; x = pra\sva1^\H
; x = sva1^\H
; x = sarvA^sta\nva1^\H
; x = ru\da\tya1^\H
; x = ta\nva1^\H
; x = vida\Tya1^\H
; x = ta\nva1^\H

python convert.py x_changes_1.txt x_changes_1_convert.txt deva1
python convert.py x_changes_2.txt x_changes_2_convert.txt deva2

python convert1.py x_misc1.txt x_misc1_convert1.txt



python changes_2.py pwg.txt changes_2.txt
 15 cases
 These are currently displayed correctly, but the spelling is wrong. (accent should precede [MH])
; x = dU\Qya1^H\
; x = ruda\tya1^H\
; x = su\Bva1^H\
; x = azwaka\rRya1^H\
; x = asi^knyA^M\
; x = udraTA^nA^M\
; x = su\Bva1^H\
; x = sva1^H\
; x = su\Bva1^H\
; x = Da\rtAra^mo\Ryo\3^H\
; x = nApara^M\
; x = martya^M\
; x = ti\mraSca\mva1^H\
; x = manu\zyA\3^H\
; x = ta\nva1^H\

Emacs 17 matches for "[HM][\/^]"  has also these two matches
; <L>28552<pc>3-0214<k1>tan<k2>tan<h>1
; 3-9218 4)
281980 old <ls>ṚV. 6, 46, 12.</ls> {#aM\Ho\yuva^sta\nva^stanvate\ vi#}
281980 new <ls>ṚV. 6, 46, 12.</ls> {#a\Mho\yuva^sta\nva^stanvate\ vi#}
;
; <L>32023<pc>3-0515<k1>dama<k2>dama/<h>1
316133 old <ls n="ṚV.">1, 1, 8.</ls> <ls n="ṚV.">2, 2, 11.</ls> <ls n="ṚV.">4, 8, 3.</ls> <ls>VS. 8, 24.</ls> {#siM\Ho na dame^#} 
316133 new <ls n="ṚV.">1, 1, 8.</ls> <ls n="ṚV.">2, 2, 11.</ls> <ls n="ṚV.">4, 8, 3.</ls> <ls>VS. 8, 24.</ls> {#si\Mho na dame^#} 

python updateByLine.py pwg.txt changes.txt pwg_1.txt

## not done  python make_tooltip.py pwgbib_input.txt pwg_tooltip.txt

python updateByLine.py pwg.txt changes.txt pwg_1.txt
 1035 change transacctions

regenerate pwg.xml and check for validity
cp pwg_1.txt ../pwg.txt  # assumes in subdirectory csl-orig/v02/pwg/
# in csl-pywork/v02, regenerate local pwg xml and displays
sh generate_dict.sh pwg  ../../pwg                                            
## check validity of pwg.xml
python ../../xmlvalidate.py ../../pwg/pywork/pwg.xml ../../pwg/pywork/pwg.dtd 
  correct changes.txt as needed, then rerun prior three steps
  
; ---- redo the 'problem' cases

python changes_remark.py 'ṚV. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_rv_prat.txt
4
python changes_remark.py 'AV. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_av_prat.txt
13
python changes_remark.py 'TS. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_ts_prat.txt
1
python changes_remark.py 'TAITT. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_taitt_prat.txt
0
python changes_remark.py 'VS. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_vs_prat.txt

python changes_remark.py 'PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_prat.txt

python changes_remark.py 'PRĀT.' 3,True pwg_1.txt pwgbib_input.txt problem_prat.txt
  # the '3' (generates change transactions for all <ls>abbrev...</ls>)

concatenate the 6 'problem' files to changes_todo.txt
cat problem*.txt > changes_todo.txt
