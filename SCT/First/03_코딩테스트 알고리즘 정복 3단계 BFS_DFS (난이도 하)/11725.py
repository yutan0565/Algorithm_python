from collections import deque
import sys

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = 1
                result[nx] = a



n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
result = [-1 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
for i in range(2, n+1):
    print(result[i])
