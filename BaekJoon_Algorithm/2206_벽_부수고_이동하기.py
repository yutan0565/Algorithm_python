import sys
from collections import deque

def bfs(N, M, graph, visited):
    q = deque()
    q.append([0,0,1])
    visited[0][0][1] = 1

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while q:
        a,b,flag = q.popleft()
        if a == N-1 and b == M-1:
            for i in visited:
                print(i)
            return visited[a][b][flag]

        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >=0 and ny >= 0 and nx < N and ny < M:
                if graph[nx][ny] == 1 and flag  == 1:
                    visited[nx][ny][0] = visited[a][b][flag] +1
                    q.append([nx,ny,0])
                elif graph[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                    visited[nx][ny][flag] = visited[a][b][flag] + 1
                    q.append([nx,ny,flag])

    return  -1




N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

visited = [ [[0, 0] for _ in range(M)] for _ in range(N)]

result = bfs(N, M, graph, visited)
print(result)
