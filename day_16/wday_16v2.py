import binascii
ls = open("inp.txt").read().splitlines()
hexDict1 = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
fullBinaryString = ""

for lines in ls:
    for words in lines:
        binary_string = hexDict1[words]
        fullBinaryString += (binary_string)

def idfunc(id,decList):
    if id == 0:
        ans = sum(decList)
    elif id == 1:
        if len(decList)==1:
            ans = decList[0]
        else:
            ans = 1
            for k in decList:
                ans *= k
    elif id == 2:
        ans = min(decList)
    elif id == 3:
        ans = max(decList)
    elif id == 5:
        if decList[0]>decList[1]:
            ans = 1
        else:
            ans = 0
    elif id == 6:
        if decList[0]<decList[1]:
            ans = 1
        else:
            ans = 0
    else:
        if decList[0]==decList[1]:
            ans = 1
        else:
            ans = 0
    return ans

def getVerSum(fullBinaryString,iterate,versionSum,numberOfPackets,lengthOfSubPackets):
    version = int(fullBinaryString[0+iterate:3+iterate], 2)
    ID = int(fullBinaryString[3+iterate:6+iterate], 2)
    versionSum += version
    binString = ""
    if ID == 4:
        while int(fullBinaryString[6 + iterate], 2) == 1:
            binString += fullBinaryString[7 + iterate:11+iterate]
            iterate += 5

        if int(fullBinaryString[6 + iterate], 2) == 0:
            binString += fullBinaryString[7 + iterate:11+iterate]
            iterate += 5
            iterate += 6
            decNum = int(binString,2)
    else:
        LID = int(fullBinaryString[6+iterate], 2)
        decList = []
        if LID == 1:
            numberOfPackets = int(fullBinaryString[7 + iterate:18 + iterate], 2)
            iterate += 18
            for j in range(numberOfPackets):
                iterate, versionSum,decNum = getVerSum(fullBinaryString, iterate, versionSum, 0,
                                                0)
                decList.append(decNum)

            decNum = idfunc(ID, decList)
        else:
            b = " IF lid == 0"
            lengthOfSubPackets = int(fullBinaryString[7 + iterate:22 + iterate], 2)
            iterate += 22
            k = int(iterate)
            while iterate < k + lengthOfSubPackets:
                iterate,versionSum,decNum = getVerSum(fullBinaryString, iterate, versionSum, 0, 0)
                decList.append(decNum)

            decNum = idfunc(ID,decList)

    return iterate,versionSum,decNum

iterate,versionSum,decNum = getVerSum(fullBinaryString,0,0,0,0)
print(decNum)
