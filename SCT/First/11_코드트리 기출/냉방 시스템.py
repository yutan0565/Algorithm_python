import copy
import sys
from collections import deque


def blow_wind(x,y,direct):
    dx_wind = list_dx_wind[direct]
    dy_wind = list_dy_wind[direct]

    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    nx = x + start_dx_wind[direct]
    ny = y + start_dy_wind[direct]
    visited[nx][ny] = 1
    temper_graph[nx][ny] += 5
    q.append([nx,ny,4])

    while q:
        for _ in range(len(q)):
            a,b,temper = q.popleft()
            if temper == 0:
                break
            for i in range(3):
                nx = a + dx_wind[i]
                ny = b + dy_wind[i]
                if direct == 0 or direct == 2:
                    check_x = a + dx_wind[i]
                    check_y = b
                    sub_check_wall_0 = 3
                    sub_check_wall_1 = 1
                else:
                    check_x = a
                    check_y = b + dy_wind[i]
                    sub_check_wall_0 = 2
                    sub_check_wall_1 = 0
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == -1:
                        if i == 1:
                            if direct not in graph_wall[a][b]:
                                temper_graph[nx][ny] += temper
                                visited[nx][ny] = 1
                                q.append([nx,ny,temper-1])
                        elif i == 0: # 위, 왼
                            if direct not in graph_wall[check_x][check_y]:
                                if sub_check_wall_0 not in graph_wall[check_x][check_y]:
                                    temper_graph[nx][ny] += temper
                                    visited[nx][ny] = 1
                                    q.append([nx, ny, temper - 1])
                        elif i == 2: # 아/ 오
                            if direct not in graph_wall[check_x][check_y]:
                                if sub_check_wall_1 not in graph_wall[check_x][check_y]:
                                    temper_graph[nx][ny] += temper
                                    visited[nx][ny] = 1
                                    q.append([nx, ny, temper - 1])

def mix_temp():
    new_temper_graph = copy.deepcopy(temper_graph)
    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if d not in graph_wall[i][j]:
                        if temper_graph[i][j] - temper_graph[nx][ny] > 0:
                            new_temper_graph[i][j] -= (temper_graph[i][j] - temper_graph[nx][ny])//4
                            new_temper_graph[nx][ny] += (temper_graph[i][j] - temper_graph[nx][ny]) // 4

    return new_temper_graph

def down_temp():
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                if  temper_graph[i][j] != 0:
                    temper_graph[i][j] -= 1

def check_temp():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and temper_graph[i][j] < k:
                return -1
    return 1

dx = [0,-1,0,1]
dy = [-1,0,1,0]

"""
0 왼 벽
1 위 벽
2 오른 벽
3 아래 벽
"""
dx_0 = [-1,0,1]
dy_0 = [-1,-1,-1]

dx_1 = [-1,-1,-1]
dy_1 = [-1,0,1]

dx_2 = [-1,0,1]
dy_2 = [1,1,1]

dx_3 = [1,1,1]
dy_3 = [-1,0,1]

list_dx_wind = [dx_0, dx_1, dx_2, dx_3]
list_dy_wind = [dy_0, dy_1, dy_2, dy_3]

start_dx_wind = [0, -1, 0, 1]
start_dy_wind = [-1, 0, 1, 0]

n,m,k = map(int,sys.stdin.readline().rstrip().split())

list_air_pos = []
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if not(graph[i][j] == 0 or graph[i][j] == 1):
            list_air_pos.append([i,j,graph[i][j]-2])
            graph[i][j] = 0
temper_graph = [[0 for _ in range(n)] for _ in range(n)]
graph_wall = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,s = map(int,sys.stdin.readline().rstrip().split())
    x,y = x-1, y-1
    if s == 0:
        graph_wall[x][y].append(1)
        graph_wall[x-1][y].append(3)
    elif s == 1:
        graph_wall[x][y].append(0)
        graph_wall[x][y-1].append(2)

def show_graph():
    for g in temper_graph:
        print(g)
    print()

result = 0
while 1:
    if check_temp() == 1:
        break
    if result == 101:
        result = -1
        break
    # print("시간: ", result)
    # 바람 불기
    for i,j,d in list_air_pos:
        blow_wind(i,j,d)
    # 공기 섞기
    temper_graph = mix_temp()
    # 외벽 온도 감소
    down_temp()

    result += 1
print(result)
"""
0 빈공간
1 사무실

2 에어컨 왼쪽
3 에어컨 위
4 에어컨 오른
5 에어컨 아래


0 왼 벽
1 위 벽
2 오른 벽
3 아래 벽

1. 바람 불기
2. 공기 섞기
3. 외벽 온도 감소
1 분 증가

전부 k 이상이 되면 종료
"""