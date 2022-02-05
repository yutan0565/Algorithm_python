import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().rstrip().split())
number_list = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0

# combination, permutations !!

for i in range(1, n+1):
    comb = combinations(number_list, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)