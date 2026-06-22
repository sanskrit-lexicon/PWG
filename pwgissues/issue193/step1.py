import re
import sys

replacements = {
    'AV': 'AV.',
    'BHĀG. P': 'BHĀG. P.',
    'DHĀTUP': 'DHĀTUP.',
    'HALL': 'HALL.',
    'HIT': 'HIT.',
    'HIT. ed. SCHL': 'HIT. ed. SCHL.',
    'KĀTY. ŚR': 'KĀTY. ŚR.',
    'MADHUS. ebend': 'MADHUS. ebend.',
    'MĀRK. P': 'MĀRK. P.',
    'MEGH': 'MEGH.',
    'P': 'P.',
    'R. GORR': 'R. GORR.',
    'SĀH': 'SĀH.',
    'Spr': 'Spr.',
    'ŚĀK': 'ŚĀK.',
    'TS. PRĀT': 'TS. PRĀT.',
    'Verz. d. B. H. No': 'Verz. d. B. H. No.',
    'Verz. d. Oxf. H. 109,a': 'Verz. d. Oxf. H. 109,a,',
    'Verz. d. Oxf. H. 71,a': 'Verz. d. Oxf. H. 71,a,',
    'Weber': 'WEBER',
    'VOP': 'VOP.',
}

input_file = sys.argv[1] if len(sys.argv) > 1 else 'temp_pwg0.txt'
output_file = sys.argv[2] if len(sys.argv) > 2 else 'temp_pwg1.txt'

with open(input_file, 'r', encoding='utf-8') as fin, \
     open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        for old, new in replacements.items():
            pattern = r'ls n="' + re.escape(old) + r'"(?=[ >])'
            repl = r'ls n="' + new + r'"'
            line = re.sub(pattern, repl, line)
        fout.write(line)

print(f"Processed {input_file} -> {output_file}")
