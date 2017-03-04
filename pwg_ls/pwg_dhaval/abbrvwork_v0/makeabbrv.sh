PWG=../../../../pwgxml/pwg.xml
if !([ -e $PWG ])
 then
  echo "path to PWG does not exist: $PWG"
  echo "See pwg_dhaval/readme.md for where to get pwg.xml"
  exit 1
fi

python abbrv.py $PWG
echo "Converting the Anglicized Sanskrit to IAST"
echo 
python transcoder/as_roman.py abbrvoutput/sortedcrefs.txt abbrvoutput/sortedcrefsiast.txt as roman
echo "Preparing dislpay.html for viewing."
php displayhtml.php abbrvoutput/sortedcrefsiast.txt abbrvoutput/display.html 1


