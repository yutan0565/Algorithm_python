from collections import deque
import sys

def bfs(graph, x):
    q = deque()
    q.append(x)
    visited[x] = 1
    count = 0

    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = 1
                count += 1
    return count


n,m = map(int, sys.stdin.readline().rstrip().split())
graph_up = [[] for _ in range(n+1)]
graph_down = [[] for _ in range(n+1)]

result = 0

for _  in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph_up[a].append(b)
    graph_down[b].append(a)

for i in range(1, n+1):
    visited = [-1 for _ in range(n + 1)]
    result_up = bfs(graph_up, i)
    visited = [-1 for _ in range(n + 1)]
    result_down = bfs(graph_down, i)
    if result_up + result_down == n-1:
        result += 1
print(result)