version=$1
echo "version $version"
cp temp_pwg_$version.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
# ok  No problems noticed
cd /c/xampp/htdocs/sanskrit-lexicon/PWG/pwgissues/issue81
