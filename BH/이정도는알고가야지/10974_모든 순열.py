import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
g_list = permutations(range(1,n+1),3)
for g in g_list:
    print(g)