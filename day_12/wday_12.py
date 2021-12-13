import itertools
from collections import defaultdict
from collections import Counter
import numpy as np

ls = open("inp.txt").read().splitlines()

graph = defaultdict(set)

for line in ls:
    p1,p2 = line.split("-")
    graph[p1].add(p2)
    graph[p2].add(p1)

print(graph)
def valid(path):
    smallCaveCounter = 0
    c = Counter(filter(lambda x:x.islower(),path))
    if c['start']>1:
        return False
    if c['end']>1:
        return False
    for x in c.values():
        if x > 1:
            smallCaveCounter += 1
        if x > 2:
            return False
    if smallCaveCounter > 1:
        return False
    return True
def bfs(path):
    if 'end' in path:
        return [path]
    if not valid(path):
        return []
    paths = [*map(lambda n:bfs(path+[n]),graph[path[-1]])]
    ps = []
    for p in paths:
        ps = ps+p
    return ps
ps = bfs(['start'])
print(len(ps))