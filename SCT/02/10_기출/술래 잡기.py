import copy
import sys
from collections import deque

def make_sul_mvoe():
    sul_direct = []
    len_cut = k  + 1# 길이 여기 까지 자르기  // 보는 방향을 위해 하나 더
    one_turn_max = n*n -1
    move_count = 1
    now_direct = 0
    sul_direct = []
    while 1:
        for _ in range(2):
            for _ in range(move_count):
                sul_direct.append(now_direct)
            now_direct = (now_direct +1)%4
        move_count += 1
        if len(sul_direct) >= one_turn_max:
            sul_direct = sul_direct[:one_turn_max]
            break
    for index in range(len(sul_direct)-1,-1,-1):
        sul_direct.append((sul_direct[index] + 2)%4)

    while 1:
        if len(sul_direct) >= len_cut:
            return sul_direct[:len_cut]
        sul_direct += sul_direct

def find_move_theif_list():
    move_theif_list = []
    q = deque()
    q.append([sul_x, sul_y])
    move_theif_list += graph[sul_x][sul_y]
    visited = [ [-1 for _ in range(n)] for _ in range(n)]
    visited[sul_x][sul_y] = 1
    distance = 1
    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            for d in range(4):
                nx = a + dx_sul_direct[d]
                ny = b + dy_sul_direct[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
                        if len(graph[nx][ny]) != 0:
                            move_theif_list += graph[nx][ny]
        distance += 1
        if distance == 4:
            break
    return move_theif_list


def move_theif(move_theif_list):
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) != 0:
                theif_list = graph[i][j]
                for theif_num in theif_list:
                    if theif_num not in move_theif_list:
                        new_graph[i][j].append(theif_num)
                        continue
                    now_d = dict_theif_direct[theif_num]
                    nx = i + dx_theif[now_d]
                    ny = j + dy_theif[now_d]
                    # 범위 밖
                    if not(0<=nx<n and 0<=ny<n):
                        dict_theif_direct[theif_num] = (now_d + 2)%4
                        now_d = dict_theif_direct[theif_num]
                        nx = i + dx_theif[now_d]
                        ny = j + dy_theif[now_d]
                    # 술래가 있는곳
                    if [nx,ny] == [sul_x, sul_y]:
                        # 그대로 있기
                        new_graph[i][j].append(theif_num)
                    else:
                        new_graph[nx][ny].append(theif_num)

    return new_graph

def move_sul(sul_d):
    global  sul_x, sul_y
    sul_x = sul_x + dx_sul_direct[sul_d]
    sul_y = sul_y + dy_sul_direct[sul_d]

def find_theif(see_d, round):
    count = 0
    x,y = sul_x,sul_y
    for _ in range(3):
        if not (0 <= x < n and 0 <= y < n):
            break
        # 나무가 있는 곳이면
        if tree_graph[x][y] == 1:
            x, y = x + dx_sul_direct[see_d], y + dy_sul_direct[see_d]
            continue
        # 도둑이 있던 곳이면
        if len(graph[x][y]) != 0:
            count += len(graph[x][y])
            graph[x][y] = []
        x,y = x + dx_sul_direct[see_d], y + dy_sul_direct[see_d]
    score = round * count
    return score


n,m,h,k = map(int,sys.stdin.readline().rstrip().split())
graph = [[[] for _ in range(n)] for _ in range(n)]

dict_theif_direct = {}
dx_theif = [0,1,0,-1]
dy_theif = [1,0,-1,0]
arrive_theif = []

dx_sul_direct = [-1, 0, 1, 0]
dy_sul_direct = [0, 1, 0, -1]

for theif_number in range(1, m+1):
    x,y,d = map(int,sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    # 우좌
    if d == 1:
        dict_theif_direct[theif_number] = 0
    # 하상
    elif d == 2:
        dict_theif_direct[theif_number] = 1
    graph[x][y].append(theif_number)

# 나무 심기
tree_graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(h):
    x, y= map(int, sys.stdin.readline().rstrip().split())
    x, y = x - 1, y - 1
    tree_graph[x][y] = 1

sul_direct = make_sul_mvoe()
sul_x, sul_y = n//2, n//2

def show_info(round, score, see_d):
    print("라운드 : ", round)
    print("도망자 : ", move_theif_list)
    print("점수  ", score)
    print("도둑")
    temp_graph = copy.deepcopy(graph)
    temp_graph[sul_x][sul_y] = "S"
    for g in temp_graph:
        print(g)
    print("술래 : ", [sul_x, sul_y], see_d)
    print(dict_theif_direct)
    print("--------------------")

# show_info(0,0,0)

total_score = 0
for i in range(len(sul_direct)-1):
    round = i + 1
    sul_d = sul_direct[i]
    see_d = sul_direct[i+1]
    move_theif_list = find_move_theif_list()
    graph = move_theif(move_theif_list)
    move_sul(sul_d)
    score = find_theif(see_d, round)
    total_score += score
    # show_info(round, score, see_d)

print(total_score)


"""
5 3 1 200
2 4 1
1 4 2
4 2 1
2 4

5 3 1 3
2 5 1
1 5 2
4 2 1
2 4

"""