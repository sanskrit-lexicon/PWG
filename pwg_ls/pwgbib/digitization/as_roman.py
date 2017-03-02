""" as_roman.py
    Usage: python as_roman.py pwgbib1_utf8.txt pwgbib1_roman.txt
"""
import codecs,sys,re
import transcoder
transcoder.transcoder_set_dir('.')

def unused_convertrecs(recs,tranin,tranout):
 "Modifies recs"
 n=0
 for rec in recs:
  n=n+1
  try:
   rec.abbrvunicode = transcoder.transcoder_processString(rec.abbrv,tranin,tranout)
   rec.titleunicode = transcoder.transcoder_processString(rec.title,tranin,tranout)
   m = re.search(r'[a-zA-Z][1-9]',rec.abbrvunicode + " " + rec.titleunicode )
   if m:
    print "TRANSCODER WARNING: ",m.group(0).encode('utf-8')
  except:
   print "convertrecs problem",n,rec.line.encode('utf-8')
   #exit(1)

def unused_writerecs(recs,fileout):
 fout = codecs.open(fileout,"w","utf-8")
 n=0
 for rec in recs:
  n = n + 1
  outarr=[]  # array of fields to write.
  outarr.append(rec.abbrv)
  outarr.append('%03d' % n) # sequence number in pwbib0
  if rec.checked:
   outarr.append('+') # code for marked as 'checked' in pwbib0
  else:
   outarr.append('-') # code for marked as 'unchecked' in pwbib0
  outarr.append(rec.type) # == (standard) or xx (non-standard)
  outarr.append(rec.volume) # text volume (1-6)
  outarr.append(rec.abbrvunicode) # unicode form of abbreviation
  outarr.append(rec.titleunicode) # unicode form of title
  # join fields with '\t'
  out = '\t'.join(outarr)
  fout.write('%s\n' % out)
 fout.close()

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 tranin = 'as'
 tranout = 'roman'
 f = codecs.open(filein,"r","utf-8")
 fout = codecs.open(fileout,"w","utf-8")
 n = 0
 for line in f:
  n = n + 1
  lineout = transcoder.transcoder_processString(line,tranin,tranout)
  fout.write(lineout)
 f.close()
 fout.close()
 print n,"lines from",filein,"converted from AS to ROMAN transliteration"
 print "lines written to",fileout


