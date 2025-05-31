cp /c/xampp/htdocs/cologne/csl-orig/v02/pw/pw.txt temp_pw.txt

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pw/pywork/pwauth/pwbib_input.txt pwbib_input.txt

echo "... lsextract_all.txt"
python ../lsextract_all.py temp_pw.txt pwbib_input.txt lsextract_all_pw.txt

echo "... lsexamine1.txt"
python ../lsexamine1.py temp_pw.txt pwbib_input.txt lsexamine1_pw.txt

echo "... lsexamine2.txt"
python ../lsexamine2.py lsexamine1_pw.txt lsexamine2_pw.txt

echo "... lsexamine2_summary.txt"
grep -e '^\*' lsexamine2_pw.txt > lsexamine2_summary_pw.txt

python ../lsexamine3.py lsexamine1_pw.txt lsexamine3_pw.txt
