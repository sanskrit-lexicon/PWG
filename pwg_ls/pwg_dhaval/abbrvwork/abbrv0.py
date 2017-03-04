# coding=utf-8
#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
""" abbrv0.py
 Reads pwg.xml, searches for the '<ls>' elements, and
 writes all of them 
 We remove 'key2' from output
 02-28-2017
"""

from lxml import etree # lxml.de
import re
import codecs
import datetime
import sys

"""
# Abbreviations of PWG
Run `makeabbrv.sh` from pywork/abbrvwork directory to regenerate the lists.

# Dependencies
[lxml](http://lxml.de/) to parse pwg.xml

# Logic
1. `<ls>something</ls>` tag usually holds the literary source data.

2. Output of all scripts are stored in abbrvoutput folder.

3. The text `something` is scraped via lxml and stored in abbrvlist.txt file (1st raw file).

4. abbrvlist.txt file still has some references which are pure numbers. We have discarded them as of now and stored them in purenumberabbrvlist.txt (byproduct). (See https://github.com/sanskrit-lexicon/PWK/issues/11 for details).

5. The list which is not pure numbers, but has some alphabet preceding it is stored in properrefs.txt (raw file 2).

6. The properrefs.txt file still has entries like `TA7N2D2JA-BR.25,13,3.` where the last entries are the canto / shloka number. They need to be removed.

7. The canto or shloka numbers are removed and only unique entries, sorted alphabetically are kept in cleanrefs.txt (raw file 3).

8. Errors usually come solo. Therefore, we have kept a code which sorts cleanrefs based on their occurrences. Sorted data is stored in sortedcrefs.txt. Sorting is done first based on number of occurrences and then alphabetically.

9. sortedcrefs.txt has the data is `ls@key1@key2@Lnumber@occurrence`.

10. It is difficult to read the `ls`, because it is in Anglisized Sanskrit. Therefore we add another field `lsinIAST@ls@key1@key2@Lnumber@occurrence` in  sortedcrefsiast.txt via `transcoder/as_roman.py` file.

11. The file `displayhtml.php` takes sortedcrefsiast.txt as input and gives the following output `SrNo-Lno-ReferenceinAS-ReferenceinIASTwithlinktowebpage-key1withlinktopdf-key2-counter`.

12. This file displayhtml.php would make it easy to locate the reference in dictionaries.

13. For corrections, copy the file `sortedcrefs.txt` as `finalabbrv.txt`. (This is not automated, because otherwise it may be overwritten if handled recklessly).

14. If there are errors found in HTML file, correct the `referenceinAS` in the finalabbrv.txt file.

15. If there is no error, place a ';' before the line in finalabbrv.txt.

16. Once the testing is over, run `python postprocess.py`. It would separate the file into change.txt and nochange.txt.

17. Jim would have to find a way to integrate these files into XML corrections.


# Improvements in statistics
1. First run - 3679 entries

2. After removing terminal period(.) i.e. `clean = clean.strip('.')` - 3341 entries
"""
def printtimestamp():
 # Function to return timestamp
 return datetime.datetime.now()

def scrapeabbrv(abbrvtag,entries,dictcode):
 """
 # Argument abbrvtag is the tag which contains literary resources data in the given XML file. 
 # For PWG, it is 'ls'.
 entries is parsed XML of pwg.xml
 """
 dictlo = dictcode.lower()
 # Scraped only elements in XML tree which have the abbrvtag.
 xpathfilter = ('/%s/H1/body/'% dictlo)+abbrvtag
 root = entries.xpath(xpathfilter) 
 wholeabbrvlist = []
 for elt in root:
  abbrvtext = elt.text
  key1 = elt.getparent().getparent().find('h/key1').text.strip()
  key2 = elt.getparent().getparent().find('h/key2').text.strip()
  lnum = elt.getparent().getparent().find('tail/L').text.strip()
  if abbrvtext == None:
   # A patch to overcome errors in windows for Nonetype.
   abbrvtext=""
  wholeabbrvlist.append((abbrvtext,key1,lnum))
 return wholeabbrvlist # Also return a list.

def parse_scrape(xmlfilename,tag,dictcode):
 print "Using xmlfile",xmlfilename
 print "Parsing started at", printtimestamp()
 entries = etree.parse(xmlfilename) # Parse xml
 print "Parsing ended at", printtimestamp()
 print
 print "Started scraping the abbreviations from %s.xml at "%dictcode, printtimestamp()
 print
 # Change the abbrvtag with suitable tag if you want to extend the code for other dictionaries.
 wholeabbrvlist = scrapeabbrv(tag,entries,dictcode)
 return wholeabbrvlist

if __name__ == "__main__":
 xmlfilename = sys.argv[1]  # e.g., ../pwg.xml
 fileout = sys.argv[2] # abbrvoutput/abbrvlist.txt
 wholeabbrvlist = parse_scrape(xmlfilename,"ls","pwg")
 print "Stored abbreviations in",fileout,"at", printtimestamp()
 print
 g = codecs.open(fileout, 'w','utf-8') # Opened file to store
 for w in wholeabbrvlist:
  # w = (a,b,d)
  out = '@'.join(w)
  g.write(out+'\n')
 g.close()
