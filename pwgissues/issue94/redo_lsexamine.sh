cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt temp_pwg_0.txt

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt pwgbib_input.txt

echo "... lsextract_all.txt"
python lsextract_all.py temp_pwg_0.txt pwgbib_input.txt lsextract_all.txt

echo "... lsexamine1.txt"
python lsexamine1.py temp_pwg_0.txt pwgbib_input.txt lsexamine1.txt

echo "... lsexamine2.txt"
python lsexamine2.py lsexamine1.txt lsexamine2.txt

echo "... lsexamine2_summary.txt"
grep -... '^\*' lsexamine2.txt > lsexamine2_summary.txt


echo "... lsexamine3.txt"
python lsexamine3.py lsexamine1.txt lsexamine3.txt

