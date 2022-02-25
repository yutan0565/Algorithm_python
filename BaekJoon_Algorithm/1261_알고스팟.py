import sys
from collections import deque

def bfs(graph, visited, x, y ,m,n):
    q = deque()
    q.append([x,y])
    visited[x][y] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = visited[a][b]
                        # 왼쪽에 넣어줘서, 우선 순위를 먼저 해주기!!
                        # 벽 부수는 것보다는, 최소한으로 안부수고 움직이게 해주기
                        q.appendleft([nx, ny])
                    elif graph[nx][ny]  == 1:
                        visited[nx][ny] = visited[a][b]+1
                        q.append([nx,ny])

    return visited[n-1][m-1]


m, n = map(int, sys.stdin.readline().rstrip().split())
graph = [  list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)  ]
visited = [[-1]*m for _ in range(n)]
result = bfs(graph, visited, 0, 0,m,n)
print(result)