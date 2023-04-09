from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        a,b = q.popleft()
        if a == m-1:
            return 1
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny] == 0:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = 0
    return 0
m,n = map(int, sys.stdin.readline().rstrip().split())
graph = [ list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(m)]
visited = [ [-1]*n for _ in range(m)]

result = 0
for i in range(n):
    if graph[0][i] == 0:
        if visited[0][i] == -1:
            result = bfs(0,i)
            if result ==1:
                break

if result == 0:
    print("NO")
else:
    print("YES")