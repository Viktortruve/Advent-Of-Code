import numpy as np
import astar
m = []
with open("input.txt") as file:
	for line in file:
		l = []
		for word in line:
			if word != '\n':
				l.append(int(word))
		m.append(l)
	m = np.array(m)

def find_neighbors(m,y,x,max_y,max_x):
	n1 = None if x == max_x-1 else ((y,x+1),m[y][x+1])
	n2 = None if x == 0 else ((y,x-1),m[y][x-1])
	n3 = None if y == 0 else ((y-1,x),m[y-1][x])
	n4 = None if y == max_y-1 else ((y+1,x),m[y+1][x])	
	return dict(list(filter(lambda x: x is not None,[n1,n2,n3,n4])))

def find_neighs(y,x,max_y,max_x):
	n1 = None if x == max_x-1 else (y,x+1)
	n2 = None if y == max_y-1 else (y+1,x)
	return list(filter(lambda x: x is not None,[n1,n2]))

def reconstruct_path(prev,current):
	total_path = [current]
	while current in prev.keys():
		current = prev[current]
		total_path.insert(0,current)
	return total_path

def manhattan_distance(c1,c2):
	(x1,y1) = c1
	(x2,y2) = c2
	return abs(y2-y1) + abs(x2-x1)

def A_Star(m,start, goal):
	max_y = len(m)
	max_x = len(m[0])

	openSet = set()
	openSet.add(start)
	cameFrom = {}
	fScore = {}
	gScore = {}
	h = {}
	for i in range(0,len(m)):
		for j in range(0,len(m[0])):
			gScore[(i,j)] = 100000
			h[(i,j)] = manhattan_distance((i,j),goal)
			fScore[(i,j)] = 100000
	gScore[start] = 0
	fScore[start] = h[start]
	while openSet != {}:
		current = min([item for item in fScore.keys() if item in openSet])
		if current == goal:
			return reconstruct_path(cameFrom, current)

		openSet.remove(current)
		neighbors = find_neighbors(m,current[0],current[1],max_y,max_x)
		for n,c in neighbors.items():
			tentative_gScore = gScore[current] + c
			if tentative_gScore < gScore[n]:
				cameFrom[n] = current
				gScore[n] = tentative_gScore
				fScore[n] = tentative_gScore + h[n]
				if n not in openSet:
					openSet.add(n)

	return

def expand(m):
	max_y = len(m)
	max_x = len(m[0])
	n = np.zeros((max_y*5,max_x*5))
	zs = []
	for i in range(0,max_y):
		for j in range(0,max_x):
			z = np.zeros( (max_y//2,max_x//2) )
			z[0][0] = m[i][j]
			for k in range(0,max_y//2):
				for j in range(0,max_x//2):
					ns = find_neighs(k,j,max_y//2,max_x//2)
					for item in ns:
						z[item[0]][item[1]] = 1 if z[k][j] == 9 else z[k][j] + 1
			zs.append(z)
	i = 0
	j = 0
	c = 0
	
	for z in zs:
		if c == len(m):
			j += 1
			c = 0
			i = 0
		offset_y = 0 
		offset_x = 0		
		for row in z:
			for ele in row:
				y = j + offset_y if j + offset_y < 5*max_y else 5*max_y-1
				x = i + offset_x if i + offset_x < 5*max_x else 5*max_x-1
				n[y][x] = ele 
				offset_x += max_x
			
			offset_x = 0
			offset_y += max_y
		c += 1
		i += 1
	return n


def q1(m): 
	start = (0,0)
	goal = (len(m)-1,len(m[0])-1)
	path = A_Star(m,start,goal)
	return sum([m[p[0]][p[1]] for p in path])-m[0][0]

def q2(m):
	start = (0,0)
	m = expand(m)
	max_x = len(m[0])
	max_y = len(m)
	goal = (len(m)-1,len(m[0])-1)
	path = A_Star(m,start,goal)		
	return sum([m[p[0]][p[1]] for p in path])-m[0][0]

print("Answer to question 1:",q1(m))
print("Answer to question 2:",q2(m))



