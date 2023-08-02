import copy
import sys
from collections import deque

def set_wall(x,y,s):
    # 바로 위에 벽
    if s == 0:
        wall[x][y].append(3)
        wall[x-1][y].append(5)
    # 바로 왼쪽에 벽
    elif s == 1:
        wall[x][y].append(2)
        wall[x][y-1].append(4)

def check_temper():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                if temper[i][j] < k:
                    return 1
    return 0

def start_blow(x,y,direct):
    sub_blow = dict_sub_blow[direct]
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    x,y = x + dx[direct], y + dy[direct]
    visited[x][y] = 1
    temper[x][y] += 5
    q.append([x,y,4])
    candi_blow = sub_blow + [direct]
    while q:
        a,b,air = q.popleft()
        if air == 0:
            break
        for i in range(len(candi_blow)):
            now_direct = candi_blow[i]
            if i == 2: # 정 방향으로 그냥 가는 경우
                nx = a + dx[now_direct]
                ny = b + dy[now_direct]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if direct not in wall[a][b]:
                            temper[nx][ny] += air
                            visited[nx][ny] = 1
                            q.append([nx,ny, air-1])
            # 꺽여서 가는 경우
            else:
                if i == 0:
                    now_sub_blow = dict_sub_blow[direct][i]
                    check_x, check_y = a + dx[now_sub_blow], b + dy[now_sub_blow]
                    check_direct_list = [dict_check_direct[direct][0], dict_check_direct[direct][1]]
                    nx = check_x + dx[direct]
                    ny = check_y + dy[direct]
                    if 0 <= nx < n and 0 <= ny < n:
                        if visited[nx][ny] == -1:
                            # 체크 박스, 환인 해보기 - 이동 가능한가 확인
                            if check_direct_list[0] not in wall[check_x][check_y]:
                                if  check_direct_list[1] not in wall[check_x][check_y]:
                                    temper[nx][ny] += air
                                    visited[nx][ny] = 1
                                    q.append([nx, ny, air - 1])
                elif i == 1:
                    now_sub_blow = dict_sub_blow[direct][i]
                    check_x, check_y = a + dx[now_sub_blow], b + dy[now_sub_blow]
                    check_direct_list = [dict_check_direct[direct][2], dict_check_direct[direct][3]]
                    nx = check_x + dx[direct]
                    ny = check_y + dy[direct]
                    if 0 <= nx < n and 0 <= ny < n:
                        if visited[nx][ny] == -1:
                            # 체크 박스, 환인 해보기 - 이동 가능한가 확인
                            if check_direct_list[0] not in wall[check_x][check_y]:
                                if  check_direct_list[1] not in wall[check_x][check_y]:
                                    temper[nx][ny] += air
                                    visited[nx][ny] = 1
                                    q.append([nx, ny, air - 1])

def combine_temper():
    new_temper = copy.deepcopy(temper)
    for i in range(n):
        for j in range(n):
            now_temp = temper[i][j]
            for d in range(2,6):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    # 벽이 아니면
                    if d not in wall[i][j]:
                        other_temp = temper[nx][ny]
                        if now_temp > other_temp:
                            gap = (now_temp - other_temp) // 4
                            new_temper[i][j] -= gap
                            new_temper[nx][ny] += gap

    return new_temper

def down_temper():
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                if temper[i][j] != 0:
                    temper[i][j] -= 1

n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph = []
air_pos = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j] >= 2:
            air_pos.append([i,j])

temper = [[0 for _ in range(n)] for _ in range(n)]
wall = [[[] for _ in range(n)] for _ in range(n)]

# 벽 설정 해주기
for _ in range(m):
    x,y,s = map(int,sys.stdin.readline().rstrip().split())
    x,y = x-1, y-1
    set_wall(x,y,s)

# 0 빈공간 , 1 사무실, 2 왼, 3 위, 4 오, 5 아래
dx = [0,0,0,-1,0,1]
dy = [0,0,-1,0,1,0]

# 옆으로 퍼지는 곳
dict_sub_blow = {2 : [3, 5], 3 : [2,4], 4:[3,5], 5:[2,4]}
dict_check_direct = {2 : [5,2,3,2], 3 : [4,3,2,3], 4 : [5,4,3,4], 5 : [4,5,2,5]}

result = 0
while 1:
    end_flag = check_temper()
    if end_flag == 0:
        break
    if result == 101:
        result = -1
        break
    # 바람 불기
    for x,y in air_pos:
        direct = graph[x][y]
        start_blow(x,y,direct)

    # 바람 섞기
    temper = combine_temper()
    # 벽 낮추기
    down_temper()
    result += 1

print(result)

"""
"""