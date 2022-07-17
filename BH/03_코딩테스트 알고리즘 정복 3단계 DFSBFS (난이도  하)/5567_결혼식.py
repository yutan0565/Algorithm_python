import sys
from collections import deque

# 3 스탑

def bfs(graph,visited):
    q = deque()

    q.append(1)
    visited[1] = 1

    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[a] + 1

    count = 0
    for i in range(2, len(visited)):
        if visited[i] == 2 or visited[i] == 3:
            count += 1
    print(count)


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, visited)