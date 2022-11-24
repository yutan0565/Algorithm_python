from collections import deque
import sys

def bfs(x, y):
    q = deque()
    q.append(x)
    visited[x] = 0

    while q:
        a = q.popleft()
        if a == y:
            return visited[a]
        for j in range(1, graph[a]+1):
            nx = a + j
            if nx <= y:
                if visited[nx] == -1:
                    visited[nx] = visited[a] + 1
                    q.append(nx)
    return -1


n = int(sys.stdin.readline().rstrip())
graph = list(map(int, sys.stdin.readline().rstrip().split()))
visited = [-1 for _ in range(n)]

result = bfs(0, n-1)
print(result)