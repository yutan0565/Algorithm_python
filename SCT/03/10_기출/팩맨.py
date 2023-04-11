import copy
import sys

def move_mon():
    new_graph_mon = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if graph_mon[i][j] != []:
                mon_list = graph_mon[i][j]
                for mon_d in mon_list:
                    move_flag = 0
                    for plus in range(8):
                        new_d = (mon_d + plus)%8
                        nx = i + dx[new_d]
                        ny = j + dy[new_d]
                        if 0<=nx<4 and 0<=ny<4:
                            if graph_dead[nx][ny] == -1:
                                if [nx,ny] != [pac_x,pac_y]:
                                    new_graph_mon[nx][ny].append(new_d)
                                    move_flag = 1
                                    break
                    if move_flag == 0:
                        new_graph_mon[i][j].append(mon_d)
    return new_graph_mon

def count_kill(f,s,th):
    x,y = pac_x,pac_y
    kill_count = 0
    move_list = []
    for direct in [f,s,th]:
        x = x + dx_pac[direct]
        y = y + dy_pac[direct]
        if not(0<=x<4 and 0<=y<4):
            return -1, []
        else:
            if [x,y] not in move_list:
                kill_count += len(graph_mon[x][y])
            move_list.append([x,y])
    return kill_count, move_list


def move_pac():
    global pac_x,pac_y
    max_kill = -1
    max_move = []
    for f in range(4):
        for s in range(4):
            for th in range(4):
                temp_kill, move_list = count_kill(f,s,th)
                if temp_kill > max_kill:
                    max_kill = temp_kill
                    max_move = move_list
    for x,y in max_move:
        if graph_mon[x][y] != []:
            graph_mon[x][y] = []
            graph_dead[x][y] = 2
    pac_x,pac_y = max_move[-1]

def down_dead():
    for i in range(4):
        for j in range(4):
            if graph_dead[i][j] != -1:
                graph_dead[i][j] -= 1

def done_copy():
    for i in range(4):
        for j in range(4):
            graph_mon[i][j] = graph_mon[i][j] + graph_copy[i][j]

def cal_mon():
    count = 0
    for i in range(4):
        for j in range(4):
            count += len(graph_mon[i][j])
    return count

m,t = map(int,sys.stdin.readline().rstrip().split())
pac_x,pac_y = map(int,sys.stdin.readline().rstrip().split())
pac_x,pac_y = pac_x-1, pac_y-1

dx_pac = [-1,0,1,0]
dy_pac = [0,-1,0,1]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

graph_mon = [[[] for _ in range(4)] for _ in range(4)]
graph_dead = [[-1 for _ in range(4)] for _ in range(4)]

for _ in range(m):
    r,c,d = map(int,sys.stdin.readline().rstrip().split())
    r,c,d = r-1,c-1,d-1
    graph_mon[r][c].append(d)

for turn in range(1, t + 1):
    # 몬스터 복제
    graph_copy = copy.deepcopy(graph_mon)

    # 몬스터 이동
    graph_mon = move_mon()

    # 팩맨 이동
    move_pac()

    # 몬스터 시체 소명
    down_dead()

    # 몬스터 복제 완성
    done_copy()
    # print(turn)
    # for g in graph_mon:
    #     print(g)
    # print()
    # for g in graph_dead:
    #     print(g)

result = cal_mon()
print(result)

