
readme_index.txt for aitbr

See readme_index.txt for discussion of these steps.
index_orig.txt is a renaming of index prepared by IrinaKonstant
 https://github.com/user-attachments/files/21567758/AITAREYABRAHMA.A.xlsx
 Ref: https://github.com/sanskrit-lexicon/PWG/issues/159
cp /e/pdfwork/aitbr/index_orig.txt index_orig.txt

cp index_orig.txt index.txt
--  edit index.txt to remove last 6 lines (epage >= 111)
There was a problem with the index.
mv index_orig.txt index_orig_prob.txt
mv index.txt index_prob.txt

Andhrabharati provides revised index:
  Ref:
convert to tsv form:
  AITAREYABRAHMANA.revised.txt
# use revised as (final) index.txt
mv AITAREYABRAHMANA.revised.txt index.txt

----------------------------------------
python switch_columns.py index_prob.txt index_prob_col.txt
250 Success: Page records read from index_prob.txt
250 lines writting to index_jim.txt

python unixify.py AITAREYABRAHMANA.revised.txt index_rev.txt
252 lines written to index_rev.txt

# before changes to index_jim.txt
diff index_prob_col.txt index_rev.txt| wc -l
# 84 lines in diff
# 68 lines.  84/4 = 21 differences
diff index_prob_col.txt index_rev.txt > diff_index_prob_rev.txt

cp index_prob_col.txt index_rev_jim.txt
# manually edit index_rev_jim.txt

cp index_rev_jim.txt index.txt

THE END
