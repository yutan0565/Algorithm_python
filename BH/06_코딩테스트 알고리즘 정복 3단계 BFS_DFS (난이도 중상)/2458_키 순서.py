import sys
import copy
from collections import deque

def bfs(start,graph, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    temp_count = 0
    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == False:
                q.append(nx)
                visited[nx] = True
                temp_count += 1
    return temp_count



n,m = map(int, sys.stdin.readline().rstrip().split())

graph_up = [[] for _ in range(n+1)]
graph_down = [[] for _ in range(n+1)]


for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph_up[a].append(b)
    graph_down[b].append(a)

count = 0
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    c_up = bfs(i,graph_up, visited)
    visited = [False for _ in range(n+1)]
    c_down = bfs(i, graph_down, visited)
    if c_up + c_down == n-1:
        count += 1

print(count)