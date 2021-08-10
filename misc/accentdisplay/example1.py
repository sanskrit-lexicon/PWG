"""convert2.py
  Python example of transcoding
"""
from __future__ import print_function
import sys,codecs,re
#sys.path.append('../')
import unicodedata
import transcoder
transcoder.transcoder_set_dir('./')

def convert(filein,fileout,tranin,tranout):
 fp = codecs.open(filein,"r",'utf-8')
 fpout = codecs.open(fileout,"w",'utf-8')
 n=0;
 for x in fp:
  x = x.rstrip('\r\n')
  if (x == ''):
   continue
  n=n+1
  m = re.search(r'^; x = (.*)$',x)
  if not m:
   out = "line %s is unknown: %s" %(n,x)
   exit(1)
  #head = m.group(1)
  body = m.group(1)
  #body = re.sub('/\|/',' # ',body); 
  #body = preg_replace('/ +/',' ',body);
  body1 = transcoder.transcoder_processString(body,tranin,tranout)
  y = "%s ➔ %s" % (body,tranout,body1)
  outarr = []
  outarr.append(y)
  # code point name
  unames = [(c,unicodedata.name(c)) for c in body1]
  for c,un in unames:
   outarr.append('  %04X  %s' %(ord(c),un))
  for out in outarr:
   fpout.write("%s\n" % out)
 fp.close()
 fpout.close()
 print(n,"lines converted to text\n")

def convert_html(filein,fileout,tranin,tranout):
 fp = codecs.open(filein,"r",'utf-8')
 fpout = codecs.open(fileout,"w",'utf-8')
 n=0;
 outarr = '''<!DOCTYPE html>
<html>
<head>
<title>example1</title>
<meta charset="UTF-8">
<style>
@font-face { 
 src: url(fonts/siddhanta.ttf); /* relative to this css file */
 font-family: siddhanta_deva;
}
.siddhanta {color: teal; font-family:siddhanta_deva}
@font-face { 
 src: url(fonts/Adishila.ttf); /* relative to this css file */
 font-family: adhishila_deva;
}
.adhishila {color: blue; font-family:adhishila_deva}
.default {color: gray}
.codepoint {font-size: 10px; font-family:Sans-Serif;};
</style>
</head>
<body> 
<p> three fonts for Devanagari: 
 <span class='siddhanta'> siddhanta</span>
 <span class='adhishila'> adhishila</span>
 <span class='default'> default</span>
</p>
 '''.splitlines()
 for out in outarr:
  fpout.write(out.rstrip('\r\n')+'\n')
 
 for x in fp:
  x = x.rstrip('\r\n')
  if (x == ''):
   continue
  n=n+1
  m = re.search(r'^; x = (.*)$',x)
  if not m:
   out = "line %s is unknown: %s" %(n,x)
   exit(1)
  #head = m.group(1)
  body = m.group(1)
  #body = re.sub('/\|/',' # ',body); 
  #body = preg_replace('/ +/',' ',body);
  body1 = transcoder.transcoder_processString(body,tranin,tranout)
  y = "%s ➔ <span class='siddhanta'>%s</span> | <span class='adhishila'>%s</span> | <span class='default'>%s</span>" % (body,body1,body1,body1)
  outarr = []
  outarr.append(y + '<br/>')
  # code point name
  unames = [(c,unicodedata.name(c)) for c in body1]
  for c,un in unames:
   outarr.append("&nbsp;&nbsp; <span class='codepoint'> %04X  %s</span><br/>" %(ord(c),un))
  for out in outarr:
   fpout.write("%s\n" % out)
 fp.close()
 fpout.write('</body>\n</html\n')
 fpout.close()
 print(n,"lines converted to text\n")

#-----------------------------------------------------
if __name__=="__main__":

 filein = sys.argv[1]
 fileout = sys.argv[2]
 tranin = 'slp1'
 tranout = 'deva2'
 #title = sys.argv[4]
 if fileout.endswith('.txt'):
  convert(filein,fileout,tranin,tranout)
 elif fileout.endswith('.html'):
  convert_html(filein,fileout,tranin,tranout)
 else:
  print('ERROR: output filename must end with one of ',['txt','html'])
  


