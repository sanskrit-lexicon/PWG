# coding=utf-8
""" make_js_index.py for ŚAT. BR.	The ŚATAPATHABRĀHMAṆA
"""
from __future__ import print_function
import sys, re, codecs
import json

def roman_to_int(roman):
 droman_int = {'I':1, 'II':2, 'III':3, 'IV':4,
                'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9,
                'X':10, 'XI':11, 'XII':12,'':0}
 if roman in droman_int:
  return droman_int[roman]
 else:
  # error condition
  return None

 # global parameters
parm_regex_split = '\t' #    r'[ ]+'
parm_numcols = 6
parm_numparm = 4 
parm_vol = r'^(I|II|III)$'
parm_page = r'^([0-9]+)$'
parm_kand = r'^([0-9]+)$'
parm_adhy = r'^([0-9]+)$'
parm_fromv = r'^([0-9]+)([b])?$'  # कण्डिका
parm_tov = r'^([0-9]+)([ab])?$'   # line 42 from=20b, to=20b
parm_ipage = r'^([0-9]+)$'   # not used
parm_vpstr_format = '%04d'

class Pagerec(object):
 """
Format of SAT.index.txt
page	kand.	adhy.	brāhm.	from kaṇḍ.	to kaṇḍ.	ipage
288	3	4	4	26b	27	267
288	3	5	1	1	10a	267

Note the first line (column names) is ignored
""" 
 def __init__(self,line,iline):
  line = line.rstrip('\r\n')
  self.line = line
  self.iline = iline
  parts = re.split(parm_regex_split,line)
  self.status = True  # assume all is well
  self.status_message = 'All is ok'
  if len(parts) != parm_numcols:
   self.status = False
   self.message = 'Expected %s values. Found %s value' %(parm_numcols,len(parts))
   return
  # give names to the column values
  raw_vol = parts[0]
  raw_page = parts[1] # pdf external page number
  raw_kand = parts[2]
  raw_adhy = parts[3]
  raw_fromv = parts[4]
  raw_tov = parts[5]
  #raw_ipage = parts[6]
  # check vol
  m_vol = re.search(parm_vol,raw_vol)
  if m_vol == None:
   self.status = False
   self.status_message = 'Unexpected Volume: %s' % raw_vol
   return
  # check page 
  m_page = re.search(parm_page,raw_page)
  if m_page == None:
   self.status = False
   self.status_message = 'Unexpected page: %s' % raw_page
   return
  # check kand
  m_kand = re.search(parm_kand,raw_kand)
  if m_kand == None:
   self.status = False
   self.status_message = 'Unexpected kand: %s' % raw_kand
   return
  # check adhy
  m_adhy = re.search(parm_adhy,raw_adhy)
  if m_adhy == None:
   self.status = False
   self.status_message = 'Unexpected adhy: %s' % raw_adhy
   return
  """
  # check brahm
  m_brahm = re.search(parm_brahm,raw_brahm)
  if m_brahm == None:
   self.status = False
   self.status_message = 'Unexpected brahm: %s' % raw_brahm
   return
  """
  # check fromv कण्डिका
  m_fromv = re.search(parm_fromv,raw_fromv)
  if m_fromv == None:
   self.status = False
   self.status_message = 'Unexpected fromv: %s' % raw_fromv
   return
  # check tov कण्डिका
  m_tov = re.search(parm_tov,raw_tov)
  if m_tov == None:
   self.status = False
   self.status_message = 'Unexpected tov: %s' % raw_tov
   return
 
  # set self.page as integer
  self.page = int(m_page.group(1))
  # set self.kand as integer
  self.kand = int(m_kand.group(1))
  # set self.adhy as integer
  self.adhy = int(m_adhy.group(1))
  """
  # set self.brahm as integer
  self.brahm = int(m_brahm.group(1))
  """
  # set self.fromv as integer
  self.fromv = int(m_fromv.group(1))
  x1 =  m_fromv.group(2)
  if x1 == None:
   self.fromvx = ''
  else:
   self.fromvx = x1;
  # set self.tov as integer
  self.tov = int(m_tov.group(1))
  x2 =  m_tov.group(2)
  if x2 == None:
   self.tovx = ''
  else:
   self.tovx = x2;
  """
  # set self.ipage as integer
  m_ipage = re.search(parm_ipage,raw_ipage)
  self.ipage = int(m_ipage.group(1))
  """
  # vpstr  # format consistent with format of filename of scanned page
  self.vpstr = parm_vpstr_format % self.page
  # make keys for checking. tuple of ints
  self.fromkey = (self.kand,self.adhy,self.fromv)
  self.tokey   = (self.kand,self.adhy,self.tov)
 def todict(self):
  if self.fromvx == None:
   self.fromx = ''
  e = {
   'page':int(self.page),
   'kand':int(self.kand),
   'adhy':int(self.adhy),
   'v1':int(self.fromv), 'v2':int(self.tov),
   'x1':self.fromvx, 'x2':self.tovx, 'vp':self.vpstr
  }
  return e

