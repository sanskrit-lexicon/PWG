"""example3.py
  convert slp text (conjunct consonants) to Devanagari, and
  display in two fonts (siddhanta and adhishila)
"""
from __future__ import print_function
import sys,codecs,re
#sys.path.append('../')
import unicodedata
import transcoder
transcoder.transcoder_set_dir('./')

def unused_convert(filein,fileout,tranin,tranout):
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

def init_conjuncts(filein):
 with codecs.open(filein,"r",'utf-8') as f:
  lines = [x.rstrip('\r\n') for x in f if not x.startswith(';')]
 words = []
 for line in lines:
  line = line.strip() # remove outer whitespace
  linewords = re.split(r' +',line)
  for w in linewords:
   words.append(w)
 return words

def convert_html(filein,fileout,tranin,tranout):
 words = init_conjuncts(filein)
 fpout = codecs.open(fileout,"w",'utf-8')
 n=0;
 outarr = '''<!DOCTYPE html>
<html>
<head>
<title>example3</title>
<meta charset="UTF-8">
<style>
html {font-size:16px;}
@font-face { 
 src: url(fonts/siddhanta.ttf); /* relative to this css file */
 font-family: siddhanta_deva;
}
.siddhanta {color: teal; font-family:siddhanta_deva;
 font-size:1rem;
line-height: 1.5;  /* times font-size;*/
}
@font-face { 
 src: url(fonts/Adishila.ttf); /* relative to this css file */
 font-family: adhishila_deva;
}
.adhishila {color: blue; 
 font-family:adhishila_deva;
 font-size:1.3rem;
line-height: 1.5;  /* times font-size;*/
}  
.default {color: gray;
 font-size:1rem;
line-height: 1.5;  /* times font-size;*/
}
.codepoint {font-size: 10px; font-family:Sans-Serif;};
p {font-size:1rem;
 line-height: 1.5;  /* times font-size;*/
}
</style>
</head>
<body> 

<p>  font-size of root element is 16px<br/>
  <span style="font-size:1rem;">1rem</span>
  <span style="font-size:12px;">12px</span>
  <span style="font-size:16px;">16px</span>
  <span style="font-size:24px;">24px</span>
</p>
<p> three fonts for Devanagari:<br/> 
 
 <span class='siddhanta'> siddhanta (size=1rem)</span> <br/>
 <span class='adhishila'> adhishila (size=1.3rem)</span> <br/>
 <span class='default'> default (size=1rem)</span> <br/>
</p>
<hr/>
<h2>The more common conjunct consonants</h2>
<a href="http://rb.vertimus.co.uk/assets/sanskrit/conjuncts/monier-williams_-_conjuncts.png">Source</a>
<hr/>
 '''.splitlines()
 for out in outarr:
  fpout.write(out.rstrip('\r\n')+'\n')
 
 for x0 in words:
  x = x0 + 'a'
  n=n+1
  body = x
  #body = re.sub('/\|/',' # ',body); 
  #body = preg_replace('/ +/',' ',body);
  body1 = transcoder.transcoder_processString(body,tranin,tranout)
  y = "%s ➔ <span class='siddhanta'>%s</span> | <span class='adhishila'>%s</span> | <span class='default'>%s</span>" % (body,body1,body1,body1)
  outarr = []
  outarr.append(y + '<br/>')
  # code point name (skip this
  """
  unames = [(c,unicodedata.name(c)) for c in body1]
  for c,un in unames:
   outarr.append("&nbsp;&nbsp; <span class='codepoint'> %04X  %s</span><br/>" %(ord(c),un))
  """
  for out in outarr:
   fpout.write("%s\n" % out)
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
  


