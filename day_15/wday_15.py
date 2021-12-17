import re
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def neighbour(p,z,N):
    neigh = []
    indexes = []
    if p != N - 1:
        indexes.append((p+1,z))
    #if p != 0:
     #   indexes.append((p-1,z))
    if z != N - 1:
        indexes.append((p,z+1))
    #if z != 0:
     #   indexes.append((p,z-1))
    return indexes

ls = open("inp.txt").read().splitlines()
matSiz = np.size(ls)
matrix = np.zeros((matSiz,matSiz))
for i, lines in enumerate(ls):
    for j, number in enumerate(lines):
        matrix[i][j] = int(number)**2
pathDict = defaultdict(int)
finished = False
startIndex = (0,0)
endIndex = (matSiz-1,matSiz-1)
pathDict[(0,0)] = (0,[(0,0)])
costDict = defaultdict(int)
counter = 0
while True:
    counter += 1
    theChosenOne = min(pathDict, key=pathDict.get)
    cost,theChosenPath = pathDict[theChosenOne]
    #curNeigh = list(filter(lambda x:not x in theChosenPath,neighbour(theChosenOne[0],theChosenOne[1],matSiz)))
    curNeigh = neighbour(theChosenOne[0],theChosenOne[1],matSiz)
    if theChosenOne == endIndex:
        break
    curVal, curpath = pathDict.pop(theChosenOne)
    for i,j in curNeigh:
        h = 0
        if (i,j) in pathDict.keys():
            cost,path = pathDict[(i, j)]
            if cost > curVal+matrix[i][j]:
                pathDict[(i,j)] = (h+curVal+matrix[i][j],theChosenPath+[(i,j)])
        else:
            pathDict[(i, j)] = (h+curVal + matrix[i][j],theChosenPath+[(i,j)])
cost,pat = pathDict[endIndex]
cost = 0
matrix[0][0] = 0

for path in pat:
    cost += (matrix[path[0],path[1]])**(0.5)
print(cost-1)
print(counter)
print(pathDict[endIndex])