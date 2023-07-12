import sys
from collections import deque

# 가로, 세로
M , N = map(int, sys.stdin.readline().rstrip().split())
graph = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N) ]
visited  = [ [False]*M for _ in range(N) ]


# 1 익은거, 0안익은거, -1 빈곳

def bfs(temp_list):
    global M, N, graph, visited
    q = deque()

    for i in temp_list:
        q.append(i)
        visited[i[0]][i[1]] = True
        graph[i[0]][i[1]] = 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    result = 0
    while q:
        result += 1
        print(result, len(q))
        for i in range(len(q)):
            a, b = q.popleft()
            for i in range(len(dx)):
                nx = a + dx[i]
                ny = b + dy[i]
                if nx >=0 and ny >=0 and nx < N and ny < M:
                    if visited[nx][ny] != True:
                        if graph[nx][ny] == 0:
                            q.append([nx, ny])
                            visited[nx][ny] = True
                            graph[nx][ny] = graph[a][b] + 1

    temp_max = -1
    for i in range(N):
        for j in range(M):
            # if temp_max < graph[i][j]:
            #     temp_max = graph[i][j]
            if graph[i][j] == 0:
                return 0

    return result


temp_list = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            temp_list.append([i, j])

print(bfs(temp_list) - 1)