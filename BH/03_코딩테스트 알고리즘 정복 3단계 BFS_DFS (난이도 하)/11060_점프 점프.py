import sys
from collections import deque


def bfs(graph,visited, n):
    q = deque()
    q.append([0, 0])
    visited[0] = True

    while q:
        a, count = q.popleft()

        for dx in range(0, graph[a]+1):
            nx = a + dx

            if nx >= n-1:
                return count+1

            if visited[nx] == False:
                q.append([nx, count+1])
                visited[nx] = True
    return -1

n = int(sys.stdin.readline().rstrip())
graph = list(map(int, sys.stdin.readline().rstrip().split()))
visited = [False]*n

if n == 1:
    print(0)
else:
    print(bfs(graph, visited, n))