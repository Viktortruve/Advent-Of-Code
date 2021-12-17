import binascii
ls = open("inp.txt").read().splitlines()
hexDict1 = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
fullBinaryString = ""

for lines in ls:
    for words in lines:
        binary_string = hexDict1[words]
        fullBinaryString += (binary_string)

print(len(fullBinaryString))
def getVerSum(fullBinaryString,iterate,versionSum,numberOfPackets,lengthOfSubPackets):
    if (len(fullBinaryString) - iterate) < 11:
        return iterate,versionSum
    version = int(fullBinaryString[0+iterate:3+iterate], 2)
    ID = int(fullBinaryString[3+iterate:6+iterate], 2)
    print("ID",ID)
    print("version", version,)
    versionSum += version
    print("versionSum",versionSum)
    if ID == 4:
        while int(fullBinaryString[6 + iterate], 2) == 1:
            iterate += 5
        if int(fullBinaryString[6 + iterate], 2) == 0:
            iterate += 5
            iterate += 6

    else:
        LID = int(fullBinaryString[6+iterate], 2)
        if LID == 1:
            numberOfPackets = int(fullBinaryString[7 + iterate:18 + iterate], 2)
            iterate += 18
            for j in range(numberOfPackets):
                iterate, versionSum = getVerSum(fullBinaryString, iterate, versionSum, 0,
                                                0)
        else:
            b = " IF lid == 0"
            lengthOfSubPackets = int(fullBinaryString[7 + iterate:22 + iterate], 2)
            iterate += 22
            k = int(iterate)
            while iterate < k + lengthOfSubPackets:
                iterate,versionSum = getVerSum(fullBinaryString, iterate, versionSum, 0, 0)

    return iterate,versionSum

iterate,versionSum = getVerSum(fullBinaryString,0,0,0,0)
print(iterate,versionSum)
