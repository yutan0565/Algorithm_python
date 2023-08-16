import sys
from collections import defaultdict

# 목스터 복제
def copy_mon():
    return graph_mon

# 몬스터 이동
def move_mon():
    new_graph_mon = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if graph_mon[i][j] != []:
                mon_list = graph_mon[i][j]
                for now_direct in mon_list:
                    find_flag = 0
                    for plus in range(8):
                        new_direct = (now_direct + plus)%8
                        nx = i + dx_mon[new_direct]
                        ny = j + dy_mon[new_direct]
                        if 0<=nx<4 and 0<=ny<4:
                            if graph_dead[nx][ny] == -1:
                                if [nx,ny] != [pac_x, pac_y]:
                                    new_graph_mon[nx][ny].append(new_direct)
                                    find_flag = 1
                                    break
                    # 다른 방향 못찾은 경우
                    if find_flag == 0:
                        new_graph_mon[i][j].append(now_direct)
    return new_graph_mon

# 팩맨 이동
def move_pac():
    global pac_x,pac_y
    max_eat = -1
    candi_list = []
    for f in range(4):
        for s in range(4):
            for th in range(4):
                x,y = pac_x,pac_y
                eat_mon = 0
                stop_flag = 0
                visit_list = []
                for d in [f,s,th]:
                    x = x + dx_pac[d]
                    y = y + dy_pac[d]
                    if not(0<=x<4 and 0<=y<4):
                        stop_flag = 1
                        break
                    if [x,y] not in visit_list:
                        eat_mon += len(graph_mon[x][y])
                    visit_list.append([x,y])
                if stop_flag == 0:
                    if eat_mon > max_eat:
                        candi_list = [[f,s,th]]
                        max_eat = eat_mon
                    elif eat_mon == max_eat:
                        candi_list.append([f,s,th])
    candi_list.sort(key = lambda x:[x[0],x[1],x[2]])
    max_move = candi_list[0]

    x,y = pac_x,pac_y
    for d in max_move:
        x = x + dx_pac[d]
        y = y + dy_pac[d]
        if graph_mon[x][y] != []:
            graph_dead[x][y] = 2
            graph_mon[x][y] = []
    pac_x,pac_y = x,y

# 몬스터 시체 소멸
def down_dead():
    for i in range(4):
        for j in range(4):
            if graph_dead[i][j] != -1:
                graph_dead[i][j] -= 1

# 몬스터 복제 완성
def clear_copy_monster():
    new_graph_mon = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_graph_mon[i][j] = graph_mon[i][j] + copy_graph[i][j]
    return new_graph_mon

def cal_mon():
    count = 0
    for i in range(4):
        for j in range(4):
            count += len(graph_mon[i][j])
    return count

m,t = map(int,sys.stdin.readline().rstrip().split())
pac_x, pac_y =  map(int,sys.stdin.readline().rstrip().split())
pac_x, pac_y = pac_x-1, pac_y-1

graph_mon = [[[] for _ in range(4)] for _ in range(4)]
graph_dead = [[-1 for _ in range(4)] for _ in range(4)]

dx_mon = [-1,-1,0,1,1,1,0,-1]
dy_mon = [0,-1,-1,-1,0,1,1,1]

dx_pac = [-1,0,1,0]
dy_pac = [0,-1,0,1]

for num in range(1, m+1):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    a,b,c = a-1, b-1, c-1
    graph_mon[a][b].append(c)

for turn in range(1, t+1):

    # 목스터 복제
    copy_graph = copy_mon()

    # 몬스터 이동
    graph_mon =  move_mon()

    # 팩맨 이동
    move_pac()

    # 몬스터 시체 소멸
    down_dead()

    # 몬스터 복제 완성
    graph_mon = clear_copy_monster()


result = cal_mon()
print(result)
"""
4 1
3 1
1 3 5
2 2 7
3 4 6
4 2 2


"""
