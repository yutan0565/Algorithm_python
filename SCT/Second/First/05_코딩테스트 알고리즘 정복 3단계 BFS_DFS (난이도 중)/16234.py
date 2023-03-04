from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    group = []
    group.append([x,y])

    sum_people = graph[x][y]
    peaple_count = 1

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if l<= abs(graph[a][b] - graph[nx][ny]) <=r:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        group.append([nx,ny])
                        peaple_count += 1
                        sum_people += graph[nx][ny]

    avg = sum_people//peaple_count
    if peaple_count > 1:
        for i,j in group:
            graph[i][j] = avg
    return peaple_count

n,l,r = map(int, sys.stdin.readline().rstrip().split())
graph = [ list(map(int ,sys.stdin.readline().rstrip().split())) for _ in range(n)]

result = 0

while 1:
    flag = 0
    visited = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                count = bfs(i,j)
                if count > 1:
                    flag = 1
    if flag == 1:
        result += 1
    else:
        break

print(result)
