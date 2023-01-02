from collections import deque
import sys

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    count = 0
    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = 1
                count += 1
    return count

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    a,b = map(int ,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

result = bfs(1)
print(result)