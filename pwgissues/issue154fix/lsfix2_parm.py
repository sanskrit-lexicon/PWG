# coding=utf-8
""" lsfix2_parm.py
"""
targetobj2 = {
 # COLEBR.
 'colebr': {'dictcode': 'pwg',
    'lscode': 'COLEBR.', 'nparms': [4,3],
    'skip': ['COLEBR. Alg.', 'COLEBR. Misc.',
             'COLEBR. Gr.' ,
             'COLEBR. Dig.' , ],
    'skip1': ['<ls n="COLEBR.">Misc. Ess.',
               '<ls n="COLEBR.">Alg.',
               '<ls>COLEBR. I,',   # COLEBR. Misc. Ess. I,N
              ],
    },
 # COL.
 'col': {'dictcode': 'pwg',
    'lscode': 'COL.', 'nparms': [4,3],
         'skip1' : ['<ls>COL. Misc.'],
    },
 # AK. ed. COLEBR.
  'akcol' :{'dictcode': 'pwg',
    'lscode': 'AK. ed. COLEBR.', 'nparms': [4,3],
         'skip1' : ['<ls>COL. Misc.'],
    }
}

