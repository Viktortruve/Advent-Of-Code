import numpy as np
from collections import defaultdict
xRange = np.arange(287,310)
yRange = np.arange(-76,-47)

print(xRange)
print(yRange)
ySet = defaultdict(set)
xSet = defaultdict(set)
ySet = set()
for y in range(-77,76):
    print(y)
    for x in range(0,311):
        yPos = 0
        yVel = y
        xPos = 0
        xVel = x
        while True:
            yPos += yVel
            yVel -= 1
            xPos += xVel
            xVel -= 1
            if xVel < 0:
                xVel = 0
            if yPos in yRange:
                if xPos in xRange:
                    ySet.add((x,y))
            if yPos < min(yRange):
                break
print(len(ySet))
yPos = 0
yVel = 75
distinct = 0





