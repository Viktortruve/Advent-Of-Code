import math
from itertools import chain
import numpy as np
import pprint
from collections import defaultdict
with open("input.txt") as file:
	l = [int(item) for item in "".join(file.readlines()).split(",")]

def case(item):
	if(item == 0):
		return (6,8)
	if(item > 0):
		return item-1
def q1(l):
	x = l
	for i in range(0,80):
		x = [case(item) for item in x]
		x = list(chain(*(i if isinstance(i, tuple) else (i,) for i in x)))
	return(len(x))

def q2(l):
	c = defaultdict(int)
	for item in l:
		c[item] += 1
	for i in range(0,255):
		for j in range(1,10):
			c[j-1] = c[j]
		c[7] += c[0]
		c[9] = c[0]
		c[0] = 0
	return sum(c.values())

ans1 = q1(l)
print("Anser to question 1:",ans1)
ans2 = q2(l)
print("Answer to question 2:",ans2)


