import pprint
from collections import defaultdict
l = []
with open("input.txt") as file:
	for line in file:
		l.append(line.strip())
z = defaultdict(int)
o = defaultdict(int)
for item in l:
	for i in range(0,len(item)):
		if item[i] == "0":
			z[i] += 1
		else:
			o[i] +=1

def replacer(s, newstring, index, nofail=False):
    if index < 0: 
        return newstring + s
    if index > len(s): 
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

def  q1():
	gamma = []
	epsilon = []
	for k in range(0,len(z)):
		if o[k] > z[k]:
			gamma.append('0')
			epsilon.append('1')
		else:
			gamma.append('1')
			epsilon.append('0')

	return int("".join(gamma),2) *int("".join(epsilon),2)

def q2(l,c):
	sub_l = l
	if c == 'OXYGEN':
		for i in range(0,len(l[0])):
			z = [item for item in sub_l if item[i] == '0']
			o = [item for item in sub_l if item[i] == '1']
			if len(z) > len(o):
				sub_l = z
			elif len(o) > len(z):
				sub_l = o
			else:
				sub_l  = [replacer(item,'1',i) for item in sub_l]
	if c == 'CO2':
		for i in range(0,len(l[0])):
			if(len(sub_l) == 1):
				break
			z = [item for item in sub_l if item[i] == '0']
			o = [item for item in sub_l if item[i] == '1']
			if len(z) > len(o):
				sub_l = o
			elif len(o) > len(z):
				sub_l = z
			else:
				sub_l = z
	return int(sub_l[0],2)

ans1 = q1()
x = q2(l,"OXYGEN")
y = q2(l,"CO2")
ans2 = x*y
print("Answer to part 1:",ans1)
print("Answer to part 2:",ans2)






