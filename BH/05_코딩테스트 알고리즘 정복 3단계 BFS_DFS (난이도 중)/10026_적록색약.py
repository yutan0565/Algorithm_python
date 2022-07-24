import sys
from collections import deque

def bfs(graph,visited, n, x, y):
    q = deque()
    q.append([x,y])

    visited[x][y] = True
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == False:
                    if graph[a][b] == graph[nx][ny]:
                        q.append([nx,ny])
                        visited[nx][ny] = True


n = int(sys.stdin.readline().rstrip())

graph = [ list(map(str, sys.stdin.readline().rstrip())) for _ in range(n) ]
visited = [ [False]*n for _ in range(n) ]


count = 0
count_no = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(graph,visited, n, i, j)
            count+=1
        # if visited_no[i][j] == False:
        #     bfs(graph_no, visited_no, n, i, j)
        #     count_no+=1

visited = [ [False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' or graph[i][j] == 'G':
            graph[i][j] = 'S'

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(graph,visited, n, i, j)
            count_no+=1
        # if visited_no[i][j] == False:
        #     bfs(graph_no, visited_no, n, i, j)
        #     count_no+=1

print(count,count_no)