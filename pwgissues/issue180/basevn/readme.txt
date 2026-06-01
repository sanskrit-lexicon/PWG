Derive issue180/temp_ab_files/pwg_base.txt and pwg_VN.txt

* ../temp_pwg_0a.txt:  remove empty lines
pwg_base.txt has removed empty lines within entries.
This is non-invertible, but not controversial.

python remove_empty_lines.py ../temp_pwg_0.txt ../temp_pwg_0a.txt
1129105 lines read from ../temp_pwg_0.txt
631 empty lines removed from entries
1128474 lines written to ../temp_pwg_0a.txt

  (- 1129105 1128474) # 631 empty lines removed

* ../temp_pwg_0b.txt 
Misc changes 
python change_0a_0b.py ../temp_pwg_0a.txt ../temp_pwg_0b.txt
1128474 lines read from ../temp_pwg_0a.txt
3 lines skipped,  1 line(s) changed
adjust_lines2 inserts 6 lines
1128477 lines written to ../temp_pwg_0b.txt

--------------
* temp_pwg_0b_lend.txt
# put some <H>, etc. lines between entries after <LEND> of prior entry

python lend.py MERGE ../temp_pwg_0b.txt temp_pwg_0b_lend.txt
1128477 lines read from ../temp_pwg_0b.txt
1128395 lines written to temp_pwg_0b_lend.txt


# check invertibility
python lend.py RESTORE temp_pwg_0b_lend.txt temp.txt
1128395 lines read from temp_pwg_0b_lend.txt
1128477 lines written to temp.txt

diff ../temp_pwg_0b.txt temp.txt | wc -l
# 0 -- temp_pwg_0b.txt restored
rm temp.txt
--------------------------------------
* temp_pwg_0b_base.txt,  temp_pwg_0b_vn.txt
python basevn_split.py temp_pwg_0b_lend.txt temp_pwg_0b_base.txt temp_pwg_0b_vn.txt
1128395 lines read from temp_pwg_0b_lend.txt
123366 entries
122738 base entries
   628 vn entries
1125883 lines written to temp_pwg_0b_base.txt
2511 lines written to temp_pwg_0b_vn.txt

# Check invertibility
python basevn_join.py temp_pwg_0b_base.txt temp_pwg_0b_vn.txt temp.txt
1125883 lines read from temp_pwg_0b_base.txt
2511 lines read from temp_pwg_0b_vn.txt
122738 entries
628 entries
122738 base entries
   628 vn entries
1128395 lines written to temp.txt

diff temp_pwg_0b_lend.txt temp.txt | wc -l
# 0 expected

-------
* pwg_VN.txt peculiarity
diff ../temp_ab_files/pwg_vn.txt temp_pwg_0_vn.txt | wc -l
Reason for difference:
 ../temp_ab_files/pwg_vn.txt   has dropped the <H>{#X#} lines

edit temp_pwg_0_vn.txt
Emacs regex replacement: ^<LEND>.+$ → <LEND>
Save as temp.txt
diff ../temp_ab_files/pwg_vn.txt temp.txt | wc -l
# 0
# no need for temp.txt


-------
* pwg_base, _VN  counts
wc -l ../temp_ab_files/pwg_base.txt
598773 ../temp_ab_files/pwg_base.txt

wc -l ../temp_ab_files/pwg_vn.txt
2511 ../temp_ab_files/pwg_vn.txt

-------
* pwg_base_a.txt (dropdouble_LBC)
# ../temp_ab_files/pwg_base.txt has 94 instances of " 🞄 🞄"
# no obvious reason
# make ../temp_ab_files/pwg_base_a.txt
python dropdouble_LBC.py ../temp_ab_files/pwg_base.txt ../temp_ab_files/pwg_base_a.txt
598773 lines read from ../temp_ab_files/pwg_base.txt
93 lines changed
598773 lines written to ../temp_ab_files/pwg_base_a.txt
-------
* temp_pwg_0b_base1.txt  (div_join)
python div_join.py temp_pwg_0b_base.txt temp_pwg_0b_base1.txt
598773 lines written to temp_pwg_0b_base1.txt

* temp_pwg_0b_base2.txt (div_split = inverse of base1)
# div_split.py is inverse of div_join.py

python div_split.py temp_pwg_0b_base1.txt temp_pwg_0b_base2.txt
1125883 lines written to temp_pwg_0b_base2.txt
# check invertibility
diff temp_pwg_0b_base.txt  temp_pwg_0b_base2.txt  | wc -l
# 0

# no further need of base2
rm temp_pwg_0b_base2.txt

--------------------------------
* compare ../temp_ab_files/pwg_base_b.txt and temp_pwg_0b_base1.txt

diff ../temp_ab_files/pwg_base_a.txt temp_pwg_0b_base1.txt | wc -l
0 
../temp_ab_files/pwg_base_a.txt  == temp_pwg_0b_base1.txt

This finishes the construction of Andhrabharati's 'BASE' file,
 
../temp_ab_files/pwg_base_a.txt.

