import numpy as np
import pprint
m = []
with open("input.txt") as file:
	for line in file:
		l = []
		for word in line:
			if word != '\n':
				l.append(int(word))
		m.append(l)
	m = np.array(m)

min_x = 0
min_y = 0
max_x = len(m[0])
max_y = len(m)

def find_neighbors(m,y,x):
	n1 = None if x == max_x-1 else m[y][x+1]
	n4 = None if x == min_x else m[y][x-1]
	n2 = None if y == min_y else m[y-1][x]
	n3 = None if y == max_y-1 else m[y+1][x]
	return list(filter(lambda x: x is not None,[n1,n2,n3,n4]))

def find_neighbor_coordinates(m,y,x):
	n1 = None if x == max_x-1 else (y,x+1)
	n4 = None if x == min_x else (y,x-1)
	n2 = None if y == min_y else (y-1,x)
	n3 = None if y == max_y-1 else (y+1,x)
	return list(filter(lambda x: x is not None,[n1,n2,n3,n4]))

def get_recursive_neighbors(m,t,l):
	y = t[0][0]
	x = t[0][1]
	z = find_neighbors(m,y,x)
	cords = find_neighbor_coordinates(m,y,x)
	d = dict(zip(cords,z))
	sub_l = [(key,val) for (key,val) in d.items() if val < 9 and (key,val) not in l]
	if sub_l:
		for item in sub_l:
			l += sub_l
			return get_recursive_neighbors(m,item,l)
	else:
		return l

def q1():
	mins = []
	for i in range(0,max_y):
		for j in range(0,max_x):
			z = find_neighbors(m,i,j)
			if all([m[i][j] < item for item in z]):
				mins.append(m[i][j]+1)
	return sum(mins)

def q2():
	basins = []
	for i in range(0,max_y):
		for j in range(0,max_x):
			z = find_neighbors(m,i,j)
			cords = find_neighbor_coordinates(m,i,j)
			d = dict(zip(cords,z))
			if all([m[i][j] < item for item in z]):
				l = [(key,val) for (key,val) in d.items() if val < 9]
				l.append( ((i,j),m[i][j]) )
				basin = [get_recursive_neighbors(m,item,l) for item in l if item[0] != (i,j)]
				basins.append(len(basin[0]))
	return np.prod(sorted(basins, reverse=True)[0:3])

print("Answer to question 1: ",q1())
print("Answer to question 2: ",q2())
