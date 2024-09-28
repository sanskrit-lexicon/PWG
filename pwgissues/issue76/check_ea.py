# coding=utf-8
""" as_inventory.py
"""
import sys,re,codecs
#import transcoder
#transcoder.transcoder_set_dir("");
import unicodedata


def make_combining_chars():
 chars = [
  r'\u0300', # combining grave accent
  r'\u0301', # combining acute accent
  r'\u0302', # combining circumflex accent
  r'\u0303', # combining tilde
  r'\u0304', # combining macron
  r'\u0306', # combining breve
 ]
 ans = []
 for x in chars:
  # ref: http://stackoverflow.com/questions/2828284/conversion-of-strings-like-uxxxx-in-python
  # Python3 error: AttributeError: 'str' object has no attribute 'decode'
  #y = x.decode('unicode-escape')  
  y = x
  ans.append(y)
 if False:
  for key in ans:
   ords = [r"\u%04x" % ord(c) for c in key]
   ordstr = '.'.join(ords)
   names = [unicodedata.name(c) for c in key]
   namestr = ' + '.join(names)
   out = "%s  (%s)  := %s" %(key,ordstr,namestr)
   print(out.encode('utf-8'))
  exit(0)
 return ans

combining_chars = make_combining_chars() # a list 

def update_asdict(line,asdict):
 if line == '':
  return
 parts = []
 prev = None
 for ic,c in enumerate(line):
  if ic == 0:
   prev = c
  elif c in combining_chars:
   prev = prev + c
  else:
   # not a combining character and not the first character
   parts.append(prev)
   prev = c
 parts.append(prev)
 #print 'line=',line.encode('utf-8')
 for ic,c in enumerate(parts):
  #print ic,c
  if (len(c) == 1) and (ord(c) <= 127):
   # skip ascii character character
   continue
  if c not in asdict:
   asdict[c] = 0
  asdict[c] = asdict[c] + 1
 #exit(0)

def check_ea(inlines):
# set up regex callback 'repl' with access to dictionary asdict
 asdict = {}
 # read the lines of the file
 n = 0
 extras0 = [r'\u0064\u0301',r'\u0074\u0301'] # t,d with combining acute
 #extras = [x.decode('unicode-escape') for x in extras0]
 extras = extras0
 flag = False
 for iline,line in enumerate(inlines):
  if line.startswith('[Page'):
   continue
  line = line.rstrip()
  for extra in extras:
   if extra in line:
    print("CHECK extra:",iline,line)
  n = n + 1
  update_asdict(line,asdict)
 return asdict

def write_ea(d,fileout):
 keys = d.keys()
 print(len(keys),"extended ascii codes found")
 #print("n=",n)
 keys = sorted(keys)
 print(len(keys))
 outlines = []
 for key in keys:
  asobj = d[key]
  #key1=convert(key)
  # key is a string
  try:
   
   #ords = ["\u%04x" % ord(c) for c in key]
   ords = ["%04x" % ord(c) for c in key]
  except:
   print('write_ea error with key',key)
   exit(1)
  ordstr = ''.join(ords)
  names = [unicodedata.name(c) for c in key]
  namestr = ' + '.join(names)
  #out = "%s  (\\u%04x) %5d := %s" %(key,ord(key),asobj,namestr)
  out = "%s  (%s) %5d := %s" %(key,ordstr,asobj,namestr)
  outlines.append(out)
 with codecs.open(fileout,"w","utf-8") as fout:
  for line in outlines:
   fout.write(line+'\n')
 print(len(outlines),"lines written to",fileout)
if __name__=="__main__":
 filein = sys.argv[1]  # xxxwithmeta1.txt
 fileout = sys.argv[2] # xxxwithmeta2.txt
 with codecs.open(filein,"r","utf-8") as f:
  inlines = [x.rstrip('\r\n') for x in f]
  print(len(inlines),"lines read from",filein)
 d = check_ea(inlines)
 write_ea(d,fileout)
 exit(1)
 outlines = inlines
 as_iast(outlines) # modifies outlines
 with codecs.open(fileout,"w","utf-8") as fout:
  for line in outlines:
   fout.write(line+'\n')
 print(len(outlines),"lines written to",fileout)
