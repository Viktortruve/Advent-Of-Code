import numpy as np
from collections import defaultdict
from itertools import cycle
l = []
with open("input.txt") as file:
	for line in file:
		proj = line.strip().split("->")
		tuples = [(int(item.strip().split(',')[0]),int(item.strip().split(',')[1])) for item in proj if item != " "]
		l.append(tuples)
def q1():
	c = defaultdict(int)
	dz = [item for sublist in l for item in sublist]
	xs = [item[0] for item in dz]
	ys = [item[1] for item in dz]
	m_size = max(max(xs),max(ys))
	m = np.zeros((m_size+1,m_size+1))
	for item in l:
		if item[0][0] == item[1][0] or item[0][1] == item[1][1]:
			x_points = [item[0][0]] if item[0][0] == item[1][0] else [i for i in range(item[0][0],item[1][0]+1)] if item[1][0] > item[0][0] else [i for i in range(item[0][0],item[1][0]-1,-1)]
			y_points = [item[0][1]] if item[0][1] == item[1][1] else [i for i in range(item[0][1],item[1][1]+1)] if item[1][1] > item[0][1] else [i for i in range(item[0][1],item[1][1]-1,-1)]
			z = list(zip(x_points,cycle(y_points)) if len(x_points) > len(y_points) else zip(cycle(x_points),y_points))
			for t in z:
				c[t] += 1
	
	for k,v in c.items():
		m[k[0]][k[1]] = v
	return len([item for sublist in m for item in sublist if item >= 2])

def q2():
	c = defaultdict(int)
	dz = [item for sublist in l for item in sublist]
	xs = [item[0] for item in dz]
	ys = [item[1] for item in dz]
	m_size = max(max(xs),max(ys))
	m = np.zeros((m_size+1,m_size+1))
	for item in l:
		x_points = [item[0][0]] if item[0][0] == item[1][0] else [i for i in range(item[0][0],item[1][0]+1)] if item[1][0] > item[0][0] else [i for i in range(item[0][0],item[1][0]-1,-1)]
		y_points = [item[0][1]] if item[0][1] == item[1][1] else [i for i in range(item[0][1],item[1][1]+1)] if item[1][1] > item[0][1] else [i for i in range(item[0][1],item[1][1]-1,-1)]
		z = list(zip(x_points,cycle(y_points)) if len(x_points) > len(y_points) else zip(cycle(x_points),y_points))
		for t in z:
			c[t] += 1
	for k,v in c.items():
		m[k[0]][k[1]] = v
	return len([item for sublist in m for item in sublist if item >= 2])

ans1 = q1()
ans2 = q2()
print("Answer to question 1:",ans1)
print("Answer to question 2:",ans2)
