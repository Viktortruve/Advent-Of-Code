
from collections import defaultdict

opens = ['(','[','{','<']
close = [')',']','}','>']

d0 = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137 }
d = { 
	')': '(',
	']': '[',
	'}': '{',
	'>': '<' }

with open("inp.txt") as file:
	l = file.readlines()

incomplete = []

def q1(l):
	stack = []
	illegal = defaultdict(int)
	for line in l:
		broken = False
		for word in line:
			if word in opens:
				stack.append(word)
			elif word in close:
				x = stack[-1]
				stack.pop()
				if d[word] != x:
					broken = True
					illegal[word] += 1
		if not broken:
			incomplete.append(line)
	return sum([illegal[item]*d0[item] for item in illegal.keys()])

d2= {
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>'}
d3 = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4}

def q2(l):
	ts = []
	for line in l:
		stack = []
		for word in line:
			if word in opens:
				stack.append(word)
			elif word in close:
				stack.pop()
		
		stack.reverse()
		t = 0
		stack = [d2[item] for item in stack]
		for item in stack:
			t *= 5
			t += d3[item]
		ts.append(t)

	s = sorted(ts)
	return s[len(s)//2]

print("Answer to question 1",q1(l))
print("Answer to question 2",q2(incomplete))
