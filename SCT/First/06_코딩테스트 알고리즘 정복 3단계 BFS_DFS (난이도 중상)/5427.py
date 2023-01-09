from collections import deque
import sys

def bfs():
    q = deque()
    q_f = deque()
    q.append([start_x, start_y])
    visited[start_x][start_y] = 1

    for fire in fire_list:
        q_f.append([fire[0], fire[1]])

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        for _ in range(len(q_f)):
            a,b = q_f.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if graph[nx][ny] == '.':
                        q_f.append([nx,ny])
                        graph[nx][ny] = '*'

        for _ in range(len(q)):
            a,b = q.popleft()
            if a == 0 or b == 0 or a == n-1 or b == m-1:
                return visited[a][b]
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == '.':
                            q.append([nx,ny])
                            visited[nx][ny] = visited[a][b] + 1
    return -1

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m,n = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    start_x = 0
    start_y = 0
    fire_list = []
    for i in range(n):
        temp = list(sys.stdin.readline().rstrip())
        graph.append(temp)
        for j in range(m):
            if graph[i][j] == '@':
                start_x = i
                start_y = j
            if graph[i][j] == '*':
                fire_list.append([i,j])

    visited = [[-1 for _ in range(m)] for _ in range(n)]
    result = bfs()

    if result == -1:
        print("IMPOSSIBLE")
    else:
        print(result)

