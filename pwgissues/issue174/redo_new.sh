sfx=$1
home="/c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue174"
cd $home || exit 1

cp temp_pwg_${sfx}.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt


cd /c/xampp/htdocs/cologne/csl-pywork/v02 || exit 1
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg

cd /c/xampp/htdocs/cologne/csl-orig || exit 1
git restore .

cd $home || exit 1


