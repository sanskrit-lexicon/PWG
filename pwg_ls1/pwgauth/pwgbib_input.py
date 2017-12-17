# coding=utf-8
"""pwgbib_input.py
   12-14-2017
"""
from bibrec import Bibrec,init_bibrecs

import re,codecs,sys

def format_text(txt):
 txt = re.sub(r'<lb>',' ',txt)
 # maybe more later
 return txt

def format_code(code):
 """  Normally, compute capitalization of code. e.g.
   MBH. -> Mbh. 
   PHP does not do this reliably for extended ascii.
   Also, there are special cases (Like H. an. -> H. an.) which we
   can handle more easily here than in PHP
 """
 if code == 'an.':
  ans = code
 elif code == 'H. an.':
  ans = code
 else:
  ans = unicode.title(code)
 return ans

if __name__ == "__main__":
 filebib = sys.argv[1]
 fileout = sys.argv[2]
 
 bibrecs = init_bibrecs(filebib)
 print len(bibrecs),"records from",filebib
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in bibrecs:
   text = format_text(rec.text)
   codelo = format_code(rec.code)
   out = '%s\t%s\t%s\t%s' %(rec.lineid,rec.code,codelo,text)
   f.write(out+'\n')
 print len(bibrecs),"records written to",fileout
