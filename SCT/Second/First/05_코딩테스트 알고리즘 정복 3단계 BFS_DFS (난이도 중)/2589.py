from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 0
    dx = [0, 0,1,-1]
    dy = [1,-1,0,0]
    count = 0
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 'L':
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = visited[a][b] + 1
                        count = max(count, visited[nx][ny])
    return count
n,m = map(int, sys.stdin.readline().rstrip().split())
graph = [ list(sys.stdin.readline().rstrip()) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':

            visited = [[-1] * m for _ in range(n)]
            temp = bfs(i,j)
            result = max(result, temp)

print(result)