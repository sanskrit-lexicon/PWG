#-*- coding:utf-8 -*-
"""lsparse2.py
	Module to create automated suggestions for parsing lsexamine2_XXXX_other1.txt files.
	
	Usage - python lsparse2.py BOOKNAME lsexamine2_BOOKNAME_other1.txt auto.txt manual.txt
	Author - Dr. Dhaval Patel
	email - drdhaval2785@gmail.com
	Date - 26 February 2025
"""
from __future__ import print_function
import re
import sys

dictregexes = {'RAGH': [('(<ls>RAGH. )([0-9]+,[0-9, .]+)(</ls>)', 'one'), ('<ls n="RAGH.">([0-9]+,[0-9, .]+)</ls>', 'two')]}

def two(number_string_list, ls_name):
	done = []
	pending = []
	for number_string in number_string_list:
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
						ls = '<ls n="' + ls_name + '.">' + sarga + ',' + shloka + '</ls>'
					else:
						shloka = x
						ls = '<ls n="' + ls_name + '. ' + sarga + ',">' + shloka + '</ls>'
					result.append(ls)
				#print(number_string + '\t' + ' '.join(result))
				alt = number_string + '\t' + ' '.join(result)
				done.append(alt)
			else:
				#print('ERROR', number_string)
				#return 'ERROR\t' + number_string
				pending.append(number_string)
		else:
			#print('ERROR', number_string)
			#return 'ERROR\t' + number_string
			pending.append(number_string)
	return(done, pending)


def two_ref(previously_done_list, pending_list, ls_name):
	done = previously_done_list
	pending = []
	for number_string in pending_list:
		# Given string => <ls n="RAGH.">3,20. 12,23.</ls>
		# Expected string => <ls n="RAGH.">3,20.</ls> <ls n=RAGH.">12,23.</ls>
		# If there is only reference to shloka, bring sarga from previous one and note it in 'n' tag.
		number_string = number_string.rstrip()
		#print(number_string)
		if '<ls n="' + ls_name + '.">' in number_string:
			ns_stripped = number_string.replace('<ls n="' + ls_name + '.">', '')
			ns_stripped = ns_stripped.replace('</ls>', '')
			if re.search('^([0-9]+,[0-9]+[.])[0-9, .]*$', ns_stripped):
				#print(ns_stripped)
				result = []
				splits = ns_stripped.split(' ')
				#print(splits)
				for x in splits:
					if ',' in x:
						(sarga, shloka) = x.split(',')
						ls = '<ls n="' + ls_name + '.">' + sarga + ',' + shloka + '</ls>'
					else:
						shloka = x
						ls = '<ls n="' + ls_name + '. ' + sarga + ',">' + shloka + '</ls>'
					result.append(ls)
				#print(number_string + '\t' + ' '.join(result))
				alt = number_string + '\t' + ' '.join(result)
				done.append(alt)
			else:
				#print('ERROR', number_string)
				#return 'ERROR\t' + number_string
				pending.append(number_string)
		else:
			#print('ERROR', number_string)
			#return 'ERROR\t' + number_string
			pending.append(number_string)
	return(done, pending)


def print_status(done, pending):
	print('DONE:\t\t', len(done))
	print('PENDING:\t', len(pending))

if __name__ == "__main__":
	ls_name = sys.argv[1]
	filein = sys.argv[2]
	fileout = sys.argv[3]
	reject = sys.argv[4]
	fin = open(filein, 'r')
	fout = open(fileout, 'w')
	rout = open(reject, 'w')
	datain = fin.read().split('\n')
	# Ignore the last blank entry while splitting on linebreak.
	datain = datain[:-1]
	(done, pending) = two(datain, ls_name)
	print('FIRST ROUND DONE.')
	print_status(done, pending)
	(done, pending) = two_ref(done, pending, ls_name)
	print('SECOND ROUND DONE.')
	print_status(done, pending)
	fout.write('\n'.join(done))
	rout.write('\n'.join(pending))
	fin.close()
	fout.close()
	rout.close()

