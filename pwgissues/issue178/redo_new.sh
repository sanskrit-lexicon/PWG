sfx=$1
home="/c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue178"
cd $home

cp temp_pwg_${sfx}.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt


cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg

cd /c/xampp/htdocs/cologne/csl-orig
git restore .

cd $home


