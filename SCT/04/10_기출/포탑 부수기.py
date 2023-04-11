from collections import deque
import sys

def find_low():
    min_x,min_y = 0,0
    min_row_col_sum = n*m+1
    min_value = float("inf")
    min_turn = -1

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                now_value = graph[i][j]
                now_turn = turn_graph[i][j]
                now_row_col_sum = i+j+2
                if now_value < min_value:
                    min_x,min_y = i,j
                    min_row_col_sum = i+j+2
                    min_value = graph[i][j]
                    min_turn = turn_graph[i][j]
                elif now_value == min_value:
                    if now_turn > min_turn:
                        min_x, min_y = i, j
                        min_row_col_sum = i + j + 2
                        min_value = graph[i][j]
                        min_turn = turn_graph[i][j]
                    elif now_turn == min_turn:
                        if now_row_col_sum > min_row_col_sum:
                            min_x, min_y = i, j
                            min_row_col_sum = i + j + 2
                            min_value = graph[i][j]
                            min_turn = turn_graph[i][j]
                        elif now_row_col_sum == min_row_col_sum:
                            if j > min_y:
                                min_x, min_y = i, j
                                min_row_col_sum = i + j + 2
                                min_value = graph[i][j]
                                min_turn = turn_graph[i][j]
    return min_x,min_y

def find_high():
    max_x,max_y = 0,0
    max_row_col_sum = n*m+1
    max_value = -1
    max_turn = float("inf")

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                now_value = graph[i][j]
                now_turn = turn_graph[i][j]
                now_row_col_sum = i+j+2
                if now_value > max_value:
                    max_x,max_y = i,j
                    max_row_col_sum = i+j+2
                    max_value = graph[i][j]
                    max_turn = turn_graph[i][j]
                elif now_value == max_value:
                    if now_turn < max_turn:
                        max_x, max_y = i, j
                        max_row_col_sum = i + j + 2
                        max_value = graph[i][j]
                        max_turn = turn_graph[i][j]
                    elif now_turn == max_turn:
                        if now_row_col_sum < max_row_col_sum:
                            max_x, max_y = i, j
                            max_row_col_sum = i + j + 2
                            max_value = graph[i][j]
                            max_turn = turn_graph[i][j]
                        elif now_row_col_sum == max_row_col_sum:
                            if j < max_y:
                                max_x, max_y = i, j
                                max_row_col_sum = i + j + 2
                                max_value = graph[i][j]
                                max_turn = turn_graph[i][j]
    return max_x,max_y

def laser_attack():
    flag = 0
    q = deque()
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[low_x][low_y] = 1
    q.append([low_x,low_y,[]])
    graph[low_x][low_y] += plus_attack
    now_stat = graph[low_x][low_y]
    while q:
        a,b,now_load = q.popleft()
        if [a,b] == [high_x,high_y]:
            for del_x, del_y in now_load:
                check_graph[del_x][del_y] = 1
                if [del_x,del_y] != [high_x,high_y]:
                    graph[del_x][del_y] -= now_stat//2
                else:
                    graph[del_x][del_y] -= now_stat
                if graph[del_x][del_y] <= 0:
                    graph[del_x][del_y] = 0
            flag = 1
            return flag
        for d in range(4):
            nx = (a + dx[d])%n
            ny = (b + dy[d])%m
            if visited[nx][ny] == -1:
                if graph[nx][ny] != 0:
                    new_load = now_load + [[nx,ny]]
                    q.append([nx,ny,new_load])
                    visited[nx][ny] = 1
    return flag

def bomb_attack():
    now_stat = graph[low_x][low_y]
    half_stat = now_stat//2

    graph[high_x][high_y] -= now_stat
    if graph[high_x][high_y] <= 0:
        graph[high_x][high_y] = 0

    for d in range(8):
        nx = (high_x + dx_cross[d]) % n
        ny = (high_y + dy_cross[d]) % m
        if [nx,ny] != [low_x,low_y]:
            check_graph[nx][ny] = 1
            graph[nx][ny] -= half_stat
            if graph[nx][ny] <= 0:
                graph[nx][ny] = 0

def up_graph():
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                if check_graph[i][j] != 1:
                    graph[i][j] += 1

def count_live():
    live_count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                live_count += 1
                if live_count ==2:
                    return live_count
    return live_count

def find_best():
    max_value = -1
    for i in range(n):
        for j in range(m):
            max_value = max(graph[i][j], max_value)
    return max_value

n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
turn_graph = [[0 for _ in range(m)] for _ in range(n)]

plus_attack = n+m
dx = [0,1,0,-1]
dy = [1,0,-1,0]

dx_cross = [-1,-1,0,1,1,1,0,-1]
dy_cross = [0,1,1,1,0,-1,-1,-1]

for turn in range(1,k+1):
    # check_초기화
    check_graph = [[0 for _ in range(m)] for _ in range(n)]

    # 가장 약한거, 강한거 찾기
    low_x, low_y = find_low()
    high_x,high_y = find_high()
    turn_graph[low_x][low_y] = turn
    check_graph[low_x][low_y] = 1
    check_graph[high_x][high_y] = 1
    if [low_x,low_y] == [high_x,high_y]:
        break
    # 레이저 공격 시도
    flag = laser_attack()
    if flag == 0:
        bomb_attack()
    # 포탑 정비
    up_graph()
# 가장 강한 포탐의 공격력 출력
result = find_best()
print(result)

"""
4 4 1
0 1 26 4
8 0 10 13
8 0 11 4
0 0 0 0
"""