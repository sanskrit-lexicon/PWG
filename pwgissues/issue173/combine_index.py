# coding=utf-8
""" combine_index.py
   Merge rvps1.txt (vol 1) and rvps2.txt (vol 2) into a single index.txt
   Output columns: page	patala	fromv	tov	ipage	Remarks	volume
"""
from __future__ import print_function
import sys, re

def read_index(filein, vol):
    recs = []
    with open(filein, 'r', encoding='utf-8') as f:
        for iline, line in enumerate(f):
            line = line.rstrip('\r\n')
            if iline == 0:
                continue  # skip header
            parts = line.split('\t')
            if len(parts) < 5:
                continue
            page = parts[0].strip()
            patala = parts[1].strip()
            fromv = parts[2].strip()
            tov = parts[3].strip()
            ipage = parts[4].strip()
            remarks = parts[5].strip() if len(parts) > 5 else ''
            recs.append((page, patala, fromv, tov, ipage, remarks, str(vol)))
    return recs

def write_index(fileout, recs):
    with open(fileout, 'w', encoding='utf-8') as f:
        f.write('page\tpatala\tfrom v.\tto v.\tipage\tRemarks\tvolume\n')
        for rec in recs:
            line = '\t'.join(rec)
            f.write(line + '\n')
    print(len(recs), 'records written to', fileout)

if __name__ == '__main__':
    fileout = 'index.txt'
    recs1 = read_index('rvps1.txt', 1)
    recs2 = read_index('rvps2.txt', 2)
    recs = recs1 + recs2
    write_index(fileout, recs)
