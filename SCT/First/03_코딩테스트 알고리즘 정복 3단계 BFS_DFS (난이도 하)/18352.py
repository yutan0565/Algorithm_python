from collections import deque
import sys

def bfs():
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        a = q.popleft()
        if visited[a] == k:
            result.append(a)
        for nx in graph[a]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[a] + 1


n,m,k,x = map(int ,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
result = []

for _ in range(m):
    a,b = map(int ,sys.stdin.readline().rstrip().split())
    graph[a].append(b)

bfs()
result.sort()

if len(result) == 0:
    print(-1)
else:
    for r in result:
        print(r)
