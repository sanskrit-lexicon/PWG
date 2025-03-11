# coding=utf-8
""" ref_adhy.py
"""
from __future__ import print_function
import sys, re,codecs
sys.path.append('../') # location of digentry
import digentry

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

def get_all_regexes(X):
 regexraws = [
  r'<ls>%s.*?</ls>' % X,
  r'<ls n="%s.*?</ls>' % X
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def arec_to_outrec(arec):
 outarr = []
 adhy = arec.adhy
 maxv = arec.maxv
 datas = arec.data_prob
 nprob = len(datas)
 out = '* (%s) adhy=%s, verse > %s' %(nprob,adhy,maxv)
 outarr.append(out)
 datas1 = sorted(datas,key = lambda t: t[2]) # verse in ls
 for idata,data in enumerate(datas):
  entry,adhy1,v1,ls = data
  meta = entry.metaline
  outarr.append('%d,%d %s %s' %(adhy1,v1,ls,meta))
 return outarr

def write_problems(fileout,arecs):
 outrecs = []
 for arec in arecs:
  outrec = arec_to_outrec(arec)
  outrecs.append(outrec)
 #
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(arecs),"written to",fileout)

class AdhyRange(object):
 def __init__(self,line):
  parts = re.split(r' +',line)
  assert len(parts) == 2
  self.adhy = int(parts[0])
  self.maxv = int(parts[1])
  self.data_ok = []   # tuples of entry,adhy,verse
  self.data_prob = [] # tuples of entry,adhy,verse

def init_AdhyRange(filein):
 lines = read_lines(filein)
 recs = [AdhyRange(line) for line in lines]
 d = {}
 for rec in recs:
  d[rec.adhy] = rec
 return recs,d

def adhy_entries(entries,da):
 regex_raw = r'<ls>VARĀH. BṚH. S. ([0-9]+),([0-9]+)'
 print("regex_raw =",regex_raw)

 regex = re.compile(regex_raw)
 n = 0
 for entry in entries:
  text = ' '.join(entry.datalines)
  for m in re.finditer(regex,text):
   n = n + 1
   adhy  = int(m.group(1))
   verse = int(m.group(2))
   data = (entry,adhy,verse,m.group(0))
   if adhy not in da:
    print('error: ref bad adhya',m.group(0))
    continue
   rec = da[adhy] 
   maxv = rec.maxv
   if verse <= maxv:
    rec.data_ok.append(data)
   else:
    rec.data_prob.append(data)
 print('found %s entries matching %s' % (n,regex_raw))


if __name__=="__main__":
 filein = sys.argv[1]  # xxx.txt
 filein1 = sys.argv[2] # adhy_range.txt
 fileout = sys.argv[3] # output file
 
 arecs,drec = init_AdhyRange(filein1)
 entries = digentry.init(filein)
 # set entries attribute of AdhyRange objects
 adhy_entries(entries,drec) # modifies arec objects
 
 write_problems(fileout,arecs)
 
 
