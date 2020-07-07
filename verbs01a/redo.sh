#echo "remake mwverbs"
#python mwverb.py mw ../../mw/mw.txt mwverbs.txt
#echo "remake mwverbs1"
#python mwverbs1.py mwverbs.txt mwverbs1.txt
orig="../../../cologne/csl-orig/v02"
mwverbs1="../../MWS/mwverbs/mwverbs1.txt"
echo "remake pwg_verb_filter.txt"
python pwg_verb_filter.py ${orig}/pwg/pwg.txt pwg_verb_exclude.txt pwg_verb_include.txt pwg_verb_filter.txt
echo "remake pwg_verb_filter_map.txt"
python pwg_verb_filter_map.py pwg_verb_filter.txt pw_mw_map_edit.txt ${mwverbs1} pwg_verb_filter_map.txt
echo "remake pwg_preverb1.txt"
python preverb1.py slp1 ../pwg.txt pwg_verb_filter_map.txt ${mwverbs1} pwg_preverb1.txt
