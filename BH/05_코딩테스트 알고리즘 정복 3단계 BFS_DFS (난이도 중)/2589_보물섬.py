import sys
from collections import deque

def bfs(graph,visited,n,m,x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 0

    global result

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in  range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 'L':
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = visited[a][b] + 1
                        result = max(visited[nx][ny], result)

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [ list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]

global result
result = -1

start_index = []
max_index = []


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            if 0<= i-1 and i+1 <n:
                if graph[i-1][j] == 'L' and graph[i+1][j] == 'L':
                    continue
            if 0<= j-1 and j+1 <m:
                if graph[i][j-1] == 'L' and graph[i][j+1] == 'L':
                    continue

            visited = [[-1] * m for _ in range(n)]
            bfs(graph,visited,n,m,i,j)

print(result)




