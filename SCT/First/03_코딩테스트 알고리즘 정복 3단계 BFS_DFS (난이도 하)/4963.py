from collections import deque
import sys

def bfs(x, y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    dx = [0, 0 , 1, -1, 1 , 1, -1 ,-1]
    dy = [1, -1, 0, 0 , 1 , -1 ,1 , -1]

    while q:
        a, b = q.popleft()
        for  i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] == 1:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = 1



while 1:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(h)]
    visited = [[-1 for _ in range(w)] for _ in range(h)]

    count_result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                if visited[i][j] == -1:
                    bfs(i, j)
                    count_result += 1
    print(count_result)

