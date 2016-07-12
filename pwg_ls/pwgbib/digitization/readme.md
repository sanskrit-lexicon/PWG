
*  pwgbib1_orig.txt
Received from T. Malten, July 2016
cp1252  encoding (his usual encoding)
This contains abbreviations from volume 1 only.

* corresponding images:
[vol 1.1](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc_images/pwg1-0000--06.png)
[vol 1.2](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc_images/pwg1-0000--08.png)
[vol 1.3](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc/_images/pwg1-0000--09.png)
[vol 1.4](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc/_images/pwg1-0000--10.png)
[vol 1.5](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc/_images/pwg1-0000--11.png)

* pwgbib1_utf8.txt
Make the original file utf8 encoding, which is easier to work with.
python cp1252-to-utf8.py  pwgbib1_orig.txt pwgbib1_utf8.txt

* Abbreviations from other volumes
[vol 2.1](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc/_images/pwg2-0000--05.png)
[vol 3.1](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc/_images/pwg3-0000--03.png)
These have not been digitized yet (as of Jul 9, 2016), but are expected to be
available soon.


* Conversion to Roman
step 1.  check what AS (number-letter) codings and EA (Extended ascii codings)
are present.
python check_as_ea.py pwgbib1_utf8.txt pwgbib1_check_as_ea.txt
step 2. construct as_roman1.xml to 
  (a) deal with the AS codings mentioned pwgbib1_check_as_ea.txt
  (b) deal with a couple of other peculiar codings:
      J -> Y,  j -> y  
      SH -> Ṣ, sh -> ṣ
      Ç -> Ś, ç -> ś
NOTE: python tranwork.py was used to change the \uxxxx form of unicode
    in a PW version of as_roman.xml, to UTF-8 encoded unicode in the
    as_roman.xml file used here.  Then, this file was modified as 
    mentioned in step2.  It is the transcoding file used in step 3 next.
step 3. transcode pwgbib1 to roman:
python as_roman.py pwgbib1_utf8.txt pwgbib1_roman.txt

step4.  (NOT REQUIRED. JUST FOR INFORMATION)
python traninvert.py as_roman.xml roman_as.xml
  Just invert the transcoder file.
python roman_as.py pwgbib1_roman.txt pwgbib1_as.txt
diff -w pwgbib1_utf8.txt pwgbib1_as.txt
 NOTE: There are 928 lines in the diff.  Extremely brief  examination suggests
  that the diffs occur in the German involving 'c'
  'Gedruckte' in pwgbib1_roman.txt, gets converted by roman_as.py to
  'Gedruk4kte'.  
 NOTE2: At the moment, it does not seem required to worry about this
    lack of invertibility of the transcoding from AS to roman.
