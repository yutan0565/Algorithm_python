from collections import deque
import sys

def bfs():
    q = deque()
    q.append([hx-1,hy-1, 0])
    visited[hx-1][hy-1][0] = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b, magic = q.popleft()
        if a == ex-1 and b ==ey-1:
            return visited[a][b][magic]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    if visited[nx][ny][magic] == -1:
                        if magic == 0:
                            q.append([nx,ny,1])
                            visited[nx][ny][1] = visited[a][b][magic] + 1
                        elif magic == 1:
                            continue
                elif graph[nx][ny] == 0:
                    if visited[nx][ny][magic] == -1:
                        q.append([nx,ny,magic])
                        visited[nx][ny][magic] = visited[a][b][magic] +1
    return -1


n,m = map(int, sys.stdin.readline().rstrip().split())
hx,hy = map(int, sys.stdin.readline().rstrip().split())
ex,ey = map(int, sys.stdin.readline().rstrip().split())

graph = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[[-1,-1]  for _ in range(m)] for _ in range(n)]

result = bfs()
print(result)