from collections import deque
import sys

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0

    while q:
        a = q.popleft()
        if a == e_p:
            return visited[a]
        for nx in graph[a]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[a] + 1
    return -1

n = int(sys.stdin.readline().rstrip())
s_p, e_p = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

result = bfs(s_p)

print(result)