import copy
import sys
from itertools import permutations

def move_monster():
    new_graph_monster = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for direct in graph_monster[i][j]:
                new_x = i
                new_y = j
                new_direct = direct
                for rotate in range(8):
                    nx = i + dx_mon[(direct+rotate)%8]
                    ny = j + dy_mon[(direct+rotate)%8]
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if graph_dead[nx][ny] == -1:
                            if [nx,ny] != man_pos:
                                new_x = nx
                                new_y = ny
                                new_direct = (direct+rotate)%8
                                break
                new_graph_monster[new_x][new_y].append(new_direct)
    return new_graph_monster

def move_man():
    max_eat = -1
    list_man_move = []
    for candi_move in candi_man_move:
        temp_eat = 0
        flag = 0
        x, y = man_pos
        move_list = []
        for d in candi_move:
            x = x + dx_man[d]
            y = y + dy_man[d]
            if 0 <= x < 4 and 0 <= y < 4:
                if [x,y] not in move_list:
                    temp_eat += len(graph_monster[x][y])
                    move_list.append([x, y])
            else:
                flag = 1
                break
        if flag == 0:
            if temp_eat > max_eat:
                list_man_move = candi_move
                max_eat = temp_eat
    # print("움직임 : ", list_man_move, max_eat)
    return list_man_move

def dead_monster(list_man_move):
    global  man_pos
    x,y = man_pos
    for d in list_man_move:
        x = x + dx_man[d]
        y = y + dy_man[d]
        if len(graph_monster[x][y]) != 0:
            graph_monster[x][y] = []
            graph_dead[x][y] = 2
    man_pos = [x,y]

def down_dead_graph():
    for i in range(4):
        for j in range(4):
            if graph_dead[i][j] != -1:
                graph_dead[i][j] -= 1

def complte_copy_monster():
    for i in range(4):
        for j in range(4):
            graph_monster[i][j] += graph_copy[i][j]

def count_monster():
    result = 0
    for i in range(4):
        for j in range(4):
            result += len(graph_monster[i][j])
    return result

m,t = map(int,sys.stdin.readline().rstrip().split())
r,c = map(int,sys.stdin.readline().rstrip().split())

man_pos = [r-1,c-1]
graph_monster = [[[] for _ in range(4)] for _ in range(4)]
graph_dead = [[ -1 for _ in range(4)] for _ in range(4)]
graph_copy = [[[] for _ in range(4)] for _ in range(4)]

dx_mon = [-1,-1,0,1,1,1,0,-1]
dy_mon = [0,-1,-1,-1,0,1,1,1]

dx_man = [-1,0,1,0]
dy_man = [0,-1,0,1]
candi_man_move = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            candi_man_move.append([i,j,k])

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph_monster[a-1][b-1].append(c-1)


def show_graph(graph):
    for g in graph:
        print(g)
    print()


for round in range(t):
    # 몬스터 복제 시도
    graph_copy = copy.deepcopy(graph_monster)
    # 몬스터 이동
    graph_monster = move_monster()
    # 팩맨 이동
    list_man_move = move_man()
    # 몬스터 시체 소멸
    dead_monster(list_man_move)
    # 몬스터 복제 완성
    complte_copy_monster()
    # 시체 타임 감소
    down_dead_graph()

# for round in range(t):
#     print(round +1)
#     # 몬스터 복제 시도
#     graph_copy = copy.deepcopy(graph_monster)
#     # 몬스터 이동
#     graph_monster = move_monster()
#     print("몬스터 이동")
#     show_graph(graph_monster)
#     # 팩맨 이동
#     list_man_move = move_man()
#     # 몬스터 시체 소멸
#     dead_monster(list_man_move)
#     print("먹기")
#     show_graph(graph_monster)
#     show_graph(graph_dead)
#     print(man_pos)
#     # 몬스터 복제 완성
#     complte_copy_monster()
#     print("부화")
#     show_graph(graph_monster)
#     # 시체 타임 감소
#     down_dead_graph()

result = count_monster()
print(result)



"""
몬스터 복제 시도
몬스터 이동
팩맨 이동
몬스터 시체 소멸
몬스터 복제 완성
"""