from functools import cache

with open("input.txt") as file:
	l = [int(item) for item in " ".join(file.readlines()).split(',')]
def q1():
	align_costs = {}
	for i in range(0,max(l)+1):
		align_cost = 0
		for j in range(0,len(l)):
			align_cost += abs(i-l[j])
		align_costs[i] = align_cost
	return min(align_costs.values())

@cache
def calc(a,b):
	diff = abs(a-b)
	return (diff)*(diff+1)/2

def q2():
	align_costs = {}
	for i in range(0,max(l)+1):
		align_cost = 0
		for j in range(0,len(l)):
			align_cost += calc(l[j],i)
		align_costs[i] = align_cost
	return min(align_costs.values())

print("Answer to question 1:",q1())
print("Answer to question 2:",q2())

