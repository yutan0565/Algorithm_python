import sys
from collections import deque

def bfs(x,y, visited, group_num):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    graph_group[x][y] = group_num

    while q:
        a,b = q.popleft()
        if graph_people[a][b] == 1:
            dict_head[group_num] = [a,b]
        elif graph_people[a][b] == 3:
            dict_tail[group_num] = [a,b]
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph_people[nx][ny] != 0:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        graph_group[nx][ny] = group_num

def make_group():
    visited = [ [ -1 for _ in range(n)] for _ in range(n)]
    group_num = 1
    for i in range(n):
        for j in range(n):
            if graph_people[i][j] != 0:
                if visited[i][j] == -1:
                    bfs(i,j, visited, group_num)
                    group_num += 1

def find_other_people(num):
    now_head = dict_head[num]
    x,y= now_head
    now_tail = dict_tail[num]
    dict_other[num] = []

    visit_pos = [[x,y]]
    stop_flag = 0
    # 꼬리가 나올때까지 head 부터, 추가 해주기
    while 1:

        other_flag = 0
        # other가 먼저 있나 확인 해야함
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if [nx,ny] not in visit_pos:
                    # 중간 사람이 나오는 경우
                    if graph_people[nx][ny] == 2:
                        dict_other[num].append([nx,ny])
                        visit_pos.append([nx,ny])
                        other_flag = 1
                        x,y = nx,ny
                        break
        #   other 가 없는 경우 // 꼬리 찾기
        if other_flag == 0:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if [nx, ny] not in visit_pos:
                        # 꼬리 찾기
                        if graph_people[nx][ny] == 3:
                            stop_flag = 1
                            break
        if stop_flag == 1:
            break

def make_drow_candi_list():
    drow_candi_list = []
    for row in range(n):
        drow_candi_list.append([[row,0],0])
    for col in range(n):
        drow_candi_list.append([[n-1,col],1])
    for row in range(n-1,-1,-1):
        drow_candi_list.append([[row,n-1],2])
    for col in range(n-1,-1,-1):
        drow_candi_list.append([[0,col],3])

    while 1:
        if len(drow_candi_list) > k:
            break
        else:
            drow_candi_list = drow_candi_list + drow_candi_list
    return drow_candi_list[:k]

def move_people(num):
    # other가 있는 경우
    if len(dict_other[num]) != 0:
        # 머리 먼저 이동
        x,y = dict_head[num]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph_group[nx][ny] == num:
                    # other 가 없는 다른 방향으로 지나 가기
                    if [nx,ny] not in dict_other[num]:
                        dict_head[num] = [nx,ny]
                        break
        # ohter 이동
        # 머리하고 가까운거 부터 업데이트
        for i in range(len(dict_other[num])):
            temp_x, temp_y = dict_other[num][i]
            dict_other[num][i] = [x,y]
            x,y = temp_x, temp_y
        # 꼬리 이동
        dict_tail[num] = [x,y]

    # 머리하고 꼬리만 있는 경우
    else:
        # 머리 먼저 이동
        x,y = dict_head[num]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph_group[nx][ny] == num:
                    # 꼬리가 없는 다른 방향으로 지나 가기
                    if [nx,ny] not in dict_tail[num]:
                        dict_head[num] = [nx,ny]
                        break
        # 꼬리 이동 해쥑
        dict_tail[num] = [x,y]

def reverse_list(list):
    new_list = []
    for i in range(len(list)-1, -1, -1):
        new_list.append(list[i])
    return new_list

def switch_head_tail(num):
    dict_head[num], dict_tail[num] = dict_tail[num], dict_head[num]
    dict_other[num] = reverse_list(dict_other[num])

def drow_ball(drow_start, drow_direct):
    x,y = drow_start
    # 한칸씩 공 이동하면서 확인
    for mul in range(n):
        nx = x + dx[drow_direct]*mul
        ny = y + dy[drow_direct]*mul
        num = graph_group[nx][ny]
        # 지금 있는 곳에 그룹에 속하는 곳이면
        if num != 0:
            # 그리고 사람이 있다면
            #머리
            if [nx,ny] == dict_head[num]:
                dict_score[num] += 1
                switch_head_tail(num)
                break
            # 중간
            elif [nx,ny] in dict_other[num]:
                for index in range(len(dict_other[num])):
                    if [nx,ny] == dict_other[num][index]:
                        dict_score[num] += (index+2)*(index+2)
                        break
                switch_head_tail(num)
                break
            # 꼬리
            elif [nx,ny]  ==  dict_tail[num]:
                dict_score[num] += (2 + len(dict_other[num]))*(2 + len(dict_other[num]))
                switch_head_tail(num)
                break
        else:
            continue

n,m,k= map(int,sys.stdin.readline().rstrip().split())
graph_people = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_group = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 0 빈칸 / 1 머리 / 2 나머지 / 3 꼬리
# 그룹 만들기
dict_head = {}
dict_other = {}
dict_tail = {}
dict_score = {}
make_group()

# 가운데 낀 사람들 찾기
for num in range(1, m+1):
    find_other_people(num)
    dict_score[num] = 0  # 점수 초기화

# 공 던지는 위치 / 방향 저장 list 만들기
drow_candi_list = make_drow_candi_list()

def show_info():
    temp_graph = [[ 0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_group[i][j] != 0:
                temp_graph[i][j] = 4
    for num in range(1, m+1):
        x,y  = dict_head[num]
        temp_graph[x][y] = 1
        for x,y in dict_other[num]:
            temp_graph[x][y] =2
        x,y = dict_tail[num]
        temp_graph[x][y] = 3
    for g in temp_graph:
        print(g)
# print("처음")
# show_info()
for round in range(1, k+1):
    index = round - 1
    drow_start = drow_candi_list[index][0]
    drow_direct = drow_candi_list[index][1]
    # 모든 사람들 이동
    for num in range(1, m+1):
        move_people(num)
    # 공 던지기 시작
    drow_ball(drow_start, drow_direct)

    # print("===================")
    # print("던진 곳 : ", drow_start)
    # show_info()
    # print(dict_head)
    # print(dict_other)
    # print(dict_tail)



print(sum(dict_score.values()))
"""
7 3 5
3 2 1 0 0 0 0
4 0 4 0 2 1 4
4 4 4 0 2 0 4
0 0 0 0 3 4 4
2 1 3 2 0 0 0
2 0 0 2 0 0 0
2 2 2 2 0 0 0

"""