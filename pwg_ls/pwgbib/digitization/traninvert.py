"""traninvert.py
   Reads a transcoder file and 'inverts' the codings, e.g.,
   changes '<in>X<in> <out>Y</out>' to '<in>Y<in> <out>X</out>'
"""
import codecs,sys,re

def my_replace(m):
 """  assume x is string of form '\uxxxx', where x is a hex number
 """
 x = m.group(0)
 y = x[2:] # drop the '\u'
 try:
  z = int(y,16) #convert to base 16 integer,  z is a code point
 except:
  print "ERROR. y=",y,"x=",x
  exit(1)
 u = unichr(z)  # the corresponding unicode character
 return u
 
if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 f = codecs.open(filein,"r","utf-8")
 fout = codecs.open(fileout,"w","utf-8")
 n = 0
 nchg=0
 for line in f:
  n = n + 1
  lineout = re.sub(r'<in>(.*?)</in> +<out>(.*?)</out>',r'<in>\2</in> <out>\1</out>',line)  
  if line != lineout:
   nchg = nchg+1
  fout.write(lineout)
 f.close()
 fout.close()
 print nchg,"lines changed out of ",n,"lines read"
