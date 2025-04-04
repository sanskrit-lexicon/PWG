# coding=utf-8
""" make_js_index.py for ramayana_bom
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
parm_numcols = 7
parm_numparm = 4 
parm_vol = r'^(I|II|III)$'
parm_page = r'^([0-9]+)$'
parm_kand = r'^([0-9]+)$'
parm_sarga = r'^([0-9]+)$'
parm_sargap = r'^([0-9]+)[.]([0-9]+)$'
parm_fromv = r'^([0-9]+)$'  # कण्डिका
parm_tov = r'^([0-9]+)$'   # line 42 from=20b, to=20b
parm_ipage = r'^([0-9]+)([ab])?$'   # not used
parm_vpstr_format = '%d%03d'  #VPPP

class Pagerec(object):
 """
Format of index
VOL page	kand.	adhy.	brāhm.	from kaṇḍ.	to kaṇḍ.	ipage

III	578	7	23	52	53	37b	
III	578	7	23.1	1	15	37b	

""" 
 def __init__(self,line,iline):
  line = line.rstrip('\r\n')
  self.line = line
  self.iline = iline
  parts0 = re.split(parm_regex_split,line)
  parts = parts0[0:7]  # exclude remarks
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
  raw_sarga = parts[3]
  raw_sargap = None # section for prakshipta
  raw_fromv = parts[4]
  raw_tov = parts[5]
  raw_ipage = parts[6]
  # self.vol
  if raw_vol in ('I','II','III'):
   self.vol = roman_to_int(raw_vol)
  else:
   self.status = False
   self.status_message = 'Unexpected vol: %s' % raw_vol
   return
  # self.page
  if raw_page == '---':
   raw_page = '0' # ?
  elif raw_page.endswith(('x','y')):
   print('raw_page dropping last character',raw_page[-1])
   raw_page = raw_page[0:-1]  # drop
  m_page = re.search(parm_page,raw_page)
  if m_page == None:
   self.status = False
   self.status_message = 'Unexpected page: %s' % raw_page
   return
  else:
   self.page = int(raw_page)
  # self.kand
  if raw_kand == '---':
   raw_kand = '0'
  m_kand = re.search(parm_kand,raw_kand)
  if m_kand == None:
   self.status = False
   self.status_message = 'Unexpected kand: %s' % raw_kand
   return
  else:
   self.kand = int(raw_kand)
 
  # sarga and sargap
  if raw_sarga == '---':
   raw_sarga = '0'
  m_sargap = re.search(parm_sargap,raw_sarga)
  if m_sargap:
   self.sarga = int(m_sargap.group(1))
   self.sargap = int(m_sargap.group(2))
  else:
   m_sarga = re.search(parm_sarga,raw_sarga)
   if m_sarga != None:
    self.sarga = int(raw_sarga)
    self.sargap = 0
   else:
    self.status = False
    self.status_message = 'Unexpected sarga: %s' % raw_sarga
    return
  # fromv
  if raw_fromv == '---':
   raw_fromv = '0'
  if raw_fromv.endswith(('a','b')):
   print('dropping last character of',raw_fromv,'line=',line)
   raw_fromv = raw_fromv[0:-1]
  m_fromv = re.search(parm_fromv,raw_fromv)
  if m_fromv == None:
   self.status = False
   self.status_message = 'Unexpected fromv: %s' % raw_fromv
   return
  self.fromv = int(raw_fromv)
  # tov
  if raw_tov == '---':
   raw_tov = '0'
  if raw_tov.endswith(('a','b')):
   print('dropping last character of',raw_tov,'line=',line)
   raw_tov = raw_tov[0:-1]
  m_tov = re.search(parm_tov,raw_tov)
  if m_tov == None:
   self.status = False
   self.status_message = 'Unexpected tov: %s' % raw_tov
   return
  self.tov = int(raw_tov)
  # ipage
  if raw_ipage == '---':
   raw_ipage = '0'
  m_ipage = re.search(parm_ipage,raw_ipage)
  if m_ipage == None:
   self.status = False
   self.status_message = 'Unexpected ipage: %s' % raw_ipage
   return
  self.ipage = raw_ipage
  # vpstr  # format consistent with format of filename of scanned page
  self.vpstr = parm_vpstr_format % (self.vol,self.page)
  # make keys for checking. tuple of ints
  self.fromkey = (self.kand,self.sarga,self.sargap,self.fromv)
  self.tokey   = (self.kand,self.sarga,self.sargap,self.fromv)
 def todict(self):
  #if self.fromvx == None:
  # self.fromx = ''
  e = {
   # 'page':int(self.page), # implied in 'vp'
   'kand':int(self.kand),
   'sarga':int(self.sarga),
   'sargap':int(self.sargap),
   'v1':int(self.fromv), 'v2':int(self.tov),
   'vp':self.vpstr
  }
  return e

def init_pagerecs(filein):
 """ filein is a tsv file, with first line as fieldnames
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
    print('WARNING: check1_hierarchy: first key not 1.',rec.fromkey)
    print('lnum=%s, line=%s' % (lnum,line))
    # exit(1)
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
    # exit(1)
   prev = rec
   continue
  if prev.fromkey[0:1] == rec.fromkey[0:1]:
   if ( ((prev.fromkey[1] + 1) != rec.fromkey[1]) or
        (rec.fromkey[2:4] != (1,1)) ):
    print('check1_hierarchy: parm#2 error')
    print('lnum=%s, line=%s' % (lnum,line))
    #exit(1)
   prev = rec
   continue
  if ( ((prev.fromkey[0] + 1) != rec.fromkey[0]) or
        (rec.fromkey[1:4] != (1,1,1)) ):
    print('check1_hierarchy: parm#1 error')
    print('lnum=%s, line=%s' % (lnum,line))
    #exit(1)
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
 print('skipping check1_hierarchy')
 #check1_hierarchy(pagerecs)

if __name__ == "__main__":
 filein1=sys.argv[1]  # index file vol 1
 filein2=sys.argv[2]  # index file vol 2
 filein3=sys.argv[3]  # index file vol 3
 fileout = sys.argv[4]
 pagerecs1 = init_pagerecs(filein1)
 pagerecs2 = init_pagerecs(filein2)
 pagerecs3 = init_pagerecs(filein3)
 pagerecs = pagerecs1 + pagerecs2 + pagerecs3
 outrecs = make_js(pagerecs)
 write_recs(fileout,outrecs)
 check1(pagerecs)
 
 
