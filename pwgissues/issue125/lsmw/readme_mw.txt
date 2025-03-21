
Notes on mw references.

Śak.  is the literary source  abbreviation in mw.


285 matches for "<ls>Śak. " in buffer: temp_mw.txt

32 matches for "<ls>Śak. [0-9]+[^0-9,]" in buffer: temp_mw.txt

30 matches for "<ls>Śak. [0-9]+, [0-9]+" in buffer: temp_mw.txt


207 matches for "<ls>Śak. [iv]+" in buffer: temp_mw.txt

194 matches for "<ls>Śak. \(i\|ii\|iii\|iv\|v\|vi\|vii\), [0-9]" in buffer: temp_mw.txt

The 'verse' numbers restart at new  shloka

index question:  

There are at least 3 variants of Śak. references in mw
------------------------------
# Variant 1
'mw1':r'<ls>Śak. ([0-9]+)[^,])  (verse,)

# random sample
cd ../
python generate_random.py 5 mw2 temp_mw.txt index.txt lsmw/check_mw2.txt
cd lsmw
NOT FOUND ALL

# all instances of variant 1
python lsmw.py mw1 ../temp_mw.txt lsmw1.txt
found 30 distinct in kosha

------------------------------
# Variant 2
'mw2':r'<ls>Śāk. ([0-9]+), *([0-9]+)  (ipage,linenum)
cd ../
python generate_random.py 5 mw2 temp_mw.txt index.txt lsmw/check_mw2.txt
cd lsmw

NOT FOUND ALL

# all instances of variant 2
python lsmw.py mw2 ../temp_mw.txt lsmw2.txt
found 28 distinct in kosha

------------------------------
# Variant 3
'mw3':r'<ls>Śak. ([iv]+), ([0-9]+).*?</ls>',
i\|ii\|iii\|iv\|v\|vi\|vii  # 'aNka' 


python lsmw.py mw3 ../temp_mw.txt lsmw3.txt
found 117 distinct in kosha

