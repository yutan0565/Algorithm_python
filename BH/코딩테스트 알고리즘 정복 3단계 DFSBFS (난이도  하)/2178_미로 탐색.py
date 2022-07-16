import sys
from collections import deque

def bfs(x, y,graph, visited, n, m):
    q = deque()
    q.append([x,y])
    graph[x][y] = 2

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[a][b] + 1
                    q.append([nx,ny])

    return graph[n-1][m-1] - 1


n,m = map(int, sys.stdin.readline().rstrip().split())

graph = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [ [False]*m for _ in range(n)]

print(bfs(0,0, graph, visited, n, m))
