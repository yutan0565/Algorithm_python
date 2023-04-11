import sys

dx_magic = [-1,1,0,0]
dy_magic = [0,0,-1,1]

def make_line():
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    visited_line = [[0 for _ in range(n)] for _ in range(n)]

    direct_index = 0
    move_count = 1
    visit_number = -1
    x,y = n//2, n//2
    visited_line[x][y] = visit_number

    while 1:
        for _ in range(2):
            for _ in range(move_count):
                visit_number += 1
                nx = x + dx[direct_index]
                ny = y + dy[direct_index]
                visited_line[nx][ny] = visit_number
                x,y = nx,ny
                if nx == 0 and ny == 0:
                    return visited_line
            direct_index = (direct_index +1 ) %4
        move_count += 1

def make_sort_ball_list():
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    direct_index = 0
    move_count = 1

    sort_ball_list = []
    x = n//2
    y = n//2
    while 1:
        for _ in range(2):
            for _ in range(move_count):
                nx = x + dx[direct_index]
                ny = y + dy[direct_index]
                if not(0 <= nx < n and 0 <= ny < n):
                    return sort_ball_list
                if graph[nx][ny] == 0:
                    return sort_ball_list
                sort_ball_list.append(graph[nx][ny])
                x,y = nx,ny
            direct_index = (direct_index +1 ) %4
        move_count += 1

def magic_bli():
    del_index_list = []
    for i in range(1, speed+1):
        nx = shark_x + dx_magic[direct]*i
        ny = shark_y + dy_magic[direct]*i
        if visited_line[nx][ny] < len(sort_ball_list):
            del_index_list.append(visited_line[nx][ny])
    del_count = 0
    for index in del_index_list:
        del sort_ball_list[index - del_count]
        del_count += 1

def maigc_bomb():
    if len(sort_ball_list) == 0:
        return 1
    cont_list = []
    cont_value = sort_ball_list[0]
    cont_list.append(0)
    del_index_list = []
    for i in range(1, len(sort_ball_list)):
        if sort_ball_list[i] == cont_value:
            cont_list.append(i)
            # 마지막꺼에서 계속 같은거만 나온 경우 고려
            if i == len(sort_ball_list) -1 :
                if len(cont_list) >= 4:
                    del_index_list = del_index_list + cont_list
        elif sort_ball_list[i] != cont_value:
            # 연속 된 값이, 4개 이상인 경우
            if len(cont_list) >= 4:
                del_index_list = del_index_list + cont_list
            cont_value = sort_ball_list[i]
            cont_list = [i]
            # 마지막꺼에서 계속 같은거만 나온 경우 고려
            if i == len(sort_ball_list) -1 :
                if len(cont_list) >= 4:
                    del_index_list = del_index_list + cont_list
    del_count = 0
    for index in del_index_list:
        dict_del_bomb[sort_ball_list[index - del_count]] += 1
        del sort_ball_list[index - del_count]
        del_count += 1
    if len(del_index_list) == 0:
        return 1

def make_group():
    if len(sort_ball_list) == 0:
        return []

    cont_list = []
    cont_value = sort_ball_list[0]
    cont_list.append(0)
    new_sort_ball_list = []
    for i in range(1, len(sort_ball_list)):
        if sort_ball_list[i] == cont_value:
            cont_list.append(i)
            if i == len(sort_ball_list) - 1:
                a = len(cont_list)
                b = cont_value
                new_sort_ball_list = new_sort_ball_list + [a, b]
        elif sort_ball_list[i] != cont_value:
            # 지금까지 쌓인거 처리
            a = len(cont_list)
            b = cont_value
            new_sort_ball_list = new_sort_ball_list + [a,b]
            if len(new_sort_ball_list) > n**2 - 1:
                return new_sort_ball_list[:n**2 - 1]

            #새로 시작
            cont_value = sort_ball_list[i]
            cont_list = [i]
            # 마지막꺼 처리는 따로 해주기
            if i == len(sort_ball_list) - 1:
                a = len(cont_list)
                b = cont_value
                new_sort_ball_list = new_sort_ball_list + [a, b]

    if len(new_sort_ball_list) > n**2 - 1:
        return new_sort_ball_list[:n**2 - 1]

    return new_sort_ball_list

n,m = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

visited_line = make_line()
sort_ball_list = make_sort_ball_list()

shark_x,shark_y = n//2, n//2

dict_del_bomb = {}
for i in range(1,4):
    dict_del_bomb[i] = 0

for _ in range(m):
    d,s = map(int,sys.stdin.readline().rstrip().split())
    direct,speed = d-1, s
    # 블리자드 마법을 통해, 해당 방향으로 구슬 파괴

    magic_bli()

    # 구슬 폭발
    while 1:
        flag = maigc_bomb()
        if flag == 1:
            break
    # 그룹 만들기
    sort_ball_list = make_group()
    if len(sort_ball_list) == 0:
        break
result = dict_del_bomb[1] + 2*dict_del_bomb[2] + 3*dict_del_bomb[3]
print(result)

"""
5 1
0 0 0 0 0
0 0 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0
1 2

5 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 2

5 2
0 0 0 0 0
0 0 0 0 0
0 2 0 0 0
0 2 2 0 0
0 0 0 0 0
1 2
1 2

"""