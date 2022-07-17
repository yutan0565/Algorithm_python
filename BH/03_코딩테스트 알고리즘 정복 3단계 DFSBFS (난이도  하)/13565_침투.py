import sys
from collections import deque


def bfs(graph, visited, m, n, x, y):
    q = deque()
    q.append([x,y])
    visited[x][y] = True

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        if a == m-1:
            return 1
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >=0 and ny >= 0 and nx < m and ny < n:
                if graph[nx][ny] == 0:
                    if visited[nx][ny] == False:
                        q.append([nx,ny])
                        visited[nx][ny] = True
    return 0

m, n  = map(int, sys.stdin.readline().rstrip().split())
graph = [ list(map(int, sys.stdin.readline().rstrip()))   for _ in range(m)  ]
visited = [ [False] * n for _ in range(m)]


flag = 0
for y in range(n):
    if visited[0][y] == False and graph[0][y] == 0:
        result = bfs(graph, visited, m, n, 0, y)

        if result == 1:
            flag = 1
            break
        elif result == 0:
            continue

if flag == 1:
    print("YES")
else:
    print("NO")



