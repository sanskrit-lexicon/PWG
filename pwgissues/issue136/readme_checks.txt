

KĀTYĀYANA'S ŚRAUTASŪTRĀṆI has 2 kinds of citations:

citations of verses: Adhy.-Kaṇḍikā-Śloka (KĀTY. ŚR. 6,7,14.),
citations of commentaries: Ipage-line (Schol. zu KĀTY. ŚR. 34,9.).
57 matches for "Schol. zu <ls>KĀTY. ŚR. [0-9]+,[0-9]+[^0-9,]" in buffer: temp_pwg.txt

Also,
62 matches for "Schol. zu <ls>KĀTY. ŚR. [0-9]+,[0-9]+,[0-9]+" in buffer: temp_pwg.txt

# preliminary check of temp_pwg.txt and index and pdf
# adhy,kand,verse

python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg_man.txt
regex_raw = <ls>KĀTY. ŚR. ([0-9]+),([0-9]+),([0-9]+)
found 4629 instances in kosha

  one NOT FOUND:  see check_pwg_man.txt

----------
python generate_random.py 5 pwg2 temp_pwg.txt index.txt check_pwg2_man.txt
123366 entries found
regex_raw = Schol. zu <ls>KĀTY. ŚR. ([0-9]+),([0-9]+)[^0-9,]
found 68 instances in kosha

All sample items found.

----------
python generate_random.py 5 pwg3 temp_pwg.txt index.txt check_pwg3_man.txt
regex_raw = Schol. zu <ls>KĀTY. ŚR. ([0-9]+),([0-9]+),([0-9]+)
found 75 instances in kosha


=================================================
Checks for all dictionaries after basicadjust updated.
NOT YET DONE !

These are checks for app1 (3 parameters)
----------------------------------------------------
First, pwg

python generate_random.py 5 pwg temp_pwg.txt index.txt check_pwg.txt
regex_raw = <ls>KĀTY. ŚR. ([0-9]+),([0-9]+),([0-9]+)
found 4629 instances in kosha

one NOT FOUND (schol. zu ...)

-----------------------------------
Random checks between pw , the pdf and index

python generate_random.py 5 pw temp_pw.txt index.txt check_pw.txt

regex_raw = <ls>KĀTY. ŚR. ([0-9]+),([0-9]+),([0-9]+)
found 511 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between pwkvn , the pdf and index

python generate_random.py 5 pwkvn temp_pwkvn.txt index.txt check_pwkvn.txt
regex_raw = <ls>KĀTY. ŚR. ([0-9]+),([0-9]+),([0-9]+)
found 58 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between sch , the pdf and index

python generate_random.py 5 sch temp_sch.txt index.txt check_sch.txt
regex_raw = <ls>Kāty. Śr. ([0-9]+),([0-9]+),([0-9]+)
found 78 instances in kosha

All in this random sample checked.

-----------------------------------
Random checks between mw , the pdf and index

python generate_random.py 5 mw temp_mw.txt index.txt check_mw.txt
regex_raw = <ls>KātyŚr. ([vix]+), *([0-9]+), *([0-9]+)
found 141 instances in kosha


All in this random sample checked.
  One not found, due to error in mw kosha  (different but similar err in pwg)
  
