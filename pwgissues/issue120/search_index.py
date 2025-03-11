import re
import sys
import operator
import json

alphabets = 'aAiIuUfxFXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh'

def str_to_int():
	result = {}
	counter = 1
	for x in alphabets:
		result[x] = counter
		counter += 1
	return result

alphint = str_to_int()

def convert_str_to_int(text):
	result = []
	for y in text:
		result.append(alphint[y])
	return result

def terminal_consonant(text):
	p = re.sub('[aAiIuUfxFXeEoOMH]*', '', text)
	if len(p) > 0:
		q = alphint[p[-1]]
	else:
		q = 0
	return q

def vowels(text):
	counter = 0
	for x in text:
		if x in 'aAiIuUfxFXeEoO':
			counter += 1
	return counter


class Rec(object):
	def __init__(self, s):
		i = convert_str_to_int(s)
		t = terminal_consonant(s)
		v = vowels(s)
		self.s = s
		self.i = i
		self.t = t
		self.v = v
	
	def print_details(self):
		print('string:', self.s)
		print('integer:', self.i)
		print('terminal consonant:', self.t)
		print('vovels:', self.v)


def sort_per_medini(listOfWords):
	reclist = [Rec(x) for x in listOfWords]
	reclist.sort(key=operator.attrgetter('t', 'v', 'i'))
	return [x.s for x in reclist]


def check_whether_before(test, base):
	x = sort_per_medini([test, base])
	if x[0] == test:
		return True
	else:
		return False



if __name__ == "__main__":
	input_word = sys.argv[1]
	with open('index_v1.js') as jin:
		index_data = json.loads(jin.read())
	for ind in index_data:
		base = ind['hw']
		page = ind['page']
		adhy = ind['adhy']
		if adhy in ['avy', 'coloph'] or base == '':
			continue
		else:
			if check_whether_before(input_word, base):
				print(input_word + ' is before ' + base + ' on page ' + str(page-1))
				break
