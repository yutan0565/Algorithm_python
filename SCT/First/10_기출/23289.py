import copy
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def make_wind(x,y,direct):
    q = deque()
    q.append([x,y, 5])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    flag_first = 0
    while q:
        for _ in range(len(q)):
            a,b,temp = q.popleft()
            if flag_first == 0:
                wind_direct = [0]
                flag_first = 1
            else:
                wind_direct = [-1,0,1]
            for i in wind_direct:
                if direct == 0 or direct == 1:
                    nx = a + i
                    ny = b + dy[direct]
                elif direct == 2 or direct == 3:
                    nx = a + dx[direct]
                    ny = b + i
                if 0<=nx<n and 0<=ny<m:
                    if visited[nx][ny] == 0:
                        if i == 0:
                            if [[a,b],[nx,ny]] not in wall_list :
                                if temp != 0:
                                    q.append([nx,ny, temp - 1])
                                    visited[nx][ny] = 1
                                    temper[nx][ny] += temp
                        else :
                            if direct == 0 or direct == 1:
                                if [[a, b], [nx, ny-dy[direct]]] not in wall_list and [[nx,ny-dy[direct]], [nx, ny]] not in wall_list:
                                    if temp != 0:
                                        q.append([nx, ny, temp - 1])
                                        visited[nx][ny] = 1
                                        temper[nx][ny] += temp
                            elif direct == 2 or direct == 3:
                                if [[a, b], [ny-dx[direct], ny]] not in wall_list and [[nx-dx[direct], ny], [nx, ny]] not in wall_list:
                                    if temp != 0:
                                        q.append([nx, ny, temp - 1])
                                        visited[nx][ny] = 1
                                        temper[nx][ny] += temp

# 온도 조절
def turn_temper():
    temp_temper = copy.deepcopy(temper)
    turn_list = []
    for i in range(n):
        for j in range(m):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0<=nx<n and 0<=ny<m:
                    if [[i,j],[nx,ny]] not in turn_list:
                        chai = temper[i][j] - temper[nx][ny]
                        if chai >= 4:
                            temp_temper[i][j] -= chai//4
                            temp_temper[nx][ny] += chai // 4
                            turn_list.append([[nx,ny], [i,j]])
    return temp_temper

def make_big_size_temper():
    global temper
    temper = [[0 for _ in range(m+2)]] + temper + [[0 for _ in range(m+2)]]
    for i in range(1, n+1):
        temper[i] = [0] + temper[i] + [0]


def down_temper():
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n-1 or j == m-1:
                if temper[i][j] != 0:
                    temper[i][j] -= 1
    return temper
    # global temper
    # make_big_size_temper()
    # temp_big_temper = copy.deepcopy(temper)
    # q = deque()
    # q.append([0,0])
    # visited = [[0 for _ in range(m+2)] for _ in range(n+2)]
    # visited[0][0] = 1
    #
    # while q:
    #     a,b = q.popleft()
    #     for i in range(4):
    #         nx = a + dx[i]
    #         ny = b + dy[i]
    #         if 0 <= nx < n+2 and 0 <= ny < m+2:
    #             if visited[nx][ny] == 0:
    #                 if temper[nx][ny] == 0:
    #                     q.append([nx,ny])
    #                     visited[nx][ny] = 1
    #                 else:
    #                     print([nx,ny])
    #                     temp_big_temper[nx][ny] -= 1
    #                     visited[nx][ny] = 1
    # print("늘림")
    # for t in temp_big_temper:
    #     print(t)
    # out_temper = []
    # for i in range(1,n+1):
    #     out_temper.append(temp_big_temper[i][1:m+1])
    # return out_temper


def check_temper():
    for machine in dict_machine.keys():
        if dict_machine[machine][2] == 5:
            x = dict_machine[machine][0]
            y = dict_machine[machine][1]
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
wall_list = []
for _ in range(w):
    x,y,t = map(int, sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    if t == 0:
        if 0<=x-1<n and 0<=y<m:
            wall_list.append([[x-1,y],[x,y]])
            wall_list.append([[x, y], [x-1, y]])
    elif t == 1:
        if 0 <= x < n and 0 <= y + 1  < m:
            wall_list.append([[x,y+1],[x,y]])
            wall_list.append([[x, y], [x, y+1]])

result = 0

def show_temp():
    for t in temper:
        print(t)

print(wall_list)
while 1:
    print(result)

    print("처음")
    show_temp()

    # 온풍기 바람이 나옴
    for machine in dict_machine.keys():
        if dict_machine[machine][2] != 5:
            now_direct = dict_machine[machine][2] - 1
            make_wind(dict_machine[machine][0],dict_machine[machine][1],now_direct)

            print("바람")
            show_temp()

    # 온도 조절
    temper = turn_temper()

    print("조절")
    show_temp()

    # 온도가 1 이상인 가장 바깥쪽 온도가 1 씩 감소
    temper = down_temper()

    print("온도 내림")
    show_temp()

    result += 1
    if check_temper() == 1:
        break
print(result)