a = []

with open("input.txt") as file:
	for line in file:
		a.append(int(line.strip()))
def q1():
    return [ a[i+1] > a[i] for i in range(0,len(a)-1)].count(True)

def q2():
    return [ sum(a[i+1:i+4]) > sum(a[i:i+3]) if len(a[i+1:i+4]) == 3 else False for i in range(0,len(a)-3)].count(True)

ans1 = q1()
ans2 = q2()

print("Answer to Question 1:",ans1)
print("Answer to Question 2:",ans2)



