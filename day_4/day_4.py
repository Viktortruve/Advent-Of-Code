import numpy as np
from collections import defaultdict
import pprint
first = True
skip = True
players = defaultdict(list)
with open("input.txt") as file:
	player = 0
	for line in file:
		if first:
			numbers = line.strip().split(',')
			numbers = [int(item) for item in numbers]
			first = False
			continue
		if skip:
			skip = False
			continue
		if not line.strip().split():
			player += 1;
			continue
		row = line.strip().split()
		row = [int(item) for item in row]
		players[player].append(row)



def has_bingo(numbers,m):
	 last_num = numbers[len(numbers)-1]
	 c = np.transpose(m)
	 x = [item for item in c if set(item).issubset(set(numbers))]
	 y = [item for item in m if set(item).issubset(set(numbers))]
	 if x or y:
	 	return (x,last_num) if x else (y,last_num)
	 return False

def q1():
	for i in range(0,len(numbers)):
		for v in players.values():
			q = has_bingo(numbers[:i+1],v)
			if q:
				l,num = q
				flat_v = [item for sublist in v for item in sublist]
				return num*sum([item for item in flat_v if item not in numbers[:i+1]])
def q2():
	finished = []
	bingos = []
	for i in range(0,len(numbers)):
		for k,v in players.items():
			if k in finished:
				continue
			q = has_bingo(numbers[:i+1],v)
			if q:
				l,num = q
				flat_v = [item for sublist in v for item in sublist]
				bingos.append(num*sum([item for item in flat_v if item not in numbers[:i+1]]))
				finished.append(k)
	return bingos[len(bingos)-1]
ans1 = q1()
ans2 = q2()

print("Answer to question 1:",ans1)
print("Answer to question 2:",ans2)

