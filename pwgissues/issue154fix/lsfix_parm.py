# coding=utf-8
""" lsfix_parm.py
"""
targetobj = {
 'col4': 
   {'dictcode': 'pwg',
    'lscode': 'COL.',
    'nparm': 4,
    'skip': ['COL. Misc. Ess.'],
    },
 'col3': 
   {'dictcode': 'pwg',
    'lscode': 'COL.',
    'nparm': 3,
    'skip': ['COL. Misc. Ess.'],
    },
 'colebr4': 
   {'dictcode': 'pwg',
    'lscode': 'COLEBR.',
    'nparm': 4,
    'skip': ['COLEBR. Alg.', 'COLEBR. Misc.',
             'COLEBR. Gr.' ,
             'COLEBR. Dig.' , ],
     'skip1': ['<ls n="COLEBR.">Misc. Ess.',
               '<ls n="COLEBR.">Alg.',
               '<ls>COLEBR. I,',   # COLEBR. Misc. Ess. I,N
         ]
    }, 
 'colebr3': 
   {'dictcode': 'pwg',
    'lscode': 'COLEBR.',
    'nparm': 3,
    'skip': ['COLEBR. Alg.', 'COLEBR. Misc. Ess.' ],
    },
 }
