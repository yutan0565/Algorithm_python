import sys
from itertools import combinations

# 체력 100


happy = 0

n = int(sys.stdin.readline().rstrip())
loss = list(map(int, sys.stdin.readline().rstrip().split()))
plus = list(map(int, sys.stdin.readline().rstrip().split()))


for i in range(1, n + 1):
    combi = combinations(range(n), i)
    for group in combi:
        new_loss = [loss[j] for j in range(n) if j in group]
        new_plus = [plus[j] for j in range(n) if j in group]
        if 100 - sum(new_loss) > 0:
            happy = max(happy, sum(new_plus))

print(happy)