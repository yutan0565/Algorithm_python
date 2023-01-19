import copy
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 확인 점을 찾기 위한 좌표
back_move = [-1,1,1,-1]

def make_wind(x,y,direct):
    q = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]

    s_x = x + dx[direct]
    s_y = y + dy[direct]
    temper[s_x][s_y] += 5
    visited[s_x][s_y] = 1
    q.append([s_x,s_y, 4])
    while q:
        for _ in range(len(q)):
            a,b,temp = q.popleft()
            if temp == 0:
                continue
            for i in [-1,0,1]:
                if direct == 0 or direct == 1:
                    # 좡우 이동이면  -  x 축으로 퍼짐 - i,  y 축 방향으로는는 1칸 이동
                    nx = a + i
                    ny = b + dy[direct]
                elif direct == 2 or direct == 3:
                    # 상하 이동이면  -  y 축으로 퍼짐 - i,  x 축 방향으로는는 1칸 이동
                    nx = a + dx[direct]
                    ny = b + i
                if 0<=nx<n and 0<=ny<m:
                    if visited[nx][ny] == 0:
                        if i == 0:
                            if direct not in wall[a][b]:
                                q.append([nx,ny, temp - 1])
                                visited[nx][ny] = 1
                                temper[nx][ny] += temp
                        else :
                            if direct == 0 or direct == 1:
                                check_ny = ny+back_move[direct] 
                                # 확인 점 기준으로,  내가 가는 방향에 벽에 없음
                                if direct not in wall[nx][check_ny]:
                                    if i == -1:
                                        # 위로 퍼지면,  아래쪽 확인
                                        wind_direct = 3
                                    else:
                                        # 아래로 퍼지면 ,위쪽 확인
                                        wind_direct = 2
                                    if wind_direct not in wall[nx][check_ny]:
                                        q.append([nx, ny, temp - 1])
                                        visited[nx][ny] = 1
                                        temper[nx][ny] += temp
                            elif direct == 2 or direct == 3:
                                check_nx = nx+back_move[direct]
                                if direct not in wall[check_nx][ny]:
                                    if i == -1:
                                        # 좌로 갔으면, 우측 확인
                                        wind_direct = 0
                                    else:
                                        # 우로 갔으면, 좌측 확인
                                        wind_direct = 1
                                    if wind_direct not in wall[check_nx][ny]:
                                        q.append([nx, ny, temp - 1])
                                        visited[nx][ny] = 1
                                        temper[nx][ny] += temp

# 온도
def turn_temper():
    temp_temper = copy.deepcopy(temper)
    for i in range(n):
        for j in range(m):
            if temper[i][j] != 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<m:
                        if d not in wall[i][j]:
                            chai = temper[i][j] - temper[nx][ny]
                            if chai >= 4:
                                temp_temper[i][j] -= chai//4
                                temp_temper[nx][ny] += chai // 4

    return temp_temper

def down_temper():
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n-1 or j == m-1:
                if temper[i][j] != 0:
                    temper[i][j] -= 1
    return temper


def check_temper():
    for machine in dict_machine.values():
        if machine[2] == 5:
            x = machine[0]
            y = machine[1]
            if temper[x][y] < k:
                return -1
    return 1

n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dict_machine = {}
machine_number = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            dict_machine[machine_number] = [i,j,graph[i][j]]
            machine_number += 1

temper = [[0 for _ in range(m)] for _ in range(n)]

w = int(sys.stdin.readline().rstrip())
wall = [[[] for _ in range(m)] for _ in range(n)]
for _ in range(w):
    x,y,t = map(int, sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    if t == 1:
        wall[x][y].append(0)    #우
        if y + 1 < m:
            wall[x][y+1].append(1)  #좌
    elif t == 0:
        wall[x][y].append(2)    #위
        if 0 <= x - 1:
            wall[x-1][y].append(3)  #아래
result = 0

def show_temp():
    for t in temper:
        print(t)
    print()

while 1:

    # 온풍기 바람이 나옴
    for machine in dict_machine.keys():
        if dict_machine[machine][2] != 5:
            now_direct = dict_machine[machine][2] - 1
            make_wind(dict_machine[machine][0],dict_machine[machine][1],now_direct)

    # 온도 조절
    temper = turn_temper()

    # 온도가 1 이상인 가장 바깥쪽 온도가 1 씩 감소
    temper = down_temper()

    result += 1
    if result  == 101:
        break
    if check_temper() == 1:
        break

print(result)

"""
7 8 100
0 0 0 0 0 0 0 0
0 0 2 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 1 0
0 1 0 0 0 0 0 0
0 0 0 0 3 0 0 0
9
3 1 0
1 2 0
3 2 1
6 1 1
2 5 1
4 5 1
4 3 1
5 5 0
3 2 0

2 2 5
0 5
1 0
1
1 2 1

"""