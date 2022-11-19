from collections import deque
import sys

def bfs(x, y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = 1
                        q.append([nx,ny])

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        b,a = map(int, sys.stdin.readline().rstrip().split())
        graph[a][b] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                if visited[i][j] == -1:
                   bfs(i,j)
                   result+=1
    print(result)