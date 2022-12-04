from collections import deque
import sys

def bfs():
    q = deque()
    flag = 0
    q.append([0,0, flag])
    visited[0][0][flag] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while q:
        a,b, sw = q.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b][sw]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if sw == 0:
                    if graph[nx][ny] == 0:
                        if visited[nx][ny][sw] == -1:
                            q.append([nx,ny,0])
                            visited[nx][ny][0] = visited[a][b][sw]+1
                    elif graph[nx][ny] == 2:
                        if visited[nx][ny][sw] == -1:
                            q.append([nx,ny,1])
                            visited[nx][ny][1] = visited[a][b][sw]+1
                elif sw == 1:
                    if visited[nx][ny][sw] == -1:
                        q.append([nx,ny,sw])
                        visited[nx][ny][sw] =visited[a][b][sw]+1
    return -1


n,m,t = map(int, sys.stdin.readline().rstrip().split())

graph = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[[-1,-1] for _ in range(m) ] for _ in range(n)]

result = bfs()

if result ==-1 or result > t:
    print("Fail")
else:
    print(result)