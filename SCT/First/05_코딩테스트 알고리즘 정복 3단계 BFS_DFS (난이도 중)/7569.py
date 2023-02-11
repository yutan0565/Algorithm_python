from collections import deque
import sys

def bfs():
    q = deque()
    for x,y,z in start:
        q.append([x,y,z])
        visited[x][y][z] = 0
    max_ = 0

    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    while q:
        for _ in range(len(q)):
            a,b,c = q.popleft()
            for i in range(6):
                nx = a + dx[i]
                ny = b + dy[i]
                nz = c + dz[i]
                if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                    if graph[nx][ny][nz] == 0:
                        if visited[nx][ny][nz] == -1:
                            q.append([nx,ny,nz])
                            graph[nx][ny][nz] = 1
                            visited[nx][ny][nz] = visited[a][b][c] + 1
                            max_ = max(max_, visited[nx][ny][nz])

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return -1
    return max_


m,n,h = map(int , sys.stdin.readline().rstrip().split())

graph = [ [list(map(int, sys.stdin.readline().rstrip().split()))  for _ in range(n) ] for _ in range(h) ]
visited = [ [[-1 for _ in range(m)]  for _ in range(n) ] for _ in range(h) ]
start = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                start.append([i,j,k])

result = bfs()
print(result)
