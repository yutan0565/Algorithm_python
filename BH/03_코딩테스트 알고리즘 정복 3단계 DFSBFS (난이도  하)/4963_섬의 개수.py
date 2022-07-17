import sys
from collections import deque

def bfs(graph, x, y):
    q = deque()
    q.append([x,y])
    graph[x][y] = group_count

    dx = [1, -1, 0 , 0 , 1 , 1, -1 ,-1 ]
    dy = [0,  0, 1,  -1, 1,  -1, 1 , -1]

    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >=0 and ny >= 0 and nx < h and ny < w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = group_count
                    q.append([nx,ny])

while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
    group_count = 1
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                group_count += 1
                bfs(graph, x, y)


    print(group_count - 1)