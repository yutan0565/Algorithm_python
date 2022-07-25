import sys
from collections import deque

def bfs():
    global graph
    q = deque()
    x = 7
    y = 0
    q.append([x,y])

    dx = [0,0,1,-1,1,1,-1,-1,0]
    dy = [1,-1,0,0,1,-1,1,-1,0]

    while q:
        visited = [[False for _ in range(8)] for _ in range(8)]
        for _ in range(len(q)):
            a,b = q.popleft()
            if a == 0 and b == 7:
                return 1
            if graph[a][b] == '#':
                continue
            for i in range(9):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<8 and 0<=ny<8:
                   if graph[nx][ny] != '#':
                      if visited[nx][ny] == False:
                         q.append([nx,ny])
                         visited[nx][ny] = True
        graph = new_line + graph
        graph = graph[:8][:]
    return 0

graph = [ list(map(str, sys.stdin.readline().rstrip())) for _ in range(8) ]
visited = [ [False for _ in range(8)] for _ in range(8) ]
new_line = [["." for _ in range(8)]]

print(bfs())