def init_pagerecs(filein):
 """ filein is a csv file, with first line as fieldnames
 """
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for iline,line in enumerate(f):
   if (iline == 0):
    # assert line.startswith('volume') # skip column-title line
    # print('Skipping column title line:',line)
    continue
   pagerec = Pagerec(line,iline)
   if pagerec.status:
    # No problems noted
    recs.append(pagerec)
   else:
    lnum = iline + 1
    print('Problem at line # %s:' % lnum)
    print('line=',line)
    print('message=',pagerec.status_message)
    exit(1)
 print('%s Page records read from %s' % (len(recs),filein))
 return recs

def make_js(recs):
 outarr = []
 outarr.append('indexdata = [')
 arr = [] # array of Python dicts
 for rec in recs:
  d = rec.todict()  # a Python dictionary
  arr.append(d)
 return arr

def write_recs(fileout,data):
 with codecs.open(fileout,"w","utf-8") as f:
  f.write('indexdata = \n')
  jsonstring = json.dumps(data,indent=1)
  f.write( jsonstring +  '\n')
  f.write('; // end of indexdata\n')
  
 print('json data written to',fileout)

def check1_hierarchy(pagerecs):
 # records assumed lexicographically ordered
 prev = None
 for irec,rec in enumerate(pagerecs):
  lnum = rec.iline + 1
  line = rec.line
  if irec == 0:
   # first record has all parameters = 1
   if rec.fromkey != (1,1,1,1):
    print('check1_hierarchy: first key not 1.')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
   prev = rec
   continue
  if prev.fromkey[0:3] == rec.fromkey[0:3]:
   # nothing to check
   prev = rec
   continue
  if prev.fromkey[0:2] == rec.fromkey[0:2]:
   if ( ((prev.fromkey[2] + 1) != rec.fromkey[2]) or
        (rec.fromkey[3] != 1)):
    print('check1_hierarchy: parm#3 error')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
   prev = rec
   continue
  if prev.fromkey[0:1] == rec.fromkey[0:1]:
   if ( ((prev.fromkey[1] + 1) != rec.fromkey[1]) or
        (rec.fromkey[2:4] != (1,1)) ):
    print('check1_hierarchy: parm#2 error')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
   prev = rec
   continue
  if ( ((prev.fromkey[0] + 1) != rec.fromkey[0]) or
        (rec.fromkey[1:4] != (1,1,1)) ):
    print('check1_hierarchy: parm#1 error')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
  prev = rec
  continue
  
 print('pagerecs passes check1_hierarchy ')
 
def check1_key(pagerecs):
 for irec,rec in enumerate(pagerecs):
  lnum = rec.iline + 1
  line = rec.line
  if not (rec.fromkey <= rec.tokey):
    print('ERROR fromkey %s > tokey %s.' % (rec.fromkey,rec.tokey))
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
 print('pagerecs passes check1_key')
 
def check1(pagerecs):
 """ check that v1 = v2_prev + 1 when 
 """
 check1_key(pagerecs)
 check1_hierarchy(pagerecs)

if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 pagerecs = init_pagerecs(filein)
 outrecs = make_js(pagerecs)
 write_recs(fileout,outrecs)
 check1(pagerecs)
 
 
