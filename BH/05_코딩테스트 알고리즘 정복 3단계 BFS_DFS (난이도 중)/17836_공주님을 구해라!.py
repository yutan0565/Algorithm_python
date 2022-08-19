import sys
from collections import deque

def bfs():
    global graph, visited
    q = deque()
    q.append([0,0,0])
    graph[0][0] = 3
    visited[0][0][0] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        a,b,sword = q.popleft()
        if a == n-1 and b == m-1:
            return graph[a][b] - 3
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx< n and 0<=ny<m:
                if visited[nx][ny][sword] == False:
                    if sword == 1:
                        q.append([nx,ny,1])
                        graph[nx][ny] = graph[a][b] + 1
                        visited[nx][ny][1] = True
                    elif graph[nx][ny] != 1:
                        if graph[nx][ny] == 2:
                            q.append([nx, ny, 1])
                            graph[nx][ny] = graph[a][b] + 1
                            visited[nx][ny][1] = True
                        else:
                            q.append([nx,ny,0])
                            graph[nx][ny] = graph[a][b] + 1
                            visited[nx][ny][0] = True
    return 1000001

n,m,t = map(int,sys.stdin.readline().rstrip().split())
graph = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[[False,False] for _ in range(m)] for _ in range(n) ]

result = bfs()

if result > t:
    print("Fail")
else:
    print(result)



