l = []
with open("input.txt") as file:
    for line in file:
        l.append(line.strip().split())

pos = [0,0,0]

def q1():
    pos = [0,0]
    for item in l:
        if item[0] == "forward":
            pos[0] += int(item[1])

        if item[0]  == "down":
            pos[1] += int(item[1])
        
        if item[0] == "up":
            pos[1] -= int(item[1])   
    return pos[0]*pos[1]

def q2():
    pos = [0,0,0]
    for item in l:
        if item[0] == "forward":
            pos[0] += int(item[1])
            pos[1] += int(item[1])*pos[2]

        if item[0]  == "down":
            pos[2] += int(item[1])
        
        if item[0] == "up":
            pos[2] -= int(item[1])
    return pos[0]*pos[1]
ans1 = q1()
ans2 = q2()

print("Answer for Question 1: ",str(ans1))
print("Answer for Question 2: ",str(ans2))



