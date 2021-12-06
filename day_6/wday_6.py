import numpy as np

def day6(days,fishlist):
    numbers = np.arange(-1,9)
    fishDict = {}
    for i in numbers:
        fishDict[i] = len(np.argwhere(fishlist==i))
    for d in range(days):
        for key in fishDict:
            if key == 8:
                break
            fishDict[key] = fishDict[key+1]
        fishDict[6] += fishDict[-1]
        fishDict[8] = fishDict[-1]
        fishDict[-1] = 0
    sum = 0
    for key in fishDict:
        sum += fishDict[key]
    return sum

fishlist = []
ls = open("inp.txt").read().split(",")
for fish in ls:
    fishlist.append(int(fish))
fishlist = np.array(fishlist)

days = 80
ans1 = day6(days,fishlist)

days = 256
ans2 = day6(days,fishlist)

print("Answer 1 =",ans1,"fishes")
print("Answer 2 =",ans2,"fishes")