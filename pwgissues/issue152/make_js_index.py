# coding=utf-8
""" make_js_index.py for hitopadesha 
"""
from __future__ import print_function
import sys, re, codecs
import json

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

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
parm_numcols = 5
parm_numparm = 2 
#parm_vol = r'^(I|II|III)$'
parm_page = r'^([0-9]+)$'
#parm_tantra = r'^([0IV]+)$'  # roman, except for 0  I,II,III,IV
parm_tantra = r'^(prooemium|I|II|III|IV)$'
parm_fromv = r'^([0-9]+)([b])?$'
parm_tov = r'^([0-9]+)([a])?$'

parm_ipage = r'^([0-9]+)$'
parm_vpstr_format = '%03d'

class Pagerec(object):
 """

""" 
 def __init__(self,line,iline):
  line = line.rstrip('\r\n')
  self.line = line
  self.iline = iline
  parts = re.split(parm_regex_split,line)
  #assert len(parts) == parm_numcols
  self.status = True  # assume all is well
  self.status_message = 'All is ok'
  if len(parts) != parm_numcols:
   self.status = False
   self.message = 'Expected %s values. Found %s value' %(parm_numcols,len(parts))
   return
  # give names to the column values
  raw_page = parts[0] # 
  raw_tantra = parts[1]
  raw_fromv = parts[2]
  raw_tov = parts[3]
  raw_ipage = parts[4]
  # check page 
  m_page = re.search(parm_page,raw_page)
  if m_page == None:
   self.status = False
   self.status_message = 'Unexpected page: %s' % raw_page
   return
  # check tantra
  m_tantra = re.search(parm_tantra,raw_tantra)
  if m_tantra == None:
   self.status = False
   self.status_message = 'Unexpected tantra: %s' % raw_tantra
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
  # set self.page as integer
  self.page = int(m_page.group(1))
  # self.tantra as integer
  tan = m_tantra.group(1)
  if tan == 'prooemium':
   self.tantra = 0
  else:
   self.tantra = roman_to_int(tan)
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
  # set self.page as integer
  self.page = int(m_page.group(1))
  # set self.ipage as integer
  self.ipage = int(m_ipage.group(1))  
  # vpstr  # format consistent with format of filename of scanned page
  self.vpstr = parm_vpstr_format % (self.page)

 def todict(self):
  e = {
   'page':int(self.page),
   'tantra':self.tantra,
   'v1':int(self.fromv),
   'v2':int(self.tov),
   #'x1':self.fromvx,
   #'x2':self.tovx,
   'vp':self.vpstr,
   'ipage':int(self.ipage)
  }
  return e

def no_shlokas(lines):
 newlines = []
 for iline,line in enumerate(lines):
  if '---' in line:
   prev = lines[iline - 1]
   parts =  re.split(parm_regex_split,line)
   prevparts =  re.split(parm_regex_split,prev)
   prevtov = prevparts[3]
   parts[2] = prevtov
   parts[3] = prevtov
   newline = '\t'.join(parts)
  else:
   newline = line
  newlines.append(newline)
 return newlines

def init_pagerecs(filein):
 """ filein is a csv file, with first line as fieldnames
 """
 recs = []
 lines0 = read_lines(filein)
 # pre-adjustment for lines (pages) with no shlokas
 lines = no_shlokas(lines0)
 for iline,line in enumerate(lines):
  if (iline == 0):
   # assert line.startswith('volume') # skip column-title line
   print('Skipping column title line:',line)
   continue
  if '-' in line:
   # skip these lines at end
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
 print(len(recs),'Success: Page records read from',filein)
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

def check1_tantra(pagerecs):
 prev = None
 for irec,rec in enumerate(pagerecs):
  lnum = rec.iline + 1
  line = rec.line
  if irec == 0:
   # first record has tantra = 0 (prstAva)
   if rec.tantra != 0:
    print('check1_tantra: first tantra not 1.')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
   prev = rec
   continue
  if prev.tantra == rec.tantra:
   pass # no problem
  elif (prev.tantra + 1) == rec.tantra:
   pass
  elif (prev.tantra,rec.tantra) == (116,118):
   print('check1_tantra known anomaly')
   print('prev line:',prev.line)
   print(' cur line:',rec.line)
  else:
   # unexpected
   print('check1_tantra. tantra=%s, expected %s' %(rec.tantra,prev.tantra + 1))
   print('lnum=%s, line=%s' % (lnum,line))
   exit(1)
  # reset prev
  prev = rec
 print('pagerecs passes check1_tantra ')
 

def check1(pagerecs):
 """ check that v1 = v2_prev + 1 when 
 """
 check1_tantra(pagerecs)
 
 nerr = 0
 for irec,rec in enumerate(pagerecs):
  lnum = rec.iline + 1
  line = rec.line
  if irec == 0:
   # first verse should be 1
   if rec.fromv != 1:
    print('first verse not 1')
    print('check1_tantra: first tantra not 1.')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)    
   prev = rec
   continue
  if (rec.tantra != prev.tantra):
   if rec.fromv != 1:
    print('first verse in tantraaya not 1')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
   prev = rec
   continue
  # rec.tantra = prev.tantra
  if (rec.fromvx == '') and (prev.tovx == ''):
   #if rec.fromv != (prev.tov + 1):
   if rec.fromv not in (prev.tov + 1, prev.tov):
    print('fromv problem A')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
  else:
   #if (prev.tovx == 'a') and (rec.fromvx == 'b') and (rec.fromv == prev.tov):
   if (prev.tovx in ('a','b')) and (rec.fromvx == 'b') and (rec.fromv == prev.tov):
    # no problem
    pass
   else:
    print('fromv problem B')
    print('lnum=%s, line=%s' % (lnum,line))
    exit(1)
  prev = rec
 print("check1 finds no problems")


if __name__ == "__main__":
 filein=sys.argv[1]  # tab-delimited index file
 fileout = sys.argv[2]
 pagerecs = init_pagerecs(filein)
 outrecs = make_js(pagerecs)
 write_recs(fileout,outrecs)
 check1(pagerecs)
 
 
