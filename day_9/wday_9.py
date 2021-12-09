import numpy as np

matrix = np.zeros((100,100))
N = 100
ls = open("inp.txt").read().splitlines()
ansList = []
totSum = 0

def neighbour(i,j,N):
    neigh = []
    indexes = []
    if i != N - 1:
        neigh.append(matrix[min(i + 1, N - 1)][j])
        indexes.append((min(i + 1, N - 1),j))
    if i != 0:
        neigh.append(matrix[max(i - 1, 0)][j])
        indexes.append((i-1,j))
    if j != N - 1:
        neigh.append(matrix[i][min(j + 1, N - 1)])
        indexes.append((i,j+1))

    if j != 0:
        neigh.append(matrix[i][max(j - 1, 0)])
        indexes.append((i,j-1))
    indexes.append((i,j))
    return neigh, indexes

for i, lines in enumerate (ls):
    for j, ele in enumerate(lines):
        matrix[i][j] = int(ele)
for i in range(100):
    for j in range(100):

        neigh,indexes = neighbour(i,j,N)
        neigh.append(matrix[i][j])
        matVal = matrix[i][j]
        minVal = np.min(neigh)
        if len((np.argwhere(neigh == minVal))) == 1:
            if minVal == matrix[i][j]:
                totSum += matrix[i][j] + 1
                ansList.append((i, j))
basinSizes = []
for i,j in ansList:
    print(i,j)
    tmpMatrix = np.zeros((100, 100))
    tmpIndexes = []
    tmpMatrix[i][j] = 2
    while sum(sum(tmpMatrix==2))>0:
        print(np.where(tmpMatrix == 2)[0])
        for q, t in zip(np.where(tmpMatrix == 2)[0], np.where(tmpMatrix == 2)[1]):  # loop over expanding nodes
            newNeigh, indexes = neighbour(q, t, N)
            for z,y in indexes:
                if matrix[z][y] != 9:
                    tmpMatrix[z][y] = 2
            tmpMatrix[q,t] = 1
    basinSizes.append(np.sum(tmpMatrix))

print(np.max(basinSizes))
print(ansList)
print(totSum)