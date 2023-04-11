from collections import deque
import sys

def bfs():
    q_w = deque()
    q_s = deque()

    for a,b in water:
        q_w.append([a,b])
        visited[a][b] = -2

    q_s.append([start[0], start[1]])
    visited[start[0]][start[1]] = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q_s:
        for _ in range(len(q_w)):
            a,b = q_w.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<r and 0<=ny<c:
                    if graph[nx][ny] == '.':
                        q_w.append([nx,ny])
                        graph[nx][ny] = '*'

        for _ in range(len(q_s)):
            a, b = q_s.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == '.':
                            q_s.append([nx, ny])
                            visited[nx][ny] = visited[a][b] + 1
                        if graph[nx][ny] == 'D':
                            return visited[a][b] + 1

    return -1

r,c = map(int , sys.stdin.readline().rstrip().split())
graph = []

water = []
start =[0,0]
end = [0,0]

for i in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(c):
        if graph[i][j] == '*':
            water.append([i,j])
        if graph[i][j] == 'S':
            start[0] = i
            start[1] = j
        if graph[i][j] == 'D':
            end[0] = i
            end[1] = j

visited = [[-1 for _ in range(c)] for _ in range(r)]
result = bfs()

if result == -1:
    print("KAKTUS")
else:
    print(result)