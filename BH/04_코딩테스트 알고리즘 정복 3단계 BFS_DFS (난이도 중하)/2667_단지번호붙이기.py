import sys
from collections import deque

def bfs(graph, visited, x , y, n):
    q = deque()
    q.append([x,y])
    count = 1
    visited[x][y] = True
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 1:
                    if visited[nx][ny] == False:
                        q.append([nx,ny])
                        visited[nx][ny] = True
                        count += 1
    return count

n = int(sys.stdin.readline().rstrip())

graph = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)  ]
visited = [[False]*n for _ in range(n)]

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False :
            temp = bfs(graph, visited, i , j, n)
            result.append(temp)
result.sort()
print(len(result))
for r in result:
    print(r)
