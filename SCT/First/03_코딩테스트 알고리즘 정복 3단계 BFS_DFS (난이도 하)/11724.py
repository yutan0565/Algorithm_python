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

n, m = map(int ,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for start in range(1, n+1):
    if visited[start] == -1:
        bfs(start)
        result += 1
print(result)