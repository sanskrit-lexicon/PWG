# coding=utf-8
""" lsother.py  
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"lines read from",filein)
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"cases written to",fileout)

LSCODE = 'Spr.'
X1 = '<ls>%s ' % LSCODE
X2 = '<ls n="%s">' % LSCODE
LSCLOSE = '</ls>'
REGEX0 = r'^(%s|%s)(.*?)%s$' %(X1,X2,LSCLOSE)
REGEX1 = r'^[0-9]+\.$'
REGEX2 = r'^([0-9]+\.)|([0-9]+\.fg\.)|([0-9]+\.fgg\.)|([0-9]+,v\.l\.)$'
def solve_1(line):
 dbg = (line == '<ls>Spr. 1,467. 468.</ls>')
 dbg = False
 defaultans = None
 m = re.search(REGEX0,line)
 if m == None:
  return defaultans
 X = m.group(1)
 body = m.group(2)
 if dbg:
  print('line=',line)
  print('X=',X)
  print('body=',body)
 # option 1
 parts = body.split(' ')
 # require all parts to be 'N' digit sequence followed by period
 flag = True
 for part in parts:
  if not re.search(REGEX1,part):
   flag = False
 if not flag:
  return defaultans
 arr = []
 for ipart,part in enumerate(parts):
  if ipart == 0:
   a = '%s%s%s' %(X,part,LSCLOSE)
  else:
   a = '%s%s%s' %(X2,part,LSCLOSE)
  arr.append(a)
 ans = ' '.join(arr)
 return ans

def solve_2_version1(line):
 dbg = (line == '<ls>Spr. 1973. fg. 2647.</ls>')
 defaultans = None
 m = re.search(REGEX0,line)
 if m == None:
  return defaultans
 X = m.group(1)
 body = m.group(2)
 if dbg:
  print('line=',line)
  print('X=',X)
  print('body=',body)
 # option 2
 parts = body.split(' ')
 # require all parts to be
 # 'N' digit sequence followed by period
 # OR 'fg.' or 'fgg.'
 flag = True
 parttypes = []
 for part in parts:
  if re.search(REGEX1,part):
   parttypes.append('N')
   continue
  if part in ['fg.','fgg.']:
   parttypes.append('FG')
   continue
  flag = False
  break
 if not flag:
  return defaultans
 arr = []
 for ipart,part in enumerate(parts):
  if ipart == 0:
   a = '%s%s%s' %(X,part,LSCLOSE)
   arr.append(a)
   assert parttypes[ipart] == 'N'
  elif parttypes[ipart] == 'N':
   a = '%s%s%s' %(X2,part,LSCLOSE)
   arr.append(a)
  elif parttypes[ipart] == 'FG':
   # add part to previous arr elt
   aprev = arr.pop()
   a = aprev.replace('</ls>',
                     ' ' + part + '</ls>')
   arr.append(a)
  else:
   print('solve_2_version1 internal error')
   print(line)
   exit(1)
 ans = ' '.join(arr)
 if dbg:
  print('ans=',ans)
 return ans

def solve_2(line):
 dbg = (line == '<ls>Spr. 1973. fg. 2647.</ls>')
 defaultans = None
 # preadjust line
 replacements = [
  ('. fg.', '.fg.'),
  ('. fgg.', '.fgg.'),
  (', v. l.' , ',v.l.'),
  ]
 line1 = line
 for old,new in replacements:
  line1 = line1.replace(old,new)
 m = re.search(REGEX0,line1)
 if m == None:
  return defaultans
 X = m.group(1)
 body = m.group(2)
 if dbg:
  print('line=',line)
  print('line1=',line1)
  print('X=',X)
  print('body=',body)
 # option 2
 parts = body.split(' ')
 # require all parts to match REGEX2
 flag = True
 for part in parts:
  if re.search(REGEX2,part):
   continue
  flag = False
  break
 if not flag:
  return defaultans
 # construct ls elements for each part
 arr = []
 for ipart,part in enumerate(parts):
  if ipart == 0:
   a = '%s%s%s' %(X,part,LSCLOSE)
  else:
   a = '%s%s%s' %(X2,part,LSCLOSE)
  arr.append(a)
 ans = ' '.join(arr)
 ans1 = ans
 # restore the initial replacements (if any)
 for old,new in replacements:
  ans1 = ans1.replace(new,old)
 if dbg:
  print('ans=',ans)
  print('ans1=',ans1)
 return ans1

def solve_3(line):
 # temporary add period at end
 # 3</ls> -> 3.</ls>
 m = re.search(r'([0-9])</ls>',line)
 defaultans = None
 #line1 = re.sub(r'([0-9])</ls>$',r'\1.</ls>',line)
 if m == None:
  return defaultans
 a = m.group(1) # the last digit at end
 old = '%s</ls>' % a
 new = '%s.</ls>' % a
 line1 = line.replace(old,new)
 # Apply solve_2 to line1
 newline1 = solve_2(line1)
 if newline1 == defaultans:
  return defaultans
 # remove the period before ending </ls>
 ans = re.sub(r'[.]</ls>$', '</ls>',newline1)
 return ans

def solve_4(line):
 # <ls>Spr. 3321).</ls> ->  <ls>Spr. 3321</ls>).
 defaultans = None
 dbg = (line == '<ls>Spr. 4909).</ls>')
 line1 = line.replace(').</ls>',  '.</ls>')
 if line1 == line:
  return defaultans
 m = re.search(r'<ls>Spr\. [0-9]+\.</ls>',line1)
 if m != None:
  # 1 parameter. - no solving required
  line2 = line1
 else:
  line2 = solve_2(line1)
 if dbg:
  print('solve_4: line =',line)
  print('line1=',line1)
  print('line2=',line2)
 if line2 == defaultans:
  return defaultans
 # Restore the end
 ans = line2.replace('.</ls>', '</ls>).')
 return ans

def solve_5(line):
 defaultans = None
 m = re.search(r'^<ls n="Spr\."> ([0-9]+) \(II\)\.(.*)</ls>$',line)
 if m == None:
  return defaultans
 v1 = m.group(1) # this verse in 2nd edition of Spruche
 newline1 = '<ls>Spr. (II) %s.</ls>' % v1
 rest = m.group(2)  # the rest of the line
 if rest == '':
  return newline1
 # use method 2 to parse rest
 # rest should start with a space, and end with </ls>
 line2 = '<ls>Spr.%s</ls>' % rest
 # try solve_3 on line2
 newline2 = solve_2(line2)
 if newline2 == defaultans:
  return defaultans
 # restore the ending ')'
 # join newline1 and 2
 ans = '%s %s' %(newline1,newline2)
 return ans

def solve_6(line):
 defaultans = None
 dbg = (line == '<ls n="Spr.">115 (II). 3611. 4746.</ls>')
 if dbg: print(line)
 m = re.search(r'^<ls n="Spr.">([0-9]+) \(II\)\.(.*)</ls>$',line)
 if m == None:
  return defaultans
 v1 = m.group(1) # this verse in 2nd edition of Spruche
 newline1 = '<ls>Spr. (II) %s.</ls>' % v1
 rest = m.group(2)  # the rest of the line
 if dbg:
  print('newline1 =',newline1)
  print('rest =',rest)
 if rest == '':
  return newline1
 # use method 2 to parse rest
 # rest should start with a space, and end with </ls>
 line2 = '<ls>Spr.%s</ls>' % rest
 # try solve_3 on line2
 newline2 = solve_2(line2)
 if newline2 == defaultans:
  return defaultans
 # restore the ending ')'
 # join newline1 and 2
 ans = '%s %s' %(newline1,newline2)
 return ans

def solve_7(line):
 defaultans = None
 dbg = (line == '<ls>Spr. 4719. (II) 1667.</ls>')
 if dbg: print(line)
 parts = line.split(' (II) ')
 if len(parts) != 2:
  return defaultans
 part1,part2 = parts
 line1 = '%s</ls>' % part1
 newline1 = solve_2(line1)
 if dbg:
  print('line1=',line1)
  print('newline1=',newline1)
 if newline1 == defaultans:
  return defaultans
 line2 = '<ls>Spr. %s' % part2
 newline2 = solve_2(line2)
 if dbg:
  print('line2=',line2)
  print('newline2=',newline2)
 if newline2 == defaultans:
  return defaultans
 # newline2 refers to Spr. (II)
 newline2a = newline2.replace('Spr.', 'Spr. (II)')
 if dbg:print('newline2a=',newline2a)
 ans = '%s %s' %(newline1,newline2a)
 return ans

def solve_8(line):
 defaultans = None
 from lsother_7a_edit import d
 if line not in d:
  return defaultans
 else:
  newline = d[line]
  return newline
 
def solve_line(line,option):
 if option == '1':
  return solve_1(line)
 elif option == '2':
  return solve_2(line)
 elif option == '3':
  return solve_3(line)
 elif option == '4':
  return solve_4(line)
 elif option == '5':
  return solve_5(line)
 elif option == '6':
  return solve_6(line)
 elif option == '7':
  return solve_7(line)
 elif option == '8':
  return solve_8(line)
 else:
  print('solve_line: unknown option',option)
  exit(1)
  
if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2]  # X_othr
 fileout = sys.argv[3] # output file -- each line solved
 fileout1 = sys.argv[4] # unsolved lines
 lines = read_lines(filein)
 solved = []
 unsolved = []
 for line in lines:
  solution = solve_line(line,option)
  if solution == None:
   unsolved.append(line)
  else:
   solved.append('%s\t%s' %(line,solution))
   
 write_lines(fileout,solved)
 write_lines(fileout1,unsolved)
