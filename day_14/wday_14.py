import re
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
ls = open("inp.txt").read().splitlines()
elementDict = defaultdict(int)
p1 = []
p2 = []
p3 = []
steps = 40
for lines in ls:
    if '>' not in lines and len(lines)!=0:
        initialPair = lines
    elif len(lines)!=0:
        p1.append(lines[0])
        p2.append(lines[1])
        p3.append(lines[-1])
tmpList = []
firstChar = initialPair[0]
lastChar = initialPair[-1]
for i in range(len(initialPair)-1):
    elementDict[initialPair[i]+initialPair[i+1]] += 1
for t in range(steps):
    indexPair = []
    tmpDict = defaultdict(int)
    for i in range(len(p1)):
        subStr = p1[i]+p2[i]
        if subStr in elementDict.keys():
            tmpDict[subStr] -= elementDict[subStr]
            tmpDict[p1[i] + p3[i]] += elementDict[subStr]
            tmpDict[p3[i] + p2[i]] += elementDict[subStr]
    for pa in tmpDict.keys():
        elementDict[pa] += tmpDict[pa]

sumDict = defaultdict(int)

for fr in elementDict.keys():
    sumDict[fr[0]] += elementDict[fr]
    sumDict[fr[1]] += elementDict[fr]

for fr in sumDict.keys():
    sumDict[fr] = int(sumDict[fr]/2)
sumDict[firstChar] += 1
sumDict[lastChar] += 1

print("Result")
print(max(sumDict.values())-min(sumDict.values()))