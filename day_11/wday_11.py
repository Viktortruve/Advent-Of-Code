import numpy as np
def q1(steps):
    matrix = np.zeros((10,10))
    for i, lines in enumerate(open("inp.txt").read().splitlines()):
        for j, num in enumerate(lines):
            matrix[i][j] = int(num)
    totalFlashes = 0
    for t in range(steps):
        matrix += 1
        initialFlashes = np.argwhere(matrix >= 10)
        flashedList = initialFlashes.copy()
        newFlashes = initialFlashes.copy()
        while len(newFlashes)!=0:
            for i,j in newFlashes:
                for k,z in neighbours(i,j):
                        matrix[k][z] += 1
            allFlashes = np.argwhere(matrix >= 10)
            newFlashes = []
            alltup = []
            tmptup = []
            for flash in allFlashes:
                alltup.append((flash[0],flash[1]))
            for fl in flashedList:
                tmptup.append((fl[0],fl[1]))
            for tup1 in alltup:
                if tup1 not in tmptup:
                    newFlashes.append(tup1)
            flashedList = allFlashes.copy()
            if len(allFlashes)==100:
                print(t)
                break
        matrix = np.where(matrix>=10,0,matrix)
        totalFlashes += len(flashedList)
    return totalFlashes
def neighbours(i,j):
    neighIndex = []
    for k in range(i-1,i+2):
        for z in range(j-1,j+2):
            if k in range(0,10) and z in range(0,10):
                neighIndex.append((k,z))
    return neighIndex
print(q1(1000))