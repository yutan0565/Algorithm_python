import copy
import sys
from collections import deque
from itertools import product

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

def move_all_fish():
    """
    상어, 물고기의 냄새, 격자 밖   이동 불가
    이동 가능할때 까지, 45도 반시계 방향으로 회전
    """
    temp_graph = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            fish_list = graph[i][j]
            for k in range(len(fish_list)):
                flag = 0
                for d in range(8):
                    new_direct = (fish_list[k] - d) % 8
                    nx = i + dx[new_direct]
                    ny = j + dy[new_direct]
                    if 0<=nx<4 and 0<=ny<4:
                        if not(nx == s_x and ny == s_y):
                            if smell[nx][ny] == 0:
                                temp_graph[nx][ny].append(new_direct)
                                flag = 1
                                break
                if flag == 0 :
                    temp_graph[i][j].append(fish_list[k])
    return temp_graph

def move_shark():

    move_list = []
    max_fish = -1

    dx_s = [-1,0,1,0]
    dy_s = [0,-1,0,1]
    candi_move = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                candi_move.append([i,j,k])

    for move in candi_move:
        x,y = s_x,s_y
        fish = 0#len(graph[x][y])
        flag = 0
        visit_list = []
        for d in move:
            nx = x + dx_s[d]
            ny = y + dy_s[d]
            if 0<=nx<4 and 0<=ny<4:
                if [nx,ny] not in visit_list:
                    fish += len(graph[nx][ny])
                    visit_list.append([nx,ny])
                    x,y = nx,ny
            else:
                flag = 1
                break

        if flag == 1:
            continue
        if fish > max_fish:
            move_list = []
            move_list.append(move)
            max_fish = fish
        elif fish == max_fish:
            move_list.append(move)

    move_list.sort(key = lambda x : ( (x[0]+1)*100 + (x[1]+1)*10 + (x[2]+1)*1    ))
    move_direct = move_list[0]

    x,y = s_x,s_y
    # if len(graph[x][y]) >= 1:
    #     smell[x][y] = 3
    for d in move_direct:
        nx = x + dx_s[d]
        ny = y + dy_s[d]
        if len(graph[nx][ny]) >= 1:
            smell[nx][ny] = 3
        graph[nx][ny] = []
        x, y = nx, ny
    new_s_x, new_s_y = x,y
    return new_s_x, new_s_y

def del_smell():
    for i in range(4):
        for j in range(4):
            if smell[i][j] != 0:
                smell[i][j] -= 1

def add_copy():
    for i in range(4):
        for j in range(4):
            graph[i][j] = graph[i][j] + copy_fish_graph[i][j]

def cal_fish():
    count = 0
    for i in range(4):
        for j in range(4):
            count += len(graph[i][j])
    return count

m,s = map(int,sys.stdin.readline().rstrip().split())
graph = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]

for _ in range(m):
    f_x,f_y,d = map(int,sys.stdin.readline().rstrip().split())
    graph[f_x-1][f_y-1].append(d-1)

s_x,s_y = map(int,sys.stdin.readline().rstrip().split())
s_x,s_y = s_x-1,s_y-1

for _ in range(s):
    # 현재 상태를 복사
    copy_fish_graph = copy.deepcopy(graph)

    # 모든 물고기 이동
    graph = move_all_fish()

    # 상어가 연속해서 3칸 이동
    s_x,s_y = move_shark()

    # 냄새 사라짐
    del_smell()

    # 복제한거 더해주기
    add_copy()


result = cal_fish()
print(result)

"""
5 4
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
4 2
1. 복제 마법 시전 ( 5번에서 물고기가 복제되어 칸에 나타남)
2. 모든 물고기가 이동
    상어, 물고기의 냄새, 격자 밖   이동 불가
    이동 가능할때 까지, 45도 반시계 방향으로 회전

3. 상어가 연속해서 3칸 이동
    상하좌우 인접 칸으로 이동 가능
        이동하는 칸이 격자 밖이면, 불가능한 이동임
    물고기가 있는 곳
        물고기의 냄새를 남김 ( 2 ) 
        그 물고기들은 격자에서 제외
    
    이 기롥을 쌓아두고,  가장 많은 물고기를 제외하는 방식으로 이동
    똑같은 수가 여러가지면 ( 사전 ) 순으로 가장 앞서는 방법 선택
    
4. 두번 전 냄새가 사라짐 ( 냄새 -= 1  )

5. 복제 마법이 완료 (1에서의 위치와 방향을 그대로 갖게 됨)

"""