from collections import defaultdict
import pprint
import time
rules = {}
mutations = defaultdict(list)
c = defaultdict(int)

with open("input.txt") as file:
	for line in file:
		if '->' in line:
			x = line.strip().split('->')
			x = [item.strip() for item in x]
			rules[x[0]] = x[0][0] + x[1] + x[0][1]
			mutations[x[0]].append(x[0][0] + x[1])
			mutations[x[0]].append(x[1] + x[0][1])
			c[x[0]] = 0 
		elif len(line) == 1:
			continue
		else:
			s = list(line.strip())

def q1(s):
	n = 2
	m = 1
	org_str = [s[i:i+n] for i in range(0, len(s), n-m) if len(s[i:i+n]) == 2]
	for i in range(0,10):
		l = [rules[item[0]+item[1]] for item in org_str]
		f = [l[0]]
		s = "".join(f + [item[1:3] for item in l[1:]])
		org_str = [s[i:i+n] for i in range(0, len(s), n-m) if len(s[i:i+n]) == 2]
	d = {}
	for item in set(s):
		d[item] = s.count(item)

	return(max(d.values())-min(d.values()))


def q2(s):
	n = 2
	m = 1
	letter_counter = defaultdict(int)	
	letter_counter[s[0]] = 1
	letter_counter[s[-1]] = 1
	org_str = [s[i:i+n] for i in range(0, len(s), n-m) if len(s[i:i+n]) == 2]
	
	for t in org_str:
		x = "".join(t)
		c[x] += 1
	
	for i in range(0,40):
		tmp = {}
		for key,val in c.items():
			l = ([c[k] for (k,v) in mutations.items() if key in v])
			tmp[key] = sum(l)
		for k,v in tmp.items():
			c[k] = v
	
	for k,v in c.items():
		letter_counter[k[0]] += v  
		letter_counter[k[1]] += v
	
	for k,v in letter_counter.items():
		letter_counter[k] = v // 2
	
	return(max(letter_counter.values())-min(letter_counter.values()))

print("Answer to question 1:",q1(s))
print("Answer to question 2:",q2(s))
