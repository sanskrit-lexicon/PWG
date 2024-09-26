# coding=utf-8
"""
 mark_deva.py
 Code assistance from Copilot
"""
import re, sys, codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"lines read from",filein)
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def mark_devanagari(text):
    # Regular expression pattern to match Devanagari characters
    devanagari_pattern = re.compile(r'[\u0900-\u097F]+')
    
    # Replace Devanagari text with marked text
    marked_text = devanagari_pattern.sub(lambda x: f'<s>{x.group()}</s>', text)
    
    return marked_text

def marklines(lines):
 newlines = []
 for line in lines:
  newline = mark_devanagari(line)
  newlines.append(newline)
 return newlines

if __name__=="__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 # Read the input file into array of lines
 lines = read_lines(filein)
 
 # Mark the Devanagari text in each line
 newlines = marklines(lines)

 # Write the output to a new file
 write_lines(fileout,newlines)

 print("Devanagari text has been marked and saved to",fileout)
