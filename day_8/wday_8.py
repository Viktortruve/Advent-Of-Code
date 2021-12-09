import numpy as np
import time
print(time.perf_counter())
t1 = time.perf_counter()

outPutList = []
ls = open("inp.txt").read().splitlines()
digitSum = 0
codeList = []

totSum = 0
for i, line in enumerate(ls):
    p1,p2 = line.split("|")
    code = p1.split(" ")
    values = p2.split(" ")

    outPutList.append(values)

    digList = []
    for j in range(0,10):
        if len(code[j])==2:
            one = sorted(code[j])
        elif len(code[j]) == 4:
            four = sorted(code[j])
        elif len(code[j]) == 3:
            seven = sorted(code[j])
        elif len(code[j]) == 7:
            eight = sorted(code[j])


    for j in range(0,10):
        tmpSum = 0
        if len(code[j]) == 5:
            for y in range(len(seven)):
                if seven[y] in sorted(code[j]):
                    tmpSum+=1
            if tmpSum == 3:
                three = sorted(code[j])
                tw = False
            else:
                tmpSum = 0
                tw = True

            for y in range(len(four)):
                if four[y] in sorted(code[j]):
                    tmpSum += 1
            if tmpSum == 3:
                five = sorted(code[j])
            elif tw:
                two = sorted(code[j])
        elif len(code[j]) == 6:
            tmpSum = 0
            for y in range(len(four)):
                if four[y] in sorted(code[j]):
                    tmpSum+=1
            if tmpSum == 4:
                nine = sorted(code[j])
                si = False
            else:
                tmpSum = 0
                si = True

            for y in range(len(one)):
                if one[y] in sorted(code[j]):
                    tmpSum += 1
            if tmpSum == 2:
                zero = sorted(code[j])
            elif si:
                six = sorted(code[j])
    fourNum = []

    for z in range(1,5):
        if sorted(outPutList[i][z]) == zero:
            fourNum.append(0)
        if sorted(outPutList[i][z]) == one:
            fourNum.append(1)
        if sorted(outPutList[i][z]) == two:
            fourNum.append(2)
        if sorted(outPutList[i][z]) == three:
            fourNum.append(3)
        if sorted(outPutList[i][z]) == four:
            fourNum.append(4)
        if sorted(outPutList[i][z]) == five:
            fourNum.append(5)
        if sorted(outPutList[i][z]) == six:
            fourNum.append(6)
        if sorted(outPutList[i][z]) == seven:
            fourNum.append(7)
        if sorted(outPutList[i][z]) == eight:
            fourNum.append(8)
        if sorted(outPutList[i][z]) == nine:
            fourNum.append(9)
    q = ""

    for p in range(4):
        q += str(fourNum[p])
    totSum += int(q)
            #print(digList)
        #print(number)
t2 = time.perf_counter()
print(t2-t1)
print(totSum)
