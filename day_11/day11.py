import numpy as np
import pprint
import copy
m = []
with open("input.txt") as file:
	for line in file:
		l = []
		for word in line:
			if word != '\n':
				l.append(int(word))
		m.append(l)
	m = np.array(m)
	m2 = copy.copy(m)

min_x = 0
min_y = 0
max_x = len(m[0])
max_y = len(m)

def find_neighbors(m,y,x):
	n1 = None if x == max_x-1 else ((y,x+1),m[y][x+1])
	n2 = None if x == min_x else ((y,x-1),m[y][x-1])
	n3 = None if y == min_y else ((y-1,x),m[y-1][x])
	n4 = None if y == max_y-1 else ((y+1,x),m[y+1][x])
	n5 = None if y == max_y-1 or x == max_x-1 else ((y+1,x+1),m[y+1][x+1])
	n6 = None if y == min_y or x == min_x else ((y-1,x-1),m[y-1][x-1])
	n7 = None if y == max_y-1 or x == min_x else ((y+1,x-1),m[y+1][x-1])
	n8 = None if y == min_y or x == max_x -1 else ((y-1,x+1),m[y-1][x+1])
	return dict(list(filter(lambda x: x is not None,[n1,n2,n3,n4,n5,n6,n7,n8])))

def flash(m,l):
	for item in l:
		neighs = find_neighbors(m,item[0],item[1])
		for n in neighs.keys():
			old_val = m[n[0]][n[1]]
			m[n[0]][n[1]] = old_val + 1 if old_val != 0 else 0
	return m

def q1(m):
	flashcount = 0
	for n in range(0,100):
		m += 1
		b = len(np.argwhere(m > 9))
		while(b > 0):
			l = np.argwhere(m > 9)
			m = np.where(m > 9,0,m)
			m = flash(m,l)
			b = len(np.argwhere(m > 9))
		flashcount += len(np.argwhere(m == 0))
	return flashcount

def q2(m):
	c = 0
	while(len(np.argwhere(m == 0)) != len(m)*len(m[0])):
		m += 1
		b = len(np.argwhere(m > 9))
		while(b > 0):
			l = np.argwhere(m > 9)
			m = np.where(m > 9,0,m)
			m = flash(m,l)
			b = len(np.argwhere(m > 9))
		c += 1
	return c
print("Answer to question 1:",q1(m))
print("Answer to question 2:",q2(m2))