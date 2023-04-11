from collections import deque
import sys

def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b,count = q.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b][count]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    if count < k:
                        if visited[nx][ny][count + 1] == -1:
                            q.append([nx,ny,count+1])
                            visited[nx][ny][count+1] = visited[a][b][count] + 1
                elif graph[nx][ny] == 0:
                    if visited[nx][ny][count] == -1:
                        q.append([nx,ny,count])
                        visited[nx][ny][count] = visited[a][b][count] + 1
    return -1

n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [ list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited = [[[-1 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

result = bfs()
print(result)

