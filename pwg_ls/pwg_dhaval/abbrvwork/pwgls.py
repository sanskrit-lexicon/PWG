""" pwgls.py
    03-03-2017
    Uses module abbrv0, which depends on lxml
"""
import re,codecs,datetime,sys
import abbrv0,abbrv1,abbrv3,abbrv4
from clean_proper import clean_one_properref 
printtimestamp = abbrv0.printtimestamp

def compute_clean(refs):
 cleanrefs = []
 #print "computing cleanrefs begins at",printtimestamp()
 for (a,b,d) in properrefs:
  clean=clean_one_properref(a,b,d)
  # keep both clean and unclean. In abbrv3, unclean ('a') is dropped
  cleanrefs.append((clean,a,b,d)) 
 return cleanrefs

class Match(abbrv4.Match):
 # The initializer here expects a 4-tuple, while
 # that in abbrv4.Match expects 3
 def __init__(self,cref):
  # cref =  clean,abbrvtext,key1,lnum
  # abbrv4.Match expects fields: promanabbrv,abbrvtext,count
  # computer proman
  (clean,abbrvtext,key1,lnum) = cref
  proman = abbrv3.abbrv_transcode(clean)
  cref_abbrv4 = (proman,clean,0)
  # apply init of abbrv4.Match
  # this uses Python 2 syntax
  # ref : http://stackoverflow.com/questions/2399307/how-to-invoke-the-super-constructor
  #(self.a,self.b,self.c) = cref
  super(Match,self).__init__(cref_abbrv4)
  # now: self.a = proman, self.b = clean, self.c = 0
  # add rest of attributes from cref
  # also, self.type and self.bibrec are None
  self.abbrvtext = abbrvtext
  self.key1=key1
  self.lnum = lnum

def match(crefs,bibrecs):
 # this is the same as in abbrv4. But 'Match' uses our Match
 recs=[] # returned list of Match objects
 for cref in crefs:
  mrec = Match(cref)
  mrec.match_one(bibrecs)
  if mrec.type != None:
   mrec.bibrec.used = True
  recs.append(mrec)
 return recs

def unique_match(mrecs):
 # keep only a sample that has all mrec.abbrvtext variants; i.e., discard
 # duplicates.
 # Also, for the representative, calculate mrec.c as the count of same
 ans = [] # returned array
 d = {} # the distinct abbrvtext keys
 for mrec in mrecs:
  abbrvtext = mrec.abbrvtext
  if abbrvtext not in d:
   d[abbrvtext] = mrec
   mrec.c = 1  # initalize count. 
   ans.append(mrec)
  else:
   mrec1 = d[abbrvtext]
   mrec1.c = mrec1.c + 1
 return ans

def output(umatchrecs,fileout):
 # filter those that match to pwgbig
 matches = [mrec for mrec in umatchrecs if mrec.type != None]
 # sort these matches by the bibrec.lineid
 matches.sort(key=lambda x: x.bibrec.lineid)
 with codecs.open(fileout,"w","utf-8") as f:
  nout = 0
  nc = 0 # 
  for mrec in matches:
   bibrec = mrec.bibrec # not None since mrec.type is not None
   # make the value as bibrec.lineid, to avoide problems with the
   # few duplicate codes of pwgbib.
   out = "%d\t%s\t%s\t%s" %(mrec.c,mrec.abbrvtext,bibrec.lineid,bibrec.code)
   f.write(out + '\n')
   nout = nout + 1
   nc = nc + mrec.c
 print nout,"records written to",fileout
 print nc,"total abbrvlist records will be matched for ls"

if __name__ == "__main__":
 xmlfilename = sys.argv[1]  # e.g., ../pwg.xml
 filebib = sys.argv[2]
 fileout = sys.argv[3] # abbrvoutput/abbrvlist.txt
 tag = "ls"
 dictcode = "pwg"
 # Generate list of all abbreviation texts
 # abbrvlist fields: abbrvtext,key1,lnum
 abbrvlist = abbrv0.parse_scrape(xmlfilename,tag,dictcode)
 print len(abbrvlist),"total %s elements from %s" %(tag,dictcode)
 # Separate wholeabbrvlist into proper and improper parts
 (numrefs,properrefs) = abbrv1.segregatepurenumbers(abbrvlist)
 print len(properrefs),"Proper abbreviations chosen from abbrvlist"
 print len(numrefs),"Improper abbreviations will be ignored"
 # clean the abbreviations
 # crefs fields: clean,abbrvtext,key1,lnum
 crefs = compute_clean(properrefs)
 print len(crefs),"clean refs"
 # read pwgbib14
 bibrecs = abbrv4.init_bibrecs(filebib)
 print len(bibrecs),"records from",filebib
 # match crefs to bibrecs
 matchrecs = match(crefs,bibrecs)
 print len(matchrecs),"match records"
 # generate unique records with regard to original abbrvtext.
 umatchrecs = unique_match(matchrecs)
 print len(umatchrecs),"unique match records"
 # generate output
 output(umatchrecs,fileout)

