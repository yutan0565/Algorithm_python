import sys
from collections import deque


def bfs(graph, visited,start,n,m,h):
    q = deque()
    for x,y,z  in start:
        q.append([x,y,z])
        graph[x][y][z] = 2
    dx = [0,0,0,0,1,-1]
    dy = [0,0,1,-1,0,0]
    dz = [1,-1,0,0,0,0]

    while q:
        a,b,c = q.popleft()
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if 0<= nx<h and 0<=ny<n and 0<=nz<m:
                if graph[nx][ny][nz] != -1:
                    if graph[nx][ny][nz] == 0:
                        q.append([nx,ny,nz])
                        graph[nx][ny][nz] = graph[a][b][c] + 1


# 가로, 세로, 기핑
m,n,h = map(int, sys.stdin.readline().rstrip().split())

graph = [ [ list(map(int,sys.stdin.readline().rstrip().split()))  for _ in range(n)] for _ in range(h)]

start = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                start.append([i,j,k])


bfs(graph,start,n,m,h)

flag = False
temp_max = -2e10

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                flag = True
            temp_max = max(temp_max,graph[i][j][k] )

if flag == True:
    print(-1)
else:
    print(temp_max-2)
