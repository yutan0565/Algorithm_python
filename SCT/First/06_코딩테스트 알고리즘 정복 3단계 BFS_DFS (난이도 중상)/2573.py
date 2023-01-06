from collections import deque
import sys

""""""

def bfs_check(x,y):
    q.append([x,y])
    visited[x][y] = 1

    graph_temp = []+graph

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] != 0:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                    elif graph[nx][ny] == 0:
                        graph_temp[a][b] = max(0,graph_temp[a][b] -1)
    return graph_temp


n,m = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

result = 0
q = deque()

while 1:
    group = 0
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                if visited[i][j] == -1:
                    graph = bfs_check(i,j)
                    group += 1
            else:
                flag = 1
    if group >= 2 :
        break
    if group == 0 or flag == 0:
        result = 0
        break


    result += 1
print(result)