import copy
import sys

def move_mon():
    new_graph_mon = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mon_list = graph_mon[i][j]
            if mon_list != []:
                for d in mon_list:
                    stop_flag = 0
                    for plus in range(8):
                        new_d = (d + plus)%8
                        nx = i + dx[new_d]
                        ny = j + dy[new_d]
                        if 0<=nx<4 and 0<=ny<4:
                            if graph_dead[nx][ny] == -1:
                                if [nx,ny] != [pac_x,pac_y]:
                                    new_graph_mon[nx][ny].append(new_d)
                                    stop_flag = 1
                                    break
                    if stop_flag == 0:
                        new_graph_mon[i][j].append(d)
    return new_graph_mon

def find_kill(f,s,th):
    x,y = pac_x,pac_y
    kill_count, kill_line = 0, []
    for d in [f,s,th]:
        x = x + dx_pac[d]
        y = y + dy_pac[d]
        if not(0<=x<4 and 0<=y<4):
            return -1,[]
        else:
            if [x,y] not in kill_line:
                kill_count += len(graph_mon[x][y])
            kill_line.append([x,y])
    return kill_count, kill_line

def move_pac():
    global pac_x,pac_y
    max_kill_count = -1
    max_kill_line = []
    for f in range(4):
        for s in range(4):
            for th in range(4):
                kill_count, kill_line = find_kill(f,s,th)
                if kill_count > max_kill_count:
                    max_kill_count = kill_count
                    max_kill_line = kill_line
    for x,y in max_kill_line:
        if graph_mon[x][y] != []:
            graph_dead[x][y] = 2
        graph_mon[x][y] = []

    pac_x,pac_y = max_kill_line[-1]

def down_dead():
    for i in range(4):
        for j in range(4):
            if graph_dead[i][j] != -1:
                graph_dead[i][j] -= 1

def clear_copy():
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
graph_mon = [[[] for _ in range(4)] for _ in range(4)]
graph_dead = [[-1 for _ in range(4)] for _ in range(4)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

dx_pac = [-1,0,1,0]
dy_pac = [0,-1,0,1]

for _ in range(m):
    r,c,d = map(int,sys.stdin.readline().rstrip().split())
    r,c,d = r-1,c-1,d-1
    graph_mon[r][c].append(d)

for turn in range(1,t+1):
    # 복제
    graph_copy = copy.deepcopy(graph_mon)
    # 몬스터 이동
    graph_mon = move_mon()
    # 팬맨 이동
    move_pac()
    # 몬스터 시체 소멸
    down_dead()
    # 몬스터 복제 완성
    clear_copy()
result = cal_mon()
print(result)

"""
4 3
3 1
1 3 5
2 2 7
3 4 6
4 2 2

"""