import sys
from collections import deque

# l 이상, r 이하면은 평균 만들기

def bfs(n, x , y,l,r):
    q = deque()
    global flag
    q.append([x,y])

    sum_po = graph[x][y]
    count = 1
    group = []
    group.append([x,y])

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
                    if l<=abs(graph[a][b] - graph[nx][ny])<=r:
                        q.append([nx,ny])
                        visited[nx][ny] = True
                        count += 1
                        sum_po += graph[nx][ny]
                        group.append([nx,ny])
    avg = sum_po//count

    if count > 1 :
        flag = True
        for i,j in group:
            graph[i][j] = avg


n,l,r = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]


result = 0
while True:
    visited = [ [False] * n for _ in range(n) ]
    flag = False

    temp_count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs( n, i , j,l,r)

    if flag == True:
        result += 1
    else:
        break
print(result)
