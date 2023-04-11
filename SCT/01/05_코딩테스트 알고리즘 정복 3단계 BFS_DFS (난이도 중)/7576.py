from collections import deque
import sys

def bfs():
    q = deque()
    for x,y in start:
        q.append([x,y])
        visited[x][y] = 0
    max_ = 0

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if  0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        graph[nx][ny] = 1
                        visited[nx][ny] = visited[a][b] + 1
                        max_ = max(max_, visited[nx][ny])
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1
    return max_


m,n= map(int , sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split()))  for _ in range(n) ]
visited = [[-1]*m  for _ in range(n) ]

start = []
for i in range(n):
    for j in range(m):
        if graph[i][j]== 1:
            start.append([i,j])

result = bfs()
print(result)
