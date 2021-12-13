from collections import defaultdict
import pprint
g = defaultdict(list)
with open("input.txt") as file:
	for line in file:
		l = line.strip().split('-')
		g[l[0]].append(l[1])
		g[l[1]].append(l[0])


def traverse(g,l):
	small_caves = list(set([item for item in l if item.islower()]))
	
	x = [l.count(item) for item in small_caves]
	if 'end' in l or any([item > 1 for item in x]):
		return [l] if 'end' in l else []

	neighs = g[l[-1]]
	return [item for sublist in list(map(lambda x: traverse(g,l+[x]),neighs)) for item in sublist]

def q1(g):
	paths = []
	l = g['start']
	for item in l:
		traversed = [item]
		traversed = traverse(g,traversed)
		for p in traversed:
			if not 'start' in p:
				paths.append(p)
	return len(paths)


def traverse2(g,l):
	small_caves = list(set([item for item in l if item.islower()]))
	x = [l.count(item) for item in small_caves]
	if 'end' in l or len([item for item in x if item >= 2]) > 1 or 3 in x:
		return [l]
	neighs = [item for item in g[l[-1]] if item != 'start']
	return [item for sublist in list(map(lambda x: traverse2(g,l+[x]),neighs)) for item in sublist]

def q2(g):
	paths = []
	l = g['start']
	for item in l:
		traversed = [item]
		traversed = traverse2(g,traversed)
		for p in traversed:
			if 'end' in p:
				paths.append(p)
			
	return len(paths)



print("Answer to question 1:",q1(g))
print("Answer to question 2:",q2(g))

