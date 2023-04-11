from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 0
    b_count = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny] == 1:
                    if visited[nx][ny] == -1:
                        b_count += 1
                        visited[nx][ny] = 0
                        q.append([nx,ny])
    return b_count


m,n,k = map(int ,sys.stdin.readline().rstrip().split())
graph = [[1]*n for _ in range(m)]
visited = [[-1]*n for _ in range(m)]

for _ in range(k):
    x,y,e_x, e_y = map(int ,sys.stdin.readline().rstrip().split())
    for i in range(y, e_y):
        for j in range(x, e_x):
            graph[i][j] = 0

result = []
count = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            if visited[i][j] == -1:
                result.append(bfs(i,j))
                count += 1
result.sort()

print(count)
for r in result:
    print(r, end=" ")