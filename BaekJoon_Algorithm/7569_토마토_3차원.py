import sys
from collections import deque

def bfs(M,N, H, graph, visited,toto):

    count = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1 or graph[i][j][k] == -1:
                    count += 1
    if count == M*N*H:
        return 0

    q = deque()
    for to in toto:
        q.append(to)
        x, y, z = map(int, to)
        visited[x][y][z] = True
        graph[x][y][z] = 2

    dx = [1,0,0,-1,0,0 ]
    dy = [0,1,0,0,-1,0 ]
    dz = [0,0,1,0,0,-1]

    while q:
        a, b, c = q.popleft()
        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]
            if nx >=0 and ny >= 0 and nz >= 0 and nx < H and ny < N and nz < M:
                if graph[nx][ny][nz] == 0:
                    if visited[nx][ny][nz] != True:
                        q.append([nx,ny,nz])
                        visited[nx][ny][nz] = True
                        graph[nx][ny][nz] = graph[a][b][c] +1

    max = -1e10
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if max < graph[i][j][k]:
                    max = graph[i][j][k]
                if graph[i][j][k] == 0:
                    return -1

    return max - 2


M,N, H = map(int, sys.stdin.readline().rstrip().split())
graph = [[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N) ] for _ in range(H)]
visited = [[ [False]* M for _ in range(N) ] for _ in range(H)]

toto = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] ==1:
                toto.append([i,j,k])

day = bfs(M,N, H, graph, visited,toto)

print(day)






