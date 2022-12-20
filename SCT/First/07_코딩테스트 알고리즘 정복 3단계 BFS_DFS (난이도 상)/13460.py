import copy
from collections import deque
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def move_line(p, k, g):
    move = 0
    new_x = p[0]
    new_y = p[1]
    while 1:
        if g[new_x + dx[k]][new_y + dy[k]] == '#' or g[new_x][new_y] == 'O':
            break
        new_x += dx[k]
        new_y += dy[k]
        move += 1
    return new_x, new_y, move, g


def bfs():
    q = deque()
    q.append([red_start, blue_start, 1])
    ball_list = []
    ball_list.append([red_start, blue_start])

    while q:
        r,b, count = q.popleft()
        graph = copy.deepcopy(reset_graph)
        graph[r[0]][r[1]] = 'R'
        graph[b[0]][b[1]] = 'B'

        if count > 10:
            return -1
        for i in range(4):
            nx_r, ny_r, move_r, grpah = move_line(r, i, graph)
            nx_b, ny_b, move_b, graph = move_line(b, i, graph)
            if [nx_b, ny_b] != end:
                if [nx_r,ny_r] == end:
                    return count

                if [nx_r, ny_r] == [nx_b,ny_b]:
                    if move_r > move_b:
                        nx_r -= dx[i]
                        ny_r -= dy[i]
                    else:
                        nx_b -= dx[i]
                        ny_b -= dy[i]

                if [[nx_r,ny_r],[nx_b,ny_b]] not in ball_list:
                    q.append([[nx_r,ny_r], [nx_b, ny_b], count +1])
                    ball_list.append([[nx_r,ny_r], [nx_b, ny_b]])
    return -1

n,m = map(int, sys.stdin.readline().rstrip().split())
red_start = []
blue_start = []
end = []
reset_graph = []
for i in range(n):
    reset_graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if reset_graph[i][j] == "R":
            red_start = [i,j]
            reset_graph[i][j] = "."
        elif reset_graph[i][j] == "B":
            blue_start = [i,j]
            reset_graph[i][j] = "."
        elif reset_graph[i][j] == "O":
            end = [i,j]

result = bfs()
print(result)
