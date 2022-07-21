import sys
from collections import deque

def dfs(x):
    graph[x] = -2
    for nx in range(n):
        if x == graph[nx]:
            dfs(nx)

n = int(sys.stdin.readline().rstrip())

graph = list(map(int, sys.stdin.readline().rstrip().split()))

del_node = int(sys.stdin.readline().rstrip())
result = 0

dfs(del_node)
for i in range(n):
    if graph[i] != -2:
        if i not in graph:
            result += 1
print(result)