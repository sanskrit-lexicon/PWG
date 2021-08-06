
python changes_1.py pwg.txt changes_1.txt
 46 cases.  Requires editing
python changes_2.py pwg_1.txt changes_2.txt
 9 cases
python changes_3.py pwg_1.txt changes_3.txt

python updateByLine.py pwg.txt changes.txt pwg_1.txt

## not done  python make_tooltip.py pwgbib_input.txt pwg_tooltip.txt
python lsextract.py 'AV. PRĀT.' pwg_1.txt pwgbib_input.txt temp_lsextract_av_prat.txt
python lsextract.py 'ṚV. PRĀT.' pwg_1.txt pwgbib_input.txt temp_lsextract_rv_prat.txt
python lsextract.py 'TAITT. PRĀT.' pwg_1.txt pwgbib_input.txt temp_lsextract_taitt_prat.txt
python lsextract.py 'VS. PRĀT.' pwg_1.txt pwgbib_input.txt temp_lsextract_vs_prat.txt
python lsextract.py 'TS. PRĀT.' pwg_1.txt pwgbib_input.txt temp_lsextract_ts_prat.txt
python lsextract.py 'TAITT. PR.' pwg_1.txt pwgbib_input.txt temp_lsextract_taitt_pr.txt
python lsextract.py 'PRĀT.' pwg_1.txt pwgbib_input.txt temp_lsextract_prat.txt
python lsextract.py 'PRĀTIŚ.' pwg_1.txt pwgbib_input.txt temp_lsextract_pratis.txt
python lsextract.py 'ṚV. PRĀTIŚ.' pwg_1.txt pwgbib_input.txt temp_lsextract_rv_pratis.txt

AV. PRĀT. 547
ṚV. PRĀT. 1147
TS. PRĀT. 397
TAITT. PRĀT. 107
TAITT. PR. 2
VS. PRĀT. 779
PRĀT. 9
PRĀTIŚ. 1
ṚV. PRĀTIŚ. 10


ṚV. PRĀTIŚ.

remark changes

python changes_remark.py 'AV. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt temp_changes_av_prat.txt
 160
make manual changes
python changes_remark.py 'AV. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt temp.txt
 20+
 problem_av_s.txt
python changes_remark.py 'ṚV. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt temp_changes_rv_prat.txt
 
python changes_remark.py 'ṚV. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_rv_prat.txt
 problem_rv_prat.txt   25
 
python changes_remark.py 'TS. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt temp_changes_ts_prat.txt

python changes_remark.py 'TS. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_ts_prat.txt
 problem_ts_prat.txt  2
 
python changes_remark.py 'TAITT. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt temp_changes_taitt_prat.txt
python changes_remark.py 'TAITT. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_taitt_prat.txt
 problem_taitt_prat.txt 4

TAITT. PR. 2
python changes_remark.py 'TAITT. PR.' 2,False pwg_1.txt pwgbib_input.txt temp_changes_taitt_pr.txt
 no changes needed

VS. PRĀT. 779
python changes_remark.py 'VS. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt temp_changes_vs_prat.txt

python changes_remark.py 'VS. PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_vs_prat.txt
 8, but no real problems.  All are '<ls>VS. PRĀT.</ls.'

python changes_remark.py 'PRĀT.' 2,False pwg_1.txt pwgbib_input.txt problem_prat.txt

; regenerate current pwg_1 from changes.txt
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
