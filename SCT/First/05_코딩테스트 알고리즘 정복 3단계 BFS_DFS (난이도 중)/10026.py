from collections import deque
import sys

def bfs(case, x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    if case == 1:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'G':
                    graph[i][j] = 'R'

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == graph[a][b]:
                        q.append([nx,ny])
                        visited[nx][ny] = 1

n = int(sys.stdin.readline().rstrip())
graph = [ list(sys.stdin.readline().rstrip()) for _ in range(n) ]

for case in range(2):
    visited = [[-1] * n for _ in range(n)]
    group = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                bfs(case, i,j)
                group += 1

    print(group, end = " ")