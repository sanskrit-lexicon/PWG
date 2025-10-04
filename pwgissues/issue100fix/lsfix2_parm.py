# coding=utf-8
""" lsfix2_parm.py
"""
skips = ['RAGH. ed. Calc.',
             'RAGH. (ed. Calc.)',
             'RAGH. (Calc.)',
             '<ls n="RAGH.">ed. Calc.</ls>',]
targetobj2 = {
 # 
 'pwg': {'dictcode': 'pwg',
    'lscode': 'RAGH.', 'nparms': [2],
    'skip': skips,
    'skip1': [],
         },
 'pw': {'dictcode': 'pw',
    'lscode': 'RAGH.', 'nparms': [2],
    'skip': skips,
    'skip1': [],
           },
 'pwkvn': {'dictcode': 'pwkvn',
    'lscode': 'RAGH.', 'nparms': [2],
    'skip': skips,
    'skip1': [],
           },
 'sch': {'dictcode': 'sch',
    'lscode': 'Ragh.', 'nparms': [2],
    'skip': [],
    'skip1': [],
           },
 'mw': {'dictcode': 'mw',
    'lscode': 'Ragh.', 'nparms': [2],
    'skip': [],
    'skip1': [],
           },
}

