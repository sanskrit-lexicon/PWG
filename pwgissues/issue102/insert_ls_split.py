import re

with open('temp_pwg.txt') as fin:
	for lin in fin:
		lin = lin.rstrip()
		matches = re.findall('<ls>RAGH. ([^<]+)</ls>', lin)
		sarga = ''
		verse = ''
		for m in matches:
			print(m)
			splits = m.split(' ')
			print(splits)
			for x in splits:
				if ',' in x:
					(sarga, verse) = x.split(',')
					ls = '<ls n="RAGH.">' + sarga + ',' + verse + '</ls>'
				else:
					verse = x
					ls = '<ls n="RAGH. ' + sarga + ',">' + verse + '</ls>'
				print(ls)



