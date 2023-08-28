import sys
from collections import defaultdict

def move_people():
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for num in range(1, m+1):
        if live_people[num] == 1:
            x,y = dict_pos[num]
            now_direct = dict_direct[num]
            direct_list = dict_candi_direct[num][now_direct]

            stop_flag = 0
            # 독접 계약 없는 칸 찾아서 이동
            for new_d in direct_list:
                nx = x + dx[new_d]
                ny = y + dy[new_d]
                if 0<=nx<n and 0<=ny<n:
                    if graph_mine[nx][ny] == [-1,-1]:
                        dict_pos[num] = [nx,ny]
                        dict_direct[num] = new_d
                        new_graph[nx][ny].append(num)
                        stop_flag = 1
                        break
            if stop_flag == 0:
                # 본인이 독접 계약한 땅으로 이동
                for new_d in direct_list:
                    nx = x + dx[new_d]
                    ny = y + dy[new_d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph_mine[nx][ny][0] == num:
                            dict_pos[num] = [nx, ny]
                            dict_direct[num] = new_d
                            new_graph[nx][ny].append(num)
                            break
    return new_graph

def del_dual():
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) == 1:
                num = graph[i][j][0]
                graph_mine[i][j] = [num,k]
            elif len(graph[i][j]) >= 2:
                candi_num = graph[i][j]
                candi_num.sort()
                small_num = candi_num[0]
                graph[i][j] = [small_num]
                graph_mine[i][j] = [small_num, k]
                for del_num in candi_num:
                    if del_num != small_num:
                        live_people[del_num] = 0

def down_mine():
    for i in range(n):
        for j in range(n):
            if graph_mine[i][j] != [-1,-1]:
                graph_mine[i][j][1] -= 1
                if graph_mine[i][j][1] == -1:
                    graph_mine[i][j] = [-1,-1]

n,m,k = map(int,sys.stdin.readline().rstrip().split())
dict_pos = defaultdict(lambda :[])
dict_direct = {}
dict_candi_direct = defaultdict(lambda :[])
live_people = [0 for _ in range(m+1)]
graph = [[[] for _ in range(n)] for _ in range(n)]
graph_mine = [[[-1,-1] for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if temp[j] >= 1:
            num = temp[j]
            graph[i][j].append(num)
            dict_pos[num] = [i,j]
            graph_mine[i][j] = [num, k]
            live_people[num] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

start_direct = list(map(int,sys.stdin.readline().rstrip().split()))
for num in range(1,m+1):
    dict_direct[num] = start_direct[num-1] - 1

for num in range(1,m+1):
    for _ in range(4):
        a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
        dict_candi_direct[num].append([a-1,b-1,c-1,d-1])

turn  = 1
while 1:
    # 계약 일수 감소
    down_mine()
    # 한칸 이동
    graph = move_people()
    # 이중 제거 / 계약 진행
    del_dual()
    # print("턴 : ",turn)
    # for g in graph:
    #     print(g)
    # print()
    # for g in graph_mine:
    #     print(g)
    # print(live_people)
    # print("=======================")
    if sum(live_people) == 1 and live_people[1] == 1:
        break
    if turn == 1001:
        turn = -1
        break
    else:
        turn += 1
print(turn)