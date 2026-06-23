# coding=utf-8
""" make_js_index.py for rvps (Ṛgveda Prātiśākhya)
   Adapted from issue169 version: adds volume, patala instead of taranga,
   handles '-' and blank values in fromv/tov.
"""
from __future__ import print_function
import sys, re
import json

parm_regex_split = '\t'
parm_numcols = 7
parm_page = r'^([0-9]+)$'
parm_patala = r'^([0-9]+)$'
parm_fromv = r'^([0-9]+)?$'
parm_tov = r'^([0-9]+)?$'
parm_ipage = r'^([0-9]+)$'
parm_volume = r'^([0-9]+)$'

class Pagerec(object):
    def __init__(self, line, iline):
        line = line.rstrip('\r\n')
        self.line = line
        self.iline = iline
        parts = re.split(parm_regex_split, line)
        self.status = True
        self.status_message = 'All is ok'
        if len(parts) != parm_numcols:
            self.status = False
            self.status_message = 'Expected %s values. Found %s' % (parm_numcols, len(parts))
            return
        raw_page = parts[0]
        raw_patala = parts[1]
        raw_fromv = parts[2]
        raw_tov = parts[3]
        raw_ipage = parts[4]
        raw_remarks = parts[5]
        raw_volume = parts[6]

        m_page = re.search(parm_page, raw_page)
        if m_page is None:
            self.status = False
            self.status_message = 'Unexpected page: %s' % raw_page
            return
        self.page = int(m_page.group(1))

        self.patala = None
        m_patala = re.search(parm_patala, raw_patala)
        if m_patala is not None and raw_patala != '-':
            self.patala = int(m_patala.group(1))

        self.fromv = None
        self.tov = None
        if raw_fromv not in ('', '-') and raw_tov not in ('', '-'):
            m_fromv = re.search(parm_fromv, raw_fromv)
            m_tov = re.search(parm_tov, raw_tov)
            if m_fromv and m_tov:
                self.fromv = int(m_fromv.group(1))
                self.tov = int(m_tov.group(1))

        m_ipage = re.search(parm_ipage, raw_ipage)
        if m_ipage is None:
            self.status = False
            self.status_message = 'Unexpected ipage: %s' % raw_ipage
            return
        self.ipage = int(m_ipage.group(1))

        self.remarks = raw_remarks

        m_volume = re.search(parm_volume, raw_volume)
        if m_volume is None:
            self.status = False
            self.status_message = 'Unexpected volume: %s' % raw_volume
            return
        self.volume = int(m_volume.group(1))

        self.vpstr = '%s_%03d' % (self.volume, self.page)

    def todict(self):
        e = {
            'page': self.page,
            'volume': self.volume,
            'patala': self.patala,
            'v1': self.fromv,
            'v2': self.tov,
            'ipage': self.ipage,
            'remarks': self.remarks,
            'vp': self.vpstr,
        }
        return e

def init_pagerecs(filein):
    recs = []
    with open(filein, 'r', encoding='utf-8') as f:
        for iline, line in enumerate(f):
            if iline == 0:
                print('Skipping column title line:', line.rstrip())
                continue
            pagerec = Pagerec(line, iline)
            if pagerec.status:
                recs.append(pagerec)
            else:
                lnum = iline + 1
                print('Problem at line %s:' % lnum)
                print('line=', line.rstrip())
                print('message=', pagerec.status_message)
                exit(1)
    print(len(recs), 'Page records read from', filein)
    return recs

def make_js(recs):
    arr = []
    for rec in recs:
        d = rec.todict()
        arr.append(d)
    return arr

def write_recs(fileout, data):
    with open(fileout, 'w', encoding='utf-8') as f:
        f.write('indexdata = \n')
        jsonstring = json.dumps(data, indent=1)
        f.write(jsonstring + '\n')
        f.write('; // end of indexdata\n')
    print('json data written to', fileout)

if __name__ == '__main__':
    filein = sys.argv[1]
    fileout = sys.argv[2]
    pagerecs = init_pagerecs(filein)
    outrecs = make_js(pagerecs)
    write_recs(fileout, outrecs)
