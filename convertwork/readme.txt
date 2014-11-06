PWGScan/2013/pywork/convertwork/readme.txt
Nov 6, 2014

This provides an after-the-fact summary of the conversion of pwg digitization
to SLP1 transliteration.

The end product is pwg_orig_utf8_slp1.txt.
This file is computed by a single program, as follows:
python26 transcode.py 1 <pwg_orig_utf8.txt> pwg_orig_utf8_slp1.txt

This program uses a specialized transcoder file hk_slp1.xml.

Here is why this conversion SHOULD be easy:
 Devanagari Sanskrit in the original (pwg_orig_utf8.txt) digitization has
the form {#X#}, where X is in Harvard-Kyoto transliteration.  It is simple,
using the transcoder file hk_slp1.xml, to  change {#X#} to {#Y#} where Y is
the slp1 transcoding of X.  

It also should be easy to check this conversion by doing the inverse
conversion, using the slp1_hk.xml transcoding rules; this would convert
{#Y#} to {#X1#}, where X1 is again in HK transliteration.

Now, if all were simple and straightforward, then it should be the case that
always X1 is identical to X.

However, using this naive approach, with naive versions of the two transcoder
files leads to 100,000+ lines of the 266,000 lines of the digitization where 
some {#X#} disagrees with {#X1#}.


Why does this occur?

In the case of pwg, this is due almost entirely to a few typies
of frequently occurring nonstandard coding practices in {#X#}.
These include:
 - use of '|' for danda.  This is non-standard HK; the period '.' is standard,
   in both HK and SLP1.
 - use of periods in X to denote (a) the English punctuation mark or
    (in case of PWG) the 'nukta'.  
 - occurrence of page breaks [Pagexxx] as part of HK X.  


When transcode.py and the two transcoder files are adjusted for these
known oddities,  there only remain 8 cases where X1 differs from X;  these
are due to minor HK typos (P instead of ph, B instead of bh, E instead of ai).

So this describes the first good version of the slp1 version of PWG.

HOWEVER, it was decided to do two other additional adjustments in this step, 
in addition to the transcoding:
 (a) Correct the 'accent after M,H' error.  
 (b) Replace the ellipsis character occuring in braces {A

When (a) is done, there are 29 differences (21 more);  these are believed to
  be primarily due to cases where, in the original, an accent was correctly
  coded BEFORE M or H.
When (a) and (b) are both done, there are 167 differences; the additional
  cases are where the original digitization used a space rather than the usual
  ellipsis in braces.

The number of lines where this transcoding plus (a),(b) changes proves to 
be non-invertible (167 lines) is very small relative to the number of lines 
of the digitization  (266,000+ lines); thus this conversion is deemed to
be sufficiently accurate, and will be used as the basis of corrections
from now on.

Incidentally, all the previous corrections (from the missingByLine files) have
been adjusted and successfully applied to pwg_orig_utf8_slp1.  Two other
'sanity checks' provide confidence in pwg_orig_utf8_slp1: 
 - the list of headwords (pwghw2.txt) is identical to that computed from
   the HK version (pwg_orig_utf8.txt).
 - the xml file version (pwg.xml) differs by only 108 lines from the one
   computed from the HK version.

