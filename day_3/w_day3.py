import numpy as np
sumList = np.zeros(12)
with open('inp.txt', 'r') as file:
    # reading each line
    counter = 0
    for line in file:
        # reading each word
        for word in line.split():
            counter += 1
            for i, numbers in enumerate(word):
                sumList[i] += int(numbers)
    bin = np.where(sumList>=counter/2,1,0)
    binT = (bin-1)*-1
    binSum = 0
    binTSum = 0
    for j in range(len(bin)):
        binSum += bin[j]*2**(11-j)
        binTSum += binT[j]*2**(11-j)
    print(binSum*binTSum)
    file.close()
##Task 2
binList = []
with open('inp.txt', 'r') as file:
    # reading each line
    for line in file:
        # reading each word
        for word in line.split():
            counter += 1
            sumList = np.zeros(12)
            for i, numbers in enumerate(word):
                sumList[i] += int(numbers)
            binList.append(sumList)
    file.close()
savedList = binList.copy()
k = 0
sumList = np.zeros(12)
for z in range(12):
    tmpBinList = []
    for i in range(len(binList)):
        sumList[k] += binList[i][k]
    if sumList[k] >= len(binList)/2:
        number = 1
    else:
        number = 0
    for i in range(len(binList)):
        if binList[i][k]==number:
            tmpBinList.append(binList[i])
    binList = tmpBinList.copy()
    k+=1
oxygen = binList.copy()
print(binList)
k = 0
binList = savedList.copy()
sumList = np.zeros(12)
for co2 in range(9):
    tmpBinList = []
    for i in range(len(binList)):
        sumList[k] += binList[i][k]
    if sumList[k] >= len(binList)/2:
        number = 0
    else:
        number = 1
    for i in range(len(binList)):
        if binList[i][k]==number:
            tmpBinList.append(binList[i])
    binList = tmpBinList.copy()
    k+=1
co2 = binList.copy()
print(co2[0][1])
binSum = 0
binTSum = 0
for ok in range(12):
    binSum += oxygen[0][ok] * 2 ** (11 - ok)
    binTSum += co2[0][ok] * 2 ** (11 - ok)
print(binSum * binTSum)
