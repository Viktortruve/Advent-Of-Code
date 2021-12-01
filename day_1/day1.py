a = []
test = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]
with open("input.txt") as file:
	for line in file:
		a.append(int(line.strip()))
def q1():
    c = 0
    for i in range(0,len(a)-1):
        if(a[i+1] > a[i]):
            c += 1
    print(c)

q1()

def q2():
    c = 0
    for i in range(0,len(a)-3):
        l1 = a[i:i+3]
        l2 = a[i+1:i+4]
        if len(l2) < 3:
            break
        if sum(l2) > sum(l1):
            c += 1 
    print(c)

q2()





