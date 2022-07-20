import sys
from collections import deque

def bfs(graph, visited, x):
    q = deque()
    q.append(x)

    count = 1
    visited[x] = count

    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == 0:
                q.append(nx)
                count += 1
                visited[nx] = count
    return max(visited) - 1


n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

graph = [ [] for _ in range(n+1) ]
visited = [0] * (n+1)

for _ in range(k):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

start = 1
result = bfs(graph, visited, start)
print(result)