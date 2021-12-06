import numpy as np
def day5(diagonals):
    n = 1000
    matrix = np.zeros((n,n))
    ls = open("inp.txt").read().splitlines()
    print(ls)
    for lines in ls:
        p1,p2 = lines.split("->",1)
        x1,y1 = p1.split(",")
        x2,y2 = p2.split(",")

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        xminind = min(x1,x2)
        xmaxind = max(x1,x2)
        yminind = min(y1,y2)
        ymaxind = max(y1,y2)
        if xminind == xmaxind:
            matrix[yminind:ymaxind+1,xminind] +=1
        elif ymaxind == yminind:
            matrix[yminind,xminind:xmaxind+1] +=1
        elif diagonals:
            xvals = np.linspace(x1,x2,xmaxind-xminind+1,dtype=int)
            yvals = np.linspace(y1,y2,xmaxind-xminind+1,dtype=int)

            for steps in range((xmaxind-xminind)+1):

                matrix[yvals[steps]][xvals[steps]] +=1
        #print(len(t))
    return matrix
matrix1 = day5(False)
matrix2 = day5(True)
ans1 = len(np.argwhere(matrix1>=2))
ans2 = len(np.argwhere(matrix2>=2))
print("1st answer = ",ans1)
print("2nd answer = ",ans2)
