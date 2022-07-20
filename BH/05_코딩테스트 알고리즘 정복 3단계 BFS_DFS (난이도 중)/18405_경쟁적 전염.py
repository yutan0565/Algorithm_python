import sys
from collections import deque

def bfs(graph, start, s, k, n):
    q = deque()
    count = 0
    for st in start:
        q.append(st)

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        if count == s:
            break
        for _ in range(len(q)):
            v_number, a, b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = v_number
                        q.append([graph[a][b], nx, ny])
        count += 1
    return graph

n,k = map(int, sys.stdin.readline().rstrip().split())

graph = []
start = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j] != 0:
            start.append([graph[i][j],i,j ])

s,end_x,end_y = map(int, sys.stdin.readline().rstrip().split())

start.sort()
result = bfs(graph, start, s, k, n)
print(result[end_x-1][end_y-1])




