# coding=utf-8
""" lsfix2_parm.py
"""

skips = []
targetobj2 = {
 # 
 'pwg': {'dictcode': 'pwg',
    'lscode': 'RĀJA-TAR. ed. Calc.', 'nparms': [2],
         'skip': [],'skip1': [],
         },

 'pwga': {'dictcode': 'pwg',
    'lscode': 'RĀJA-TAR.', 'nparms': [2],
         'skip': [],
          'skip1': ['<ls>RĀJA-TAR. ed. Calc.',
         '<ls n="RĀJA-TAR. ed. Calc.'],
          'outopt':'1', # sort 
         },

 'pwgb': {'dictcode': 'pwh',
    'lscode': 'RĀJAT.', 'nparms': [2],
          'skip': [],
    'skip1': [],
          },
    
 'pw': {'dictcode': 'pw',
    'lscode': 'RĀJAT.', 'nparms': [2],
    'skip': ['RĀJAT. ed. Calc.'],
    'skip1': [],
           },
 'pwkvn': {'dictcode': 'pwkvn',
    'lscode': 'RĀJAT.', 'nparms': [2],
    'skip': [],
    'skip1': [],
           },
 'sch': {'dictcode': 'sch',
    'lscode': 'Rājat.', 'nparms': [2],
    'skip': [],
    'skip1': [],
         },
 'mw': {'dictcode': 'mw',
    'lscode': 'Rājat.', 'nparms': [2],
    'skip': ['Rājat. (C)'],
    'skip1': [],
           },
}

