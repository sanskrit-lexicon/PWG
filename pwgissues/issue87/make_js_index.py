# coding=utf-8
""" make_js_index.py for bhagp_bom 
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
parm_regex_split = r'[ ]+'
parm_numcols = 5
parm_numparm = 1  
parm_vol = r'^(I|II|III)$'
parm_page = r'^([0-9]+)$'
parm_fromv = r'^([0-9]+)([b])?$'
parm_tov = r'^([0-9]+)([a])?$'
parm_ipage = r'^([0-9]+)$'

# scanned image file name prefix 2 parameters
# first parameter = volume (as int -- 1,2,3)
# second parameter = page  (as 3-digit 0-filled integer 001, etc.
parm_vpstr_format = '%d%03d'
# number of paramenters in a verse reference
class Pagerec(object):
 """
Format of Indische spruche index v1
volume 	page 	from v. to v. 	ipage
I       12      1       5       1
Note the first line (column names) is ignored
ipage is an 'internal page number'  Not used by this app
""" 
 def __init__(self,line,iline,filevol):
  line = line.rstrip('\r\n')
  self.line = line
  self.iline = iline
  parts = re.split(parm_regex_split,line)
  assert len(parts) == parm_numcols
  self.status = True  # assume a is well
  self.status_reason = 'All is ok'
  if len(parts) != parm_numcols:
   self.status = False
   self.message = 'Expected %s values. Found %s value' %(parm_numcols,len(parts))
   return
  # give names to the column values
  raw_vol = parts[0]  
  raw_page = parts[1] # internal to volume. digits
  raw_fromv = parts[2]
  raw_tov = parts[3]
  raw_ipage = parts[4]
  # check vol
  m_vol = re.search(parm_vol,raw_vol)
  if m_vol == None:
   self.status = False
   self.status_message = 'Unexpected vol: %s' % raw_vol
   return
  # check page 
  m_page = re.search(parm_page,raw_page)
  if m_page == None:
   self.status = False
   self.status_message = 'Unexpected page: %s' % raw_page
   return
  # check fromv 
  m_fromv = re.search(parm_fromv,raw_fromv)
  if m_fromv == None:
   self.status = False
   self.status_message = 'Unexpected fromv: %s' % raw_fromv
   return
  # check tov 
  m_tov = re.search(parm_tov,raw_tov)
  if m_tov == None:
   self.status = False
   self.status_message = 'Unexpected tov: %s' % raw_tov
   return
  # check ipage 
  m_ipage = re.search(parm_ipage,raw_ipage)
  if m_ipage == None:
   self.status = False
   self.status_message = 'Unexpected ipage: %s' % raw_ipage
   return
  # set self.vol as integer
  self.vol0 = m_vol.group(1)
  self.vol = roman_to_int(m_vol.group(1))
  if self.vol == None:
   self.status = False
   self.status_message = 'Unexpected vol: %s' % raw_vol
   return
  # set self.page as integer
  self.page = int(m_page.group(1))
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
  # set self.ipage 
  self.ipage = raw_ipage
  # vpstr  # format consistent with format of filename of scanned page
  self.vpstr = parm_vpstr_format % (self.vol,self.page)

 def todict(self):
  if self.fromvx == None:
   self.fromx = ''
  e = {
   'v':self.vol0, 'page':int(self.page), 
   'v1':int(self.fromv), 'v2':int(self.tov),
   'x1':self.fromvx, 'x2':self.tovx, 'vp':self.vpstr
  }
  return e

def init_pagerecs(filein,filevol):
 """ filein is a csv file, with first line as fieldnames
 """
 recs = []
 with codecs.open(filein,"r","utf-8") as f:
  for iline,line in enumerate(f):
   if (iline == 0):
    # assert line.startswith('volume') # skip column-title line
    print('Skipping column title line:',line)
    continue
   pagerec = Pagerec(line,iline,filevol)
   if pagerec.status:
    # No problems noted
    recs.append(pagerec)
   else:
    lnum = iline + 1
    print('Problem at line # %s:' % lnum)
    print('line=',line)
    print('message=',pagerec.status_message)
    exit(1)
 print(len(recs),'Success: Page records read from',filein)
 return recs


def make_js_1(recs):
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

def check1(pagerecs):
 """ check that v1 = v2_prev + 1
 """
 nerr = 0
 for irec,rec in enumerate(pagerecs):
  if irec == 0:
   prev = rec
   continue
  if (rec.fromvx == '') and (prev.tovx == ''):
   if rec.fromv != (prev.tov + 1):
    print('check1 error A. line %s =%s' % (rec.iline + 1,rec.line))
    nerr = nerr + 1
  else:
   if (prev.tovx == 'a') and (rec.fromvx == 'b') and (rec.fromv == prev.tov):
    # no problem
    pass
   else:
    print('check1 error B.\nline %s =%s' % (rec.iline + 1,rec.line))
    nerr = nerr + 1
    if True: # dbg
     print('prevline=',prev.line)
     print(' rec.tov =  ',rec.tov)
     print('prev.tovx=  ',prev.tovx)
     print(' rec.fromv= ',rec.fromv)
     exit(1)
  prev = rec
 print("check1 finds %s errors" % nerr)
 return nerr

if __name__ == "__main__":
 filevol = sys.argv[1] # I, II, or III
 filein=sys.argv[2]  # tab-delimited index file
 fileout = sys.argv[3]
 pagerecs = init_pagerecs(filein,filevol)
 if parm_numparm == 1:
  outrecs = make_js_1(pagerecs)
 elif parm_numparm == 2:
  outrecs = make_js_2(pagerecs)
 elif parm_numparm == 3:
  outrecs = make_js_3(pagerecs)
 elif parm_numparm == 4:
  outrecs = make_js_4(pagerecs)
 else:
  print('PROBLEM with parm_numparm = %s' % parm_numparm)
  exit(1)
 write_recs(fileout,outrecs)
 check1(pagerecs)
 
 
