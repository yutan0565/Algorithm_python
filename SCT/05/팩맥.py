import copy
import sys
from collections import deque

def move_monster():
    global graph_mon
    new_graph_mon = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if graph_mon[i][j] != []:
                for mon_direct in graph_mon[i][j]:
                    change_flag = False
                    for temp in range(8):
                        direct = (mon_direct + temp)%8
                        nx = i + dx[direct]
                        ny = j + dy[direct]
                        if not(0<=nx<4 and 0<=ny<4):
                            continue
                        if [nx,ny] == [pac_x,pac_y]:
                            continue
                        if graph_dead[nx][ny] != 0:
                            continue
                        change_flag = True
                        new_graph_mon[nx][ny].append(direct)
                        break
                    if change_flag == False:
                        new_graph_mon[i][j].append(mon_direct)
    graph_mon = new_graph_mon

def eat_mon_start(move_list):
    x,y = pac_x, pac_y
    now_eat = 0
    now_pos_list = []
    for d in move_list:
        x = x + dx_pac[d]
        y = y + dy_pac[d]
        # 범위 벗어나는 경우
        if not(0<=x<4 and 0<=y<4):
            return -1, []
        # 중복 되지 않는 경우만 증가
        if [x,y] not in now_pos_list:
            now_eat += len(graph_mon[x][y])
        now_pos_list.append([x,y])
    return now_eat, now_pos_list

def move_pac():
    global  pac_x, pac_y
    max_eat = -1
    max_pos_list = [0,0,0]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                move_list = [i,j,k]
                now_eat, now_pos_list = eat_mon_start(move_list)
                if now_eat == -1:
                    continue
                else:
                    if now_eat > max_eat:
                        max_eat = now_eat
                        max_pos_list = now_pos_list
    # 먹기 시작
    for a,b in max_pos_list:
        if graph_mon[a][b] != []:
            graph_dead[a][b] = 3
            graph_mon[a][b] = []
    pac_x,pac_y = max_pos_list[-1]

def down_dead():
    for i in range(4):
        for j in range(4):
            if graph_dead[i][j] != 0:
                graph_dead[i][j] -= 1

def comple_copy(graph_mon_copy):
    global graph_mon
    for i in range(4):
        for j in range(4):
            graph_mon[i][j] = graph_mon[i][j] + graph_mon_copy[i][j]

def show_graph():
    print("============")
    for g in graph_mon:
        print(g)
    print()
    for g in graph_dead:
        print(g)


def simulation_show():
    for turn in range(1, t+1):
        print("===================")
        print([pac_x,pac_y])
        # 몬스터 복제
        graph_mon_copy = copy.deepcopy(graph_mon)
        show_graph()
        # 몬스터 이동
        move_monster()
        show_graph()
        # 팩맨 이동
        move_pac()
        print([pac_x, pac_y])
        # 시체 소멸
        down_dead()
        show_graph()
        # 복제 완성
        comple_copy(graph_mon_copy)
        show_graph()

def simulation():
    for turn in range(1, t+1):
        # 몬스터 복제
        graph_mon_copy = copy.deepcopy(graph_mon)
        # 몬스터 이동
        move_monster()
        # 팩맨 이동
        move_pac()
        # 시체 소멸
        down_dead()
        # 복제 완성
        comple_copy(graph_mon_copy)

def cal_mon():
    result = 0
    for i in range(4):
        for j in range(4):
            result += len(graph_mon[i][j])
    return result

m,t = map(int,sys.stdin.readline().rstrip().split())
pac_x, pac_y = map(int,sys.stdin.readline().rstrip().split())
pac_x -=1
pac_y -=1
graph_mon = [[[] for _ in range(4)] for _ in range(4)]
graph_dead = [[0 for _ in range(4)] for _ in range(4)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

dx_pac = [-1,0,1,0]
dy_pac = [0,-1,0,1]

for _ in range(m):
    r,c,d = map(int,sys.stdin.readline().rstrip().split())
    r -= 1
    c -= 1
    d -= 1
    graph_mon[r][c].append(d)

simulation()
result = cal_mon()
print(result)


