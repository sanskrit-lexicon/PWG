# coding=utf-8
#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
# abbrv3.py
import re
import codecs
import datetime
import sys

from clean_proper import clean_one_properref  # Feb 16, 2016
def printtimestamp():
 return datetime.datetime.now()

class Bibrec(object):
 d = {}  # dictionary with key = code
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  m = re.search(r'^(.*?) (.*)$',line)
  lineid = m.group(1)
  body = m.group(2)
  self.lineid=lineid
  # entryflag indicates to caller that this record is/is-not an entry record
  self.entryflag=False 
  if lineid == '1.000':
   return
  m = re.search(r'<HI code="(.*?)">(.*)$',body)
  if not m:
   # [Page...],
   # [Volume...]
   return 
  self.code = m.group(1)
  self.text = m.group(2)
  if self.code == 'None':
   print "Bibrec skipping None code:"
   print self.line.encode('utf-8')
   return
  self.code_orig=self.code # save original in case we need it elsewhere
  if self.code.startswith('*'):
   # leading asterisk has some meaning in Bibliography
   # but is not needed for matching
   #print "Bibrec: removing asterisk from",self.code.encode('utf-8')
   self.code = self.code[1:] 
  # some codes are of form A oder B. Replace these with A
  m = re.search(r'^(.*?) oder (.*?)$',self.code)
  if m:
   self.code = m.group(1)
  # update dictionary
  if self.code in Bibrec.d:
   print "Bibrec skip duplicate code:",self.code.encode('utf-8'),self.lineid
   print "Previous lineid with this code is",Bibrec.d[self.code].lineid
   return
  Bibrec.d[self.code] = self
  self.entryflag = True
  self.used = False  # do any references match to this one?

def init_bibrecs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs=[]
  for x in f:
   rec = Bibrec(x)
   if rec.entryflag:
    recs.append(rec)
 return recs

