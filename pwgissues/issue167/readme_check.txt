Make misc checks between pwg , the pdf and index

Miscellaneous check using generate_random.py


cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue167


----------------------
 'pwg2a':r'<ls>NIR. ([0-9]+),([0-9]+)',

python generate_random_nir.py ALL pwg2a temp_pwg_0.txt index_nir.txt checks_nir/check_pwg2a_ALL_0.txt checks_nir/check_pwg2a_nopagerec_0.txt

regex_raw = <ls>NIR. ([0-9]+),([0-9]+)
found 2954 instances in kosha
found 401 distinct in kosha
write_examples: 2954 written to checks_nir/check_pwg2a_ALL_0.txt
8 instances of 'pagerec not found'
write_examples: 8 written to checks_nir/check_pwg2a_nopagerec_0.txt


----------------------
 'pwg2b':r'<ls>NAIGH. ([0-9]+),([0-9]+)',

python generate_random_naigh.py ALL pwg2b temp_pwg_0.txt index_naigh.txt checks_naigh/check_pwg2b_ALL_0.txt checks_naigh/check_pwg2b_nopagerec_0.txt

regex_raw = <ls>NAIGH. ([0-9]+),([0-9]+)
found 1356 instances in kosha
found 89 distinct in kosha
write_examples: 1356 written to checks_naigh/check_pwg2b_ALL_0.txt
13 instances of 'pagerec not found'
write_examples: 13 written to checks_naigh/check_pwg2b_nopagerec_0.txt


----------------------
 'pw2a':r'<ls>NIR. ([0-9]+),([0-9]+)',

python generate_random_nir.py ALL pw2a temp_pw_0.txt index_nir.txt checks_nir/check_pw2a_ALL_0.txt checks_nir/check_pw2a_nopagerec_0.txt

regex_raw = <ls>NIR. ([0-9]+),([0-9]+)
found 100 instances in kosha
found 70 distinct in kosha
write_examples: 100 written to checks_nir/check_pw2a_ALL_0.txt
1 instances of 'pagerec not found'
write_examples: 1 written to checks_nir/check_pw2a_nopagerec_0.txt

----------------------
 'pw2b':r'<ls>NAIGH. ([0-9]+),([0-9]+)',

python generate_random_naigh.py ALL pw2b temp_pw_0.txt index_naigh.txt checks_naigh/check_pw2b_ALL_0.txt checks_naigh/check_pw2b_nopagerec_0.txt

regex_raw = <ls>NAIGH. ([0-9]+),([0-9]+)
found 10 instances in kosha
found 8 distinct in kosha
write_examples: 10 written to checks_naigh/check_pw2b_ALL_0.txt
0 instances of 'pagerec not found'

----------------------
 'pwkvn2a':r'<ls>NIR. ([0-9]+),([0-9]+)',

python generate_random_nir.py ALL pwkvn2a temp_pwkvn_0.txt index_nir.txt checks_nir/check_pwkvn2a_ALL_0.txt checks_nir/check_pwkvn2a_nopagerec_0.txt

regex_raw = <ls>NIR. ([0-9]+),([0-9]+)
found 18 instances in kosha
found 17 distinct in kosha
write_examples: 18 written to checks_nir/check_pwkvn2a_ALL_0.txt
0 instances of 'pagerec not found'

----------------------
 'sch2a':r'<ls>Nir. ([0-9]+),([0-9]+)',

python generate_random_nir.py ALL sch2a temp_sch_0.txt index_nir.txt checks_nir/check_sch2a_ALL_0.txt checks_nir/check_sch2a_nopagerec_0.txt

regex_raw = <ls>Nir. ([0-9]+),([0-9]+)
found 19 instances in kosha
found 17 distinct in kosha
write_examples: 19 written to checks_nir/check_sch2a_ALL_0.txt
0 instances of 'pagerec not found'


----------------------
 'sch2b':r'<ls>Nigh. ([0-9]+),([0-9]+)',

python generate_random_naigh.py ALL sch2b temp_sch_0.txt index_naigh.txt checks_naigh/check_sch2b_ALL_0.txt checks_naigh/check_sch2b_nopagerec_0.txt

regex_raw = <ls>Nigh. ([0-9]+),([0-9]+)
found 1 instances in kosha
found 1 distinct in kosha
write_examples: 1 written to checks_naigh/check_sch2b_ALL_0.txt
0 instances of 'pagerec not found'

----------------------
 'mw2a':r'<ls>NIR. ([0-9]+),([0-9]+)',

python generate_random_nir.py ALL mw2a temp_mw_0.txt index_nir.txt checks_nir/check_mw2a_ALL_0.txt checks_nir/check_mw2a_nopagerec_0.txt

regex_raw = <ls>Nir. ([ivxl]+), ([0-9]+)
found 476 instances in kosha
found 232 distinct in kosha
write_examples: 476 written to checks_nir/check_mw2a_ALL_0.txt
0 instances of 'pagerec not found'

----------------------
 'mw2b':r'<ls>NAIGH. ([0-9]+),([0-9]+)',

python generate_random_naigh.py ALL mw2b temp_mw_0.txt index_naigh.txt checks_naigh/check_mw2b_ALL_0.txt checks_naigh/check_mw2b_nopagerec_0.txt

regex_raw = <ls>Naigh. ([ivxl]+), ([0-9]+)
found 439 instances in kosha
found 68 distinct in kosha
write_examples: 439 written to checks_naigh/check_mw2b_ALL_0.txt
3 instances of 'pagerec not found'
write_examples: 3 written to checks_naigh/check_mw2b_nopagerec_0.txt

===================================================================
Try to resolve the 'pagerec not found' problems by
editing the nopagerec_0 files
and making change to verseion 1 of kosha.

--------------------
cp temp_pwg_0.txt temp_pwg_1.txt

checks_nir/check_pwg2a_nopagerec_0.txt
  No typos found.
  
checks_naigh/check_pwg2b_nopagerec_0.txt

81498 : yantraRa : NAIGH. 4,10 : NAIṢ. 4,10 : typo
57225 : maDyesaBam : NAIGH. 6,76 : NAIṢ. 6,76 : typo
88101 : var : NAIGH. 22,41 : NAIṢ. 22,41 : typo
54463 : BAj : NAIGH. 22,44 : NAIṢ. 22,44 : typo
54857 : Bitta : NAIGH. 22,57 : NAIṢ. 22,57 : typo
36831 : DU : NAIGH. 1,35 : NAIṢ. 1,35  : typo

--------------------------
cp temp_pw_0.txt temp_pw_1.txt

checks_nir/check_pw2a_nopagerec_0.txt
120328 : samAnAKyAna : NIR. 7,39 : NIR. 7,30 : typo

--------------------------
cp temp_mw_0.txt temp_mw_1.txt

checks_naigh/check_mw2b_nopagerec_0.txt
128309 : pfkza : Naigh. ii, 57 : Naigh. ii, 17 : typo
161697 : mA : Naigh. iii, 59 : Naigh. iii, 19 : typo


