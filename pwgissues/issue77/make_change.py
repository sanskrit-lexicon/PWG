# coding=utf-8
""" make_change_regular.py adapted for pwg
"""
from __future__ import print_function
import sys, re,codecs
import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

#word_regex_raw = '[A-Za-z0-9äöüÄÖÜ]+'
#word_regex = re.compile(word_regex_raw)

def exclude_words(words):
 ans = []
 for word in words:
  if len(word) == 1:
   continue
  if re.search(r'^[0-9]+$',word):
   continue
  ans.append(word)
 return ans

def get_words_line(line0,iline=None):
 # return array of words
 # various filters
 line = line0
 # line = re.sub(r'{%.*?%}', ' ',line)
 line = re.sub(r'{#.*?#}', ' ',line)
 line = re.sub(r'<([^ ]*?)(.*?)>.*?</\1>',' ',line)
 line = re.sub(r'¦',' ',line)
 line = re.sub(r'<div.*?>',' ',line)
 line = line.strip()
 words0 = re.findall(word_regex,line)
 words = exclude_words(words0)
 dbg = False
 if dbg:
  print('line0: ',line0)
  print('line : "%s"' % line)
  print('words:',', '.join(words))
  print()
 return words

def get_words(entries):
 # create entry.dataline_words array
 dbg = False
 for ientry,e in enumerate(entries):
  e.dataline_words = []
  for iline,line in enumerate(e.datalines):
   words_line = get_words_line(line)
   e.dataline_words.append(words_line)

 print("exit get_words")
 
def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_recs(fileout,recs):
 # recs is array of Change objects
 outrecs = []
 for irec,rec in enumerate(recs):
  if rec.lnum == None:
   print('write_recs problem:',rec.linein)
  outarr = []
  outarr.append('; %s' %rec.metaline)
  outarr.append('%s old %s' % (rec.lnum,rec.line))
  outarr.append(';')
  outarr.append('%s new %s' % (rec.lnum,rec.newline))
  outrecs.append(outarr)
 write_outrecs(fileout,outrecs)

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_outarr(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

class Change:
 def __init__(self,metaline,lnum,line,newline):
  self.metaline = metaline
  self.lnum = lnum
  self.line = line
  self.newline = newline

def get_newline(line):
 lsall = re.findall(r'<ls.*?</ls>',line)
 newline = line
 for ls in lsall:
  newline = re.sub(r', +([0-9])', r',\1',newline)
 # also, remove space(s) at end of lines
 newline = re.sub(r' +$', '', newline)
 return newline

def get_changes(entries):
 changes = []
 for ientry,e in enumerate(entries):
  for iline,line in enumerate(e.datalines):
   newline = get_newline(line)
   if newline == line:
    continue
   metaline = e.metaline
   lnum = e.linenum1 + iline + 1
   change = Change(metaline,lnum,line,newline)
   changes.append(change)
 return changes

if __name__=="__main__":
 filein = sys.argv[1] # xxx.txt cdsl
 fileout = sys.argv[2] # change transactions
 entries = digentry.init(filein)
 changes = get_changes(entries)
 write_recs(fileout,changes)

