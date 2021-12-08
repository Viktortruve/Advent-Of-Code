from itertools import permutations
import pprint
l = []
with open("input.txt") as file:
	for line in file:	
		x = tuple(line.strip().split('|'))
		l.append(x)

def q1(l):
	c = 0
	for t in l:
		x = t[1].split()
		for seg in x:
			l  = len(seg)
			if l == 2 or l == 4 or l == 3 or l == 7:
				c +=1
	return c

def evaluate(x):
	one = [set(item) for item in x if len(item) == 2][0]
	four = [set(item) for item in x if len(item) == 4][0]
	zero = [set(item) for item in x if len(item) == 6 and one.issubset(item) and len(set(item).intersection(four)) == 3][0]
	nine = [set(item) for item in x if len(item) == 6 and one.issubset(item) and len(set(item).intersection(four)) == 4][0]
	six = [set(item) for item in x if len(item) == 6 and not one.issubset(item)][0]
	three = [set(item) for item in x if len(item) == 5 and one.issubset(item) and len(set(item).intersection(six)) == 4][0]
	five = [set(item) for item in x if len(item) == 5 and len(set(item).intersection(six)) == 5][0]
	two = [set(item) for item in x if len(item) == 5 and not one.issubset(item) and len(set(item).intersection(six)) == 4][0]

	return dict(list(map(lambda x: ("".join(list(x[0])),x[1]),[(zero,'0'),(two,'2'),(three,'3'),(five,'5'),(six,'6'),(nine,'9')])))

def q2(l):
	d = {}
	vals = []
	for t in l:
		x = t[0].split()
		output_val = []
		d = evaluate(x)
		output = t[1].split()
		for seg in output:
			if len(seg) == 2:
				output_val.append('1')
			elif len(seg) == 7:
				output_val.append('8')
			elif len(seg) == 4:
				output_val.append('4')
			elif len(seg) == 3:
				output_val.append('7')
			else:
				ps = permutations(seg)
				output_val.append(d[ ["".join(item) for item in ps if "".join(item) in d][0]])
		vals.append(int("".join(output_val)))
	
	return sum(vals)
print("Answer to question 1:",q1(l))
print("Answer to question 2:",q2(l))

