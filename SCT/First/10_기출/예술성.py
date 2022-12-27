import copy
from collections import deque
import sys

def rotation_block(x,y, b_size):
    for i in range(0,b_size):
        for j in range(0, b_size):
            new_graph[x+ j][y + b_size-1 - i] = graph[x + i][y+j]

def bfs(x,y):
    q = deque()
    q.append([x,y])

    group_graph[x][y] = group_name
    visited[x][y]  = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == graph[a][b]:
                        q.append([nx,ny])
                        group_graph[nx][ny] = group_name
                        dict_group_count[group_name] += 1
                        visited[nx][ny] = 1

def bfs_line():
    score = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    line_list = []

    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if group_graph[nx][ny] != group_graph[i][j]:
                        if [[nx,ny],[i,j]] not in line_list:
                            f_num = graph[i][j]
                            s_num = graph[nx][ny]
                            f_count = dict_group_count[group_graph[i][j]]
                            s_count = dict_group_count[group_graph[nx][ny]]
                            score += (f_count + s_count )*f_num*s_num
                            line_list.append([[nx,ny],[i,j]])
                            line_list.append([[i, j],[nx, ny]])
    return score

n = int(sys.stdin.readline().rstrip())
b_size = n // 2
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
reset_visited = [[-1 for _ in range(n)] for _ in range(n)]

result = 0
for k in range(4):
    visited = copy.deepcopy(reset_visited)
    group_graph = [[0 for _ in range(n)] for _ in range(n)]
    group_name = 1
    dict_group_count = {}
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                dict_group_count[group_name] = 1
                bfs(i,j)
                group_name += 1

    temp = bfs_line()
    result += temp
    if k == 3:
        break

    new_graph = copy.deepcopy(graph)
    # 블럭 단위 돌리기 - 시계
    rotation_list = [[0, 0], [n - b_size, 0], [0, n - b_size], [n - b_size, n - b_size]]
    for i, j in rotation_list:
        rotation_block(i, j, b_size)
    # 십자가 돌리기  - 시계 반대
    for i in range(n):
        for j in range(n):
            if i == b_size or j == b_size:
                new_graph[n-j-1][i] = graph[i][j]
    graph = new_graph

print(result)