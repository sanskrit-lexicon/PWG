issue94/readme.txt
02-10-2025 begun ejf
link target admin

Ref: https://github.com/sanskrit-lexicon/PWG/issues/94

This issue94 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue94

Begin with a copy of pwg.txt in csl-orig at commit
9dfc1998a78962ef82cec37184024e01353351b7

cd /c/xampp/htdocs/cologne/csl-orig
git show 9dfc1998:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue94/temp_pwg_0.txt

-------------------------------------------------
lsextract
02-10-2025
regenerate lsextract_all.txt from issue74
Ref: https://github.com/sanskrit-lexicon/PWG/blob/master/pwgissues/issue74/

link count summary for pwg
Refer: https://github.com/sanskrit-lexicon/PWG/tree/master/pwg_ls2/ak
lsextract_all.py

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ak/lsextract_all.py .
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/pwg/pywork/pwgauth/pwgbib_input.txt  .

python lsextract_all.py temp_pwg_0.txt pwgbib_input.txt lsextract_all.txt

-------------------------------------------------
python lsexamine1.py temp_pwg_0.txt pwgbib_input.txt lsexamine1.txt

python lsexamine2.py lsexamine1.txt lsexamine2.txt

grep -e '^\*' lsexamine2.txt > lsexamine2_summary.txt

-------------
-------------------------------------------------
-------------------------------------------------
