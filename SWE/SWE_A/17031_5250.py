from collections import deque

def daik():
    q = deque()
    q.append([0,0])
    visited[0][0] = 0

    while q:
        a, b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                gap = 0
                if graph[nx][ny] > graph[a][b]:
                    gap = graph[nx][ny] -  graph[a][b]
                if visited[nx][ny] > visited[a][b] + gap + 1:
                    visited[nx][ny] = visited[a][b] + gap + 1
                    q.append([nx,ny])
    return visited[n-1][n-1]

t = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for test_case in range(1,t+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [[int(2e10) for _ in range(n)] for _ in range(n)]
    result = daik()
    print("#{} {}".format(test_case, result))