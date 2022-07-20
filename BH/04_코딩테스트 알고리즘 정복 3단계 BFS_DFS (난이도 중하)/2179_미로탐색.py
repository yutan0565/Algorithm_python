import sys
from collections import deque

def bfs(graph, visited, n,m,x,y):
    q = deque()
    q.append([x,y])
    graph[x][y] = 2
    visited[x][y] = True
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        if a == n-1 and b == m-1:
            return graph[a][b] - 1

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    if visited[nx][ny] == False:
                        q.append([nx,ny])
                        visited[nx][ny] = True
                        graph[nx][ny] = graph[a][b] + 1



n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(n) ]
visited = [ [False]*m for _ in range(n)  ]

result = bfs(graph, visited, n,m,0,0)
print(result)