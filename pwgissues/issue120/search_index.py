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

index_data = [
 {
  "page": 384,
  "v1": 22,
  "v2": 36,
  "x1": "b",
  "x2": "a",
  "vp": "384",
  "st": "ka"
 },
  {
  "page": 385,
  "v1": 10,
  "v2": 22,
  "x1": "",
  "x2": "a",
  "vp": "383",
  "st": "aNga"
 }
]

if __name__ == "__main__":
	listOfWords = ['cayAna', 'cayana', 'caraRa', 'camaka', 'caRqa', 'kamala', 'kalmalA', 'fzi', 'fki', 'Saki']
	result = sort_per_medini(listOfWords)
	print(result)
	#print(check_whether_before('kARqa', 'caRqa'))
	input_word = sys.argv[1]
	for ind in index_data:
		base = ind['st']
		page = ind['page']
		if check_whether_before(input_word, base):
			continue
		else:
			print(input_word + ' is on page ' + str(page))
