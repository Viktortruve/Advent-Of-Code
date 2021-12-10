score = { ")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
score2 = { ")" : 1, "]" : 2, "}" : 3, ">" : 4}

match = { ")" : "(", "]" : "[", "}" : "{", ">" : "<"}
match2 = { "(" : ")", "[" : "]", "{" : "}", "<" : ">"}

counter = 0
counter2 = 0
counterList = []
for lines in open("inp.txt").read().splitlines():
    ansList = []
    matchingList = []
    corrupted = False
    counter2 = 0
    for char in lines:
        if char in match.values():
            ansList.append(char)
        if char in match.keys():
            last = ansList.pop()
            if match[char] != last:
                counter += score[char]
                corrupted = True
                break
    if not corrupted:
        for ans in ansList:
            matchingList.append(match2[ansList.pop()])
        for mat in matchingList:
            counter2 *= 2
            counter2 += score[mat]
        counterList.append(counter2)
print(counter)
counterList.sort()
print(len(counterList))
print(counterList[27])