import numpy as np
import pprint
l = []
folds = []
np.set_printoptions(linewidth=np.inf)
with open("input.txt") as file:
	for line in file:
		if len(line) == 1:
			continue
		if ',' not in line:
			if 'x' in line:
				folds.append(('x',line.strip().split()[2][2]))
			else:
				folds.append(('y',line.strip().split()[2][2]))
			continue
		l.append([int(item) for item in line.strip().split(',')])


def h_fold(m,max_y,max_x):
	size_x = len(m[0])
	size_y = len(m)//2
	n = np.full((size_y,size_x),'.')
	for y in range(0,size_y):
		for x in range(0,size_x):
			n[y][x] = '#' if m[y][x] == '#' or m[max_y-y-1][x] == '#' else '.'
	return n
def v_fold(m,max_y,max_x):
	size_x = len(m[0])//2
	size_y = len(m)
	n = np.full((size_y,size_x),'.')
	for y in range(0,size_y):
		for x in range(0,size_x):
			n[y][x] = '#' if m[y][x] == '#' or m[y][max_x-x-1] == '#' else '.'
	return n

def q1(l):
	max_x = max([item[0] for item in l])+1
	max_y = max([item[1] for item in l])+1
	m = np.full((max_y,max_x),'.')
	for y in range(0,max_y):
		for x in range(0,max_x):
			m[y][x] = '#' if [x,y] in l else '.'
	for f in folds:
		if 'y' in f:
			m = h_fold(m,max_y,max_x)
		elif 'x' in f:
			m = v_fold(m,max_y,max_x)
		return len(np.argwhere(m == '#'))

def q2(l):
	max_x = max([item[0] for item in l])+1
	max_y = max([item[1] for item in l])+1
	m = np.full((max_y,max_x),'.')
	for y in range(0,max_y):
		for x in range(0,max_x):
			m[y][x] = '#' if [x,y] in l else '.'
	for f in folds:
		if 'y' in f:
			m = h_fold(m,max_y,max_x)
		elif 'x' in f:
			m = v_fold(m,max_y,max_x)
		max_x = len(m[0])
		max_y = len(m)
	return m
print("Answer to question 1",q1(l))
ans2 = q2(l)
max_y = len(ans2)
max_x = len(ans2[0])
for y in range(0,max_y):
	print(ans2[y])

