"""transwork.py
   Reads a transcoder file
   and converts all '\uxxxx' strings to the correspond unicode.
   Reads and writes utf-8 files
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
 for line in f:
  n = n + 1
  lineout = re.sub(r'\\u....',my_replace,line)  
  fout.write(lineout)
 f.close()
 fout.close()
