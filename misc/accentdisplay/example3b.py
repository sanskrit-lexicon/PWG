"""example3b.py
  convert slp text (conjunct consonants) to Devanagari, and
  display in two fonts (siddhanta and adhishila)
"""
from __future__ import print_function
import sys,codecs,re
#sys.path.append('../')
import unicodedata
import transcoder
transcoder.transcoder_set_dir('./')

class Conjunct(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.txt = line
  if line.startswith('<'):
   self.type = 'html'
  else:
   self.type = 'text'
  
def init_conjuncts(filein):
 with codecs.open(filein,"r",'utf-8') as f:
  recs = [Conjunct(x) for x in f if not x.startswith(';')]
 return recs

def convert_html(filein,fileout,tranin,tranout):
 recs = init_conjuncts(filein)
 fpout = codecs.open(fileout,"w",'utf-8')
 n=0;
 outarr = '''<!DOCTYPE html>
<html>
<head>
<title>example3b</title>
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
@font-face { 
 src: url(fonts/sanskr.ttf); /* relative to this css file */
 font-family: sanskr_deva;
}
.sanskr {color: gray;
 font-family:sanskr_deva;
 font-size:1.2rem;
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
 <span class='sanskr'> sanskr (size=1.2rem)</span> <br/>
</p>
<hr/>
<h2>Conjunct consonants and accents</h2>

<hr/>
 '''.splitlines()
 for out in outarr:
  fpout.write(out.rstrip('\r\n')+'\n')
 
 for rec in recs:
  x = rec.txt
  outarr = []
  if rec.type == 'html':
   outarr.append(x)
  else:
   n=n+1
   body = x
   a = []
   tcs = [('deva1','siddhanta'),('deva2','adhishila'),('deva1','sanskr')]
   au = []
   for tranout,c in tcs:
    body1 = transcoder.transcoder_processString(body,tranin,tranout)
    au.append(body1)
    a.append("<span class='%s'>%s</span>" %(c,body1))
   #y = "%s ➔ <span class='siddhanta'>%s</span> | <span class='adhishila'>%s</span> | <span class='sanskr'>%s</span> (%s)" % (body,body1,body1,body1,nx)
   astr = ' | '.join(a)
   y = "%s ➔ %s" %(x,astr)
   outarr.append(y + '<br/>')
   if True and (au[0]!=au[1]):
    body1 = au[0] # siddhanta
    outarr.append('<details class="codepoint" style="margin-left:40px">')
    outarr.append('<summary>altered unicode sequence for siddhanta, sanskr</summary>')
    
    unames = [(c,unicodedata.name(c)) for c in body1]
    for c,un in unames:
     outarr.append("&nbsp;&nbsp; <span class='codepoint'> %04X  %s</span><br/>" %(ord(c),un))
    outarr.append('</details>')
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
 tranout = None  #  'deva2'  will vary with font
 #title = sys.argv[4]
 if fileout.endswith('.txt'):
  convert(filein,fileout,tranin,tranout)
 elif fileout.endswith('.html'):
  convert_html(filein,fileout,tranin,tranout)
 else:
  print('ERROR: output filename must end with one of ',['txt','html'])
  


