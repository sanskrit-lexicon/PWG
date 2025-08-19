# coding=utf-8
""" lsfix2_parm.py
"""
targetobj2 = {
 # 
 'spra': {'dictcode': 'pwg',
    'lscode': 'Spr.', 'nparms': [1],
    'skip1': ['<ls n="Spr.">(II)',
              '<ls>Spr. (II)',
              '<ls n="Spr. (II)',
              ]
   },
 'sprb': {'dictcode': 'pwg',
    'lscode': 'Spr.', 'nparms': [1],
    # 'skip': ['Spr. (II)', 'Spr. (I)'],
    'skip1': ['<ls n="Spr.">(II)',
              '<ls>Spr. (II)',
              '<ls n="Spr. (II)',
              '<ls n="Spr.">(I)',
              '<ls n="Spr. (I)">',
              '<ls>Spr. (I)',
              ]
   },

 'sprc': {'dictcode': 'pwg',
    'lscode': 'Spr. \(I\)', 'nparms': [1],
    # 'skip': [],
    'skip1': []
   },
}

