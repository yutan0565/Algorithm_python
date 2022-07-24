import sys
from collections import deque

def bfs():
    global result
    q = deque()
    ori_graph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ori_graph[i][j] = graph[i][j]


    for x,y in start:
        q.append([x,y])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx < n and 0<=ny < m:
                if ori_graph[nx][ny] == 0:
                    ori_graph[nx][ny] = 2
                    q.append([nx, ny])
    count = 0
    for i in range(n):
        for j in range(m):
            if ori_graph[i][j] == 0:
                count += 1
    result = max(result, count)


n,m = map(int, sys.stdin.readline().rstrip().split())
graph = []
start = []
result = 0

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(m):
        if graph[i][j] == 2:
            start.append([i,j])

def wall(x):
    if x==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                wall(x+1)
                graph[i][j]=0

wall(0)
print(result)
