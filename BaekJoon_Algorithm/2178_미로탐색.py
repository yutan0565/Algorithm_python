import sys
from collections import deque

N , M = map(int, sys.stdin.readline().rstrip().split())
graph = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(N) ]
visited = [ [False]*M for _ in range(N) ]



def bfs(x, y):
    global N, M, graph, visited
    q = deque()
    q.append([x,y])
    graph[x][y] = 2
    visited[x][y] = True

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    while q:
        a, b = q.popleft()
        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny >=0 and nx < N and ny < M:
                if visited[nx][ny] != True:
                    if graph[nx][ny] == 1:
                        q.append([nx, ny])
                        graph[nx][ny] = graph[a][b] + 1
                        visited[nx][ny] = True
    return graph[N-1][M-1]-1




for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            result = bfs(i, j)

print(result)