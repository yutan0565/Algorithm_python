import sys
from collections import deque

def bfs(graph, visited, x, result):
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == False:
                q.append(nx)
                visited[nx] = True
                result[nx] = a
    for i in range(2, len(result)):
        print(result[i])

n = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

result = [0]* (n+1)

while True:
    try:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    except:
        break

bfs(graph, visited, 1, result)


