vers=$1
file=temp_pwg_${vers}.txt
echo $file

cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue189x
cp $file /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
cd /c/xampp/htdocs/cologne/csl-orig/
git restore v02/pwg/pwg.txt
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue189x
