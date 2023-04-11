import copy
from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited = copy.deepcopy(reset_visited)
    visited[x][y] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<h+2 and 0<=ny<w+2:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == '.':
                        q.appendleft([nx,ny])
                        visited[nx][ny] = visited[a][b]
                    elif graph[nx][ny] == '#':
                        q.append([nx,ny])
                        visited[nx][ny] = visited[a][b] + 1

    return visited


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    h,w = map(int, sys.stdin.readline().rstrip().split())
    graph = [['.' for _ in range(w+2)]]
    p_list = []
    door_count = 0
    for i in range(1, h + 1):
        graph.append(['.'] + list(sys.stdin.readline().rstrip()) + ['.'] )
        for j in range(1, w + 1):
            if graph[i][j] == '$':
                p_list.append([i,j])
                graph[i][j] = '.'
    graph.append(['.' for _ in range(w+2)])
    f_x = p_list[0][0]
    f_y = p_list[0][1]
    s_x = p_list[1][0]
    s_y = p_list[1][1]

    reset_visited = [[-1 for _ in range(w+2)] for _ in range(h+2)]

    first_visited = bfs(f_x, f_y)
    second_visited = bfs(s_x, s_y)
    other_visited = bfs(0, 0)

    total_door = [[0 for _ in range(w+2)] for _ in range(h+2)]

    result = float('inf')
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if first_visited[i][j] != -1 and second_visited[i][j] != -1 and other_visited[i][j] != -1:
                temp = first_visited[i][j] + second_visited[i][j] + other_visited[i][j]
                if graph[i][j] == '#':
                    temp -= 2
                result = min(result, temp)
    print(result)