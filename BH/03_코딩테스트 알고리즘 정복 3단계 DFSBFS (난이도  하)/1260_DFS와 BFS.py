import sys
from collections import deque

def dfs(graph, visited, v, n, m):
    visited[v] = True
    print(v, end = " ")
    for nv in graph[v]:
        if visited[nv] == False:
            dfs(graph, visited, nv, n, m)

def bfs(graph, visited, v, n, m):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        a = q.popleft()
        print(a, end=" ")
        for nv in graph[a]:
            if visited[nv] == False:
                q.append(nv)
                visited[nv] = True

n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

visited = [False] * (n+1)
dfs(graph, visited, v, n, m)
print()
visited = [False] * (n+1)
bfs(graph, visited, v, n, m)