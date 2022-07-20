import sys
from collections import deque

def bfs(graph, visited, start, end):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        a = q.popleft()
        if a == end:
            return visited[a]
        for nx in graph[a]:
            if visited[nx] == 0:
                visited[nx] = visited[a] + 1
                q.append(nx)

    return 0



n = int(sys.stdin.readline().rstrip())
start, end = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


print(bfs(graph, visited, start, end)-1)