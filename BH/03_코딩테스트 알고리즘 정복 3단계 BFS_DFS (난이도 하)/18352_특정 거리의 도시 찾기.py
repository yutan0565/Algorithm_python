import sys
from collections import deque

def bfs(graph, visited, k, x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[a] + 1

    temp = []
    for i in range(1, len(visited)):
        if visited[i] == (k+1):
            temp.append(i)
    if len(temp) == 0:
        print(-1)
    else:
        temp.sort()
        for node in temp:
            print(node)

n,m,k,x = map(int, sys.stdin.readline().strip().split())

graph = [ [] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)

bfs(graph, visited, k, x)