# coding=utf-8
""" lsfix2_alt_test.py
"""
def testnoncapture(analyze,fixopt):
 tests = [
     '113,b,10. 162,b,32. 170,a, No. 378. fg. b, No. 380. 179,a, No. 410. 183,a,4. 184. fgg., No. 422. fgg. 196,a, No. 454. b, No. 456. 211,a,9. 10.'


    
  
 ]
 for ibody,body in enumerate(tests):
  results,rest = analyze(body,fixopt)
  print(f'body = "{body}"')
  for iresult,result in enumerate(results):
   print(f'{iresult:04d} "{result}"')
  print(f'rest = "{rest}"')
  print()
 exit(1)
 
