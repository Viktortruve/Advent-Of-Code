import re
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
ls = open("inp.txt").read().splitlines()
dots = []
folds = defaultdict(list)
yVals = []
xVals = []
for line in ls:
    regex2 = r"=\d"
    match2 = re.search(regex2, line)
    print(match2)
    if match2:
        z1,z2 = line.split("=")
        if z1[-1]=='x':
            folds['x'].append(z2)
            folds['order'].append('x')
        else:
            folds['y'].append(z2)
            folds['order'].append('y')
    elif len(line.strip())!=0:
        p1,p2 = line.split(",")
        xVals.append(int(p1))
        yVals.append(int(p2))
        dots.append((int(p1),int(p2)))
folds['x'].reverse()
folds['y'].reverse()
paper = np.zeros((max(yVals)+1,(max(xVals))+1))
for x,y in dots:
    paper[y][x] = 1
def folding(axis,val,matrix):
    paper = matrix.copy()
    if axis == 'x':
        paper[0:, val+1:] = np.fliplr(paper[0:, val+1:])
        paper = paper[0:, 0:val] + paper[0:, val+1:]
    else:
        paper[val+1:,0:] = np.flipud(paper[val+1:,0:])
        paper = paper[0:val, 0:] + paper[val+1:,0:]
    newPap = np.where(paper != 0, 1, 0)
    return newPap

for fold in folds['order']:
    value = folds[fold].pop()
    ax = fold
    paper = folding(ax,int(value),paper)
paper = np.flipud(paper[0:,0:])
axp = plt.pcolor(paper,cmap="binary")
plt.axis('auto')
plt.show()