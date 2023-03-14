import copy
import sys


def move_people():
    new_graph = [[0 for _ in range(n)] for _ in range(n)]
    new_info_graph = copy.deepcopy(info_graph)
    for  i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                people_number = graph[i][j]
                now_direct = dict_now[people_number]
                list_new_direct = dict_next_direct[people_number][now_direct]
                move_flag = -1
                # 계약 안된 땅 있나 돌아보기
                for nd in list_new_direct:
                    nx = i + dx[nd]
                    ny = j + dy[nd]
                    if 0<=nx<n and 0<=ny<n:
                        if info_graph[nx][ny] == [-1,-1]:
                            if new_graph[nx][ny] == 0:
                                new_graph[nx][ny] = people_number
                                new_info_graph[nx][ny] = [people_number, k]
                                dict_now[people_number] = nd
                                move_flag = 1
                                break
                            else:
                                # 내가 더 작음
                                if people_number < new_graph[nx][ny]:
                                    dead_number = new_graph[nx][ny]
                                    dict_arrive[dead_number] = 1
                                    new_graph[nx][ny] = people_number
                                    new_info_graph[nx][ny] = [people_number, k]
                                    dict_now[people_number] = nd
                                    move_flag = 1
                                    break
                                else:
                                    dict_arrive[people_number] = 1
                                    move_flag = 1
                                    break
                # 내가 계약한 곳 둘러 보기
                if move_flag == -1:
                    for nd in list_new_direct:
                        nx = i + dx[nd]
                        ny = j + dy[nd]
                        if 0 <= nx < n and 0 <= ny < n:
                            if info_graph[nx][ny][0] == people_number:
                                new_graph[nx][ny] = people_number
                                new_info_graph[nx][ny] = [people_number, k]
                                dict_now[people_number] = nd
                                break
    return new_graph, new_info_graph

def check_arrive():
    if dict_arrive[1] == 1:
        return 1
    for number in range(2, m + 1):
        if dict_arrive[number] == -1:
            return 0
    return -1

def down_mine():
    for  i in range(n):
        for j in range(n):
            if info_graph[i][j] != [-1,-1]:
                info_graph[i][j][1] -= 1
                if info_graph[i][j][1] == -1:
                    info_graph[i][j] = [-1, -1]

n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
info_graph = [[[-1,-1] for _ in range(n)] for _ in range(n)]

# 위, 아래, 왼, 오
dx = [-1,1,0,0]
dy = [0,0,-1,1]

dict_arrive = {}

dict_now = {}
temp_direct = list(map(int, sys.stdin.readline().rstrip().split()))
for number in range(1, m+1):
    dict_arrive[number] = -1
    dict_now[number] = temp_direct[number-1] -1

# 초기 세팅
for  i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            people_number = graph[i][j]
            now_direct = dict_now[people_number]
            info_graph[i][j] = [people_number, k]
dict_next_direct = {}
for number in range(1, m+1):
    dict_next_direct[number] = []
    for _ in range(4):
        z,x,c,v  =map(int, sys.stdin.readline().rstrip().split())
        z, x, c, v = z-1,x-1,c-1,v-1
        dict_next_direct[number].append([z, x, c, v ])

result = 0

def show_graph():
    for g in graph:
        print(g)

def show_info():
    for g in info_graph:
        print(g)

while 1:
    result += 1


    # 점유 취소
    down_mine()
    if result == 1001:
        result = -1
        break
    # 한칸 이동
    graph, info_graph = move_people()

    flag = check_arrive()
    if flag == 1:
        result = -1
        break
    elif flag == -1:
        break
print(result)