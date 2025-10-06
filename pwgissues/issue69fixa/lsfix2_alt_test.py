# coding=utf-8
""" lsfix2_alt_test.py
"""
def testnoncapture(analyze,fixopt):
 tests = [
'31,a,4. 6. 87,a,4. 6. 87,b. 32. 97,b,38.'

    
  
 ]
 for ibody,body in enumerate(tests):
  results,rest = analyze(body,fixopt)
  print(f'body = "{body}"')
  for iresult,result in enumerate(results):
   print(f'{iresult:04d} "{result}"')
  print(f'rest = "{rest}"')
  print()
 exit(1)
 
