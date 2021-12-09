import numpy as np
crabList = []
ls = open("inp.txt").read().split(",")
for crab in ls:
    crabList.append(int(crab))
crabList = np.array(crabList)

med = int((np.mean(crabList))+0.5)
print(med)
minSum = 1000000000000
for j in range(np.max(crabList)):
    tmpCrabList = crabList.copy()
    med = j
    tmpCrabList = np.abs(tmpCrabList - med)
    for i , crab in enumerate(tmpCrabList):
        tmpCrabList[i] = (crab*(crab+1)/2)
    if (np.sum(tmpCrabList)) <= minSum:
        minSum = (np.sum(tmpCrabList))
        minMed = j
print(minSum)
print(minMed)