class Match(object):
 def __init__(self,cref):
  (self.a,self.b,self.c) = cref
  self.type=None
  self.bibrec = None

 def match_special_exact(self,bibrecs):
  specials = {
   u'BURNOUF, Intr.':u'BURN. Intr.',
  }
  abbrv = self.a
  if abbrv not in specials:
   return
  abbrv1 = specials[abbrv]
  if abbrv1 not in Bibrec.d:
   out = "match_special_exact error 1:%s" %abbrv1
   print out.encode('utf-8')
   exit(1)
  self.type = '=!'
  self.bibrec = Bibrec.d[abbrv1]

 def match_special_error(self,bibrecs):
  # Matches after correction to errors in pwg.txt
  specials = {
   '':'',
  }
  abbrv = self.a
  if abbrv not in specials:
   return
  abbrv1 = specials[abbrv]
  assert abbrv1 in Bibrec.d,"match_special_exact error 1:%s" %abbrv1.encode('utf-8')
  self.type = '=!'
  self.bibrec = Bibrec.d[abbrv1]

 def match_special_startswith(self,bibrecs):
  specials = [
   (u'MĀLATĪM',u'MĀLAT.'),
   (u'MAITRYUP',u'MAITR. UP.'),
   (u'SIDDH.K',u'SIDDH. K.'), (u'SIDDH K.',u'SIDDH. K.'),
   (u'NIGH. PR',u'NIGH. PR.'),
   (u'YAJ. V.',u'YAJ. V.'), (u'YAJURVEDA',u'YAJ. V.'),
   (u'CATURBH.',u'CATURBH.'),
   (u'KAIV. UP.','KAIV. UP.'),('KAIV. Up.',u'KAIV. UP.'),
      (u'KAIVAIYOP.',u'KAIV. UP.'),
   (u'HAUGHTON',u'HAUGHTON'),
   (u'AMṚTAV',u'AMṚTAV. UP.'),(u'AMṚTAB',u'AMṚTAV. UP.'),
   (u'H. an.',u'H. an.'),
   (u'UTTARAR',u'UTT. RĀMAC.'),
   (u'HIOUEN-THSANG I',u'HIOUEN-THSANG I'),
    (u'HIOUEN- THSANG I',u'HIOUEN-THSANG I'),
     (u'HIOUEN-THSANG',u'HIOUEN-THSANG'),
     (u'HIOUEN- THSANG',u'HIOUEN-THSANG'),
     (u'HIOUEN - THSANG',u'HIOUEN-THSANG'),
     (u'HIOUEN',u'HIOUEN-THSANG'),
    (u'ANUP',u'ANUP. S.'),
    (u'ĀRUṆ. UP.',u'ĀRUṆ. UP.'),
    (u'BHAV. P.',u'BHAV. P.'),
    (u'BṚH. ĀR. UP. ed. POLEY',u'BṚH. ĀR. UP. (POL.)'),
    (u'ŚATAR. UP.',u'ŚATAR. UP.'),
    (u'ŚAUNAKA',u'ŚAUN. CAT.'),
    (u'DATTAKAM',u'DATT. MĪM.'),
    (u'JĀB. UP.',u'JĀB. UP.'),
     (u'JĀB. Up.',u'JĀB. UP.'),
     (u'JĀBĀLOP',u'JĀB. UP.'),
    (u'GOT',u'GOT. S.'),
    (u'WILSON, Hindu Th.',u'Hindu Th. (WILSON)'),
    (u'LASSEN, Institt.',u'Institutt. (LASSEN)'),
    (u'LASSEN. Institt.',u'Institutt. (LASSEN)'), # spelling
    (u'LASSEN, Pentap.',u'Pent. (LASSEN)'),
    (u'MBH. bei LASSEN',u'Pent. (LASSEN)'),
    (u'YAJÑAD',u'YAJÑAD. (LOIS.)'),
    (u'KOSEG.',u'KOS.'),
    (u'SCHIEFNER, Lebensb.',u'Lebensb. (SCHIEFNER)'),
    (u'SCHIEFNER. Lebensb.',u'Lebensb. (SCHIEFNER)'),
    (u'MĀDHY',u'MĀDHY. Rec.'),
    (u'MĀṆD. UP.',u'MĀṆD. UP.'),
    (u'AINSLIE',u'Mat. ind. (AINSLIE)'),
    (u'REINAUD, Mém.',u"Mém. sur l'Inde (REINAUD)"),
    (u'REINAUD. Mém.',u"Mém. sur l'Inde (REINAUD)"),
    (u'NIDĀNA',u'NIDĀNA-S.'),
    (u'PADAP',u'Padap.'),
    (u'RAGH. ed. Calc.',u'RAGH. (ed. Calc.)'),
    (u'SADDH. L',u'SADDH. L.'),
    (u'SADDH. P',u'SADDH. P. 4.'), # There is another version in bib
    (u'SARVOP. S.',u'SARVOP. S.'),
    (u'SIDDHĀNTAM',u'SIDDHĀNTAM.'),
    (u'TS. ANUKR.',u'TS. ANUKR.'),
    (u'Z. d. m. G.',u'Z. d. d. m. G.'),
    (u'ZdmG',u'Z. d. d. m. G.'),
    (u'ROTH Zur L',u'Zur L. u. G. d. w. (ROTH)'),
    (u'DURGĀRCĀT',u'DURGĀRCĀT'), # mentioned indirectly.
    (u'GILD. Bibl.',u'GILD. Bibl.'),
    (u'GILD',u'GILD.'),
    (u'GOBH',u'GOBH.'),
    (u'KṢURIKOPAN',u'KṢUR. UP.'),
    (u'NĀRĀYAṆACAKR',u'NĀRĀYAṆACAKR.'),
    (u'PARAM',u'PARAM. UP.'),
    (u'UP.',u'UP. und UPAK.'),
    (u'UPAK.',u'UP. und UPAK.'),
    (u'VĀR. P.',u'VĀR. P.'),
    (u'VĀRĀHA-P',u'VĀR. P.'),
    (u'VĀRĀHA P',u'VĀR. P.'),
    (u'VIVĀDĀRṆ',u'VIVĀDĀRṆ.'),
    (u'KĀPIŚĀV.',u'KĀPĪŚĀV.'), # spelling problem somewhere
    (u'PĀŚAKAKEV',u'PĀŚAKAK.'), # not currently separate LS
    (u'BANERYEA',u'BANERYEA und BANERYEA, Dial.'),
    (u'Verz. d. B. H.',u'Verz. d. B. H.'),
    (u'AK.',u'AK.'),
  ]
  abbrv = self.a
  abbrv1 = None
  for old,new in specials:
   if abbrv.startswith(old):
    abbrv1 = new
    break
  if abbrv1 == None:
   return
  if abbrv1 not in Bibrec.d:
   out = "match_special_startswith error 1:%s" %abbrv1
   print out.encode('utf-8')
   exit(1)
  self.type = '~!'
  self.bibrec = Bibrec.d[abbrv1]

 def match_one(self,bibrecs):
  # Exact match
  abbrv = self.a
  if abbrv in Bibrec.d:
   self.type='='
   self.bibrec = Bibrec.d[abbrv]
   return
  # Special, adhoc matches
  self.match_special_exact(bibrecs)
  if self.type != None:
   return
  # Special, startswith
  self.match_special_startswith(bibrecs)
  if self.type != None:
   return
  # Approximate match, differing only by a period
  if (not abbrv.endswith('.')):
   abbrv1 = abbrv + '.'
   if abbrv1 in Bibrec.d:
    self.type='~'
    self.bibrec = Bibrec.d[abbrv1]
    return
  # remove roman-numerals to end
  abbrv1 = re.sub(r'[ IXVL,]+$','',abbrv)
  if abbrv1 in Bibrec.d:
   self.type='=RN'
   self.bibrec = Bibrec.d[abbrv1]
   return

  # Match on first word only
  aparts = re.split(r' +',self.a)
  abbrv = aparts[0] # first word
  if abbrv in Bibrec.d:
   self.type='=1'
   self.bibrec = Bibrec.d[abbrv]
   return
  # Look for a few 'embedded forms'
  abbrv = self.a
  if u' im ŚKDR' in abbrv:
   abbrv1 = u'ŚKDR.'
   self.type='~2'
   self.bibrec = Bibrec.d[abbrv1]
   return
  if abbrv.startswith('BENFEY'):
   # assume it is this collection of stories
   abbrv1 = u'BENF. Chr.'
   self.type='~2'
   self.bibrec = Bibrec.d[abbrv1]
   return
