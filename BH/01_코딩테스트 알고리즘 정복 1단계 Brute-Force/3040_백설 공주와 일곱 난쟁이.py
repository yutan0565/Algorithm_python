import sys
from itertools import combinations

temp = []
for _ in range(9):
    temp.append(int(sys.stdin.readline().rstrip()))

combi = combinations(range(9), 7)

for com in combi:
    group = [ temp[i] for i in range(len(temp)) if i in com ]

    if sum(group) == 100:
        for g in group:
            print(g)
        break
