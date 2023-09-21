import sys
from collections import deque
from collections import defaultdict


def get_who_graph():
    for i in range(n):
        for j in range(n):
            # 사람이 있는 경우
            if graph_pos[i][j] != []:
                graph_who[i][j] = [graph_pos[i][j][0], k+1]

def move_all_people():
    global graph_pos, graph_who, direct_dict

    new_graph_pos = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 사람이 있는 경우
            if graph_pos[i][j] != []:
                for num in graph_pos[i][j]:
                    now_direct = direct_dict[num]
                    now_candi_direct_list = candi_direct_dict[num][now_direct]
                    # 아무도 계약 안한 곳 먼저 찾기
                    move_flag = False

                    for d in now_candi_direct_list:
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0<=nx<n and 0<=ny<n:
                            # 계약한 사람이 없는 경우
                            if graph_who[nx][ny][0] == 0:
                                move_flag = True
                                new_graph_pos[nx][ny].append(num)
                                direct_dict[num]  = d
                                break

                    # 못찾으면, 본인이 계약한 곳으로 가기
                    if move_flag == False:
                        for d in now_candi_direct_list:
                            nx = i + dx[d]
                            ny = j + dy[d]
                            if 0 <= nx < n and 0 <= ny < n:
                                # 계약한 사람이 없는 경우
                                if graph_who[nx][ny][0] == num:
                                    new_graph_pos[nx][ny].append(num)
                                    direct_dict[num] = d
                                    break
    graph_pos = new_graph_pos

def make_one_graph():
    global graph_pos, graph_who, direct_dict

    new_graph_pos = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 사람이 있는 경우
            if graph_pos[i][j] != []:
                temp_list = graph_pos[i][j]
                temp_list.sort()
                new_graph_pos[i][j].append(temp_list[0])
                for del_num in temp_list[1:]:
                    live_list[del_num] = 0
    graph_pos = new_graph_pos

def down_graph_who():
    global graph_pos, graph_who, direct_dict
    for i in range(n):
        for j in range(n):
            if graph_who[i][j] != [0,0]:
                graph_who[i][j][1] -= 1
                # 점유 끝인 경우
                if graph_who[i][j][1] == 0:
                    graph_who[i][j] = [0,0]

def show_graph():
    print("======pos=======")
    for g in graph_pos:
        print(g)
    print("======who=======")
    for g in graph_who:
        print(g)
    print()

def simulation():

    result = 0
    while(1):
        result += 1
        if result == 1001:
            return -1

        # 각 플레이어들 한칸씩 이동
        move_all_people()
        # 여러명이 있는 칸, 한사람만 남기기
        make_one_graph()
        # 계약 진행 하기
        get_who_graph()
        # 독접 계약 줄어들기
        down_graph_who()

        # print("turn : ", result)
        # show_graph()

        # 1번만 남고, 나머지는 죽으면 끝
        if sum(live_list) == 1 and live_list[1] == 1:
            return result



n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph_pos = [[[] for _ in range(n)] for _ in range(n)]
pos_dict = {}
graph_who = [[[0,0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if temp[j] != 0:
            graph_pos[i][j].append(temp[j])
            pos_dict[temp[j]] = [i,j]
            graph_who[i][j] = [temp[j], k]



direct_dict = {}
temp = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(1, m+1):
    direct_dict[i] = temp[i-1] -1

candi_direct_dict = {}
for num in range(1,m+1):
    candi_direct_dict[num] = {}
    for i in range(4):
        a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
        candi_direct_dict[num][i] = [a-1, b-1, c-1, d-1]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

live_list = [1 for _ in range(m+1)]
live_list[0] = 0

# print("시작")
# show_graph()
result = simulation()
print(result)
