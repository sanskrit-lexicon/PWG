## pwgbib1_orig.txt
Received from T. Malten, July 2016
cp1252  encoding (his usual encoding)
This contains abbreviations from volume 1 only.

corresponding images:
* [vol 1.1](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc_images/pwg1-0000--06.png)
* [vol 1.2](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc_images/pwg1-0000--08.png)
* [vol 1.3](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc/_images/pwg1-0000--09.png)
* [vol 1.4](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc/_images/pwg1-0000--10.png)
* [vol 1.5](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc/_images/pwg1-0000--11.png)

## pwgbib1_utf8.txt

Make the original file utf8 encoding, which is easier to work with.
```
python cp1252-to-utf8.py  pwgbib1_orig.txt pwgbib1_utf8.txt
```


## Conversion to Roman
```
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
```

# pwgbib23_orig.txt
Received July 13, 2016

Images:
* [vol 2.1](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc/_images/pwg2-0000--05.png)
* [vol 3.1](http://www.sanskrit-lexicon.uni-koeln.de/scans/csldoc/_images/pwg3-0000--03.png)

Make utf8 version:
```
python cp1252-to-utf8.py  pwgbib23_orig.txt pwgbib23_utf8.txt
```
Make roman version
```
python as_roman.py pwgbib23_utf8.txt pwgbib23_roman.txt
```

Thomas found some in volume 4.

pwgbib4_orig.txt is the original.

[vol4.1](http://www.sanskrit-lexicon.uni-koeln.de/scans/PWGScan/PWGScanpng/pwg4-1219--korabk.png) at page 1219 of volume 4.

pwgbib4_utf8.txt is the utf8 version.
```
python cp1252-to-utf8.py  pwgbib4_orig.txt pwgbib4_utf8.txt
```
Technical note:  The pwgbib4_orig file was actually transmitted to me from
Thomas within the body of an email; by contrast, the other two were transmitted
as email attachments.   Thus, the nature of the encoding of pwgbib4_orig.txt
MAY already be UTF8; I'm not sure.  Hopefully, this will cause no issues.

pwgbib4_roman.txt:
```
python as_roman.py pwgbib4_utf8.txt pwgbib4_roman.txt
```

### pwgbib14_roman.txt
(03-01-2017)
This is a concatenation of pwgbib1_roman.txt, pwgbib23_roman.txt, and
 pwgbib4_roman.txt.  However, some changes are made to promote uniformity.

python concat_roman.py pwgbib14_roman.txt

Format:
Each line has two parts:
v.nnn data
  where v is the volume number (1-4)
  nnn is 000 for 'meta' lines 
         sequence number within volume for non-meta lines
The 'data' has one of these forms:
 - [Page ...]   which indicates a page or page-column break 
 - [Volume v ...]  A Beginning of volume 
 - <H>...    a 'Header' line
Any of these forms are 'meta' lines.
 - <HI code="xxx">entry-data
   These lines are 'non-meta' lines.  In the digitization of the printed text,
   these are the actual literature reference lines.  They almost always
   (except for two cases) have the form X = Y.  We have duplicated the X part
   as 'xxx', with an aim to make it easier to identify the abbreviated
   literary source forms.
   Two other aspects of these non-meta (or entry) lines are:
    <lb> (line-break indicator).  In the text, some entries have descriptions
         that span multiple lines.  We gather all these together as part of
         one text line, but indicate the line-separation points by <lb>.
    [Page...]  In a few cases, a page-column break in the text occurs in the
         middle of a multiple-line entry.  In these cases, we have chosen
         to embed the [Page...] break within the extended <HI> line.

