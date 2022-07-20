import sys
from collections import deque


def bfs(graph, visited, x):
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == False:
                q.append(nx)
                visited[nx] = True


n, m = map(int, sys.stdin.readline().rstrip().split())  # 노드  , 간선
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b =  map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

group_count = 0

for i in range(1, n+1):
    if visited[i] == False:
        bfs(graph, visited, i)
        group_count +=1
print(group_count)