def match(crefs,bibrecs):
 recs=[] # returned list of Match objects
 for cref in crefs:
  # fields: 
  #   cleaned abbreviation in roman
  #   cleaned abbreviation in AS
  #   count
  mrec = Match(cref)
  mrec.match_one(bibrecs)
  if mrec.type != None:
   mrec.bibrec.used = True
  recs.append(mrec)
 return recs

def stats(matchrecs):
 cmatch=0
 nmatch=0
 nnomatch=0
 cnomatch=0
 for mrec in matchrecs:
  #(bibrec,a,b,c)
  bibrec = mrec.bibrec
  c = mrec.c
  ic = int(c)
  if bibrec == None:
   nnomatch = nnomatch+1
   cnomatch = cnomatch +  ic
  else:
   nmatch = nmatch+1
   cmatch = cmatch +  ic
 print "stats"
 print "matches: %4d records, %6d instances" %(nmatch,cmatch)
 print " misses: %4d records, %6d instances" %(nnomatch,cnomatch)

def stats_bibrec(bibrecs):
 fileout = "abbrvoutput/pwgbib14_usage.txt"
 f = codecs.open(fileout,"w","utf-8")
 nused = 0
 for bibrec in bibrecs:
  if bibrec.used:
   status = 'USED  '
   nused = nused+1
  else:
   status = 'UNUSED'
  out = status + ' ' + bibrec.line
  f.write(out+'\n')
 print len(bibrecs),"records written to",fileout
 print nused,"of these records used in matching"

if __name__ == "__main__":
 filein = sys.argv[1]  # abbrvoutput/sortedcrefs.txt
 filein1 = sys.argv[2] # pwgbib14_roman.txt
 filematch = sys.argv[3] # abbrvoutpu/matchcrefs.txt
 # read and parse filein
 with codecs.open(filein,"r","utf-8") as f:
  # fields: 
  #   cleaned abbreviation in roman
  #   cleaned abbreviation in AS
  #   count
  crefs = [x.rstrip('\r\n').split('@') for x in f]
 print len(crefs)
 # read pwgbib14
 bibrecs = init_bibrecs(filein1)
 print len(bibrecs),"records from",filein1
 # match crefs to bibrecs
 matchrecs = match(crefs,bibrecs)
 stats(matchrecs)
 stats_bibrec(bibrecs)
 with codecs.open(filematch,"w","utf-8") as f:
  for mrec in matchrecs:
   if mrec.type == None:
    x = "No Match"
   else:
    bibrec = mrec.bibrec
    x = "Match %s %s %s" %(mrec.type,bibrec.lineid, bibrec.code)
   ic = int(mrec.c)
   cs = "%5d"%ic
   y = (cs,x,mrec.a,mrec.b)
   #y = (proman,p,str(c)) # c is an int
   out = '@'.join(y)
   f.write(out+'\n')
