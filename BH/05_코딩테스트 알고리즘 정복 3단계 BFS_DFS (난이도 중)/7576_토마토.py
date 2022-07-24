import sys
from collections import deque

def bfs():
    global graph, start, flag
    q = deque()
    for x,y in start:
        q.append([x,y])
        graph[x][y] = 2
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    q.append([nx,ny])
                    graph[nx][ny] = graph[a][b] + 1
    max_day = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1
            max_day = max(max_day, graph[i][j])
    return max_day - 2


m,n = map(int, sys.stdin.readline().rstrip().split())
graph = []
start = []
flag = True

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(m):
        if graph[i][j] == 1:
            start.append([i,j])


result = bfs()
print(result)