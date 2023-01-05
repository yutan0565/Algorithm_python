from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = visited[a][b] + 1




n,m = map(int, sys.stdin.readline().rstrip().split())
graph = [ list(map(int, list(sys.stdin.readline().rstrip())))    for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

result = bfs(0,0)
print(result)