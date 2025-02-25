import re
import sys

dictregexes = {'RAGH': [('(<ls>RAGH. )([0-9]+,[0-9, .]+)(</ls>)', 'one'), ('<ls n="RAGH.">([0-9]+,[0-9, .]+)</ls>', 'two')]}

def one(number_string, ls_name):
	# Given string => <ls>RAGH. 3,39. 42. 4,43. 12,29.</ls>
	# Expected string => <ls>RAGH. 3,39.</ls> <ls n="RAGH. 3,">42.</ls> <ls n="RAGH.">4,43.</ls> <ls n="RAGH.">12,29.</ls>
	# If there is only reference to shloka, bring sarga from previous one and note it in 'n' tag.
	number_string = number_string.rstrip()
	if '<ls>' + ls_name in number_string:
		ns_stripped = number_string.replace('<ls>' + ls_name + '. ', '')
		ns_stripped = ns_stripped.replace('</ls>', '')
		#print(ns_stripped)
		if re.search('^([0-9]+,)[0-9, .]+$', ns_stripped):
			#print(ns_stripped)
			result = []
			splits = ns_stripped.split(' ')
			#print(splits)
			first = splits[0]
			(sarga, shloka) = first.split(',')
			result.append('<ls>' + ls_name + '. ' + sarga + ',' + shloka + '</ls>')
			for x in splits[1:]:
				if ',' in x:
					(sarga, shloka) = x.split(',')
					ls = '<ls n=' + ls_name + '. >' + sarga + ',' + shloka + '</ls>'
				else:
					shloka = x
					ls = '<ls n="' + ls_name + '. ' + sarga + ',">' + shloka + '</ls>'
				result.append(ls)
			print(number_string + '\t' + ' '.join(result))
		else:
			print('ERROR', number_string)
	else:
		print('ERROR', number_string)

if __name__ == "__main__":
	filein = sys.argv[1]
	fileout = sys.argv[2]
	reject = sys.argv[3]
	fin = open(filein, 'r')
	for lin in fin:
		one(lin, 'RAGH')
		
