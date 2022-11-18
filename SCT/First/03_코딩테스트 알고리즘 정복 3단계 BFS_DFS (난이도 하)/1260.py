from collections import deque
import sys

def dfs(x):
    print(x, end = " ")
    visited[x] = 1
    for nx in graph[x]:
        if visited[nx] == -1:
            dfs(nx)


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        a = q.popleft()
        print(a, end = " ")
        for nx in graph[a]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = 1

n,m ,v = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

dfs(v)
print()
visited = [-1 for _ in range(n+1)]
bfs(v)