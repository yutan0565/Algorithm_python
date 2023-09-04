import sys
from collections import deque
from collections import defaultdict

def show_info():
    print("------show_info-------")
    for num in range(number_of_group):
        print(num)
        print("dict_head : ", dict_head[num])
        print("dict_body : ", dict_body[num])
        print("dict_tail : ", dict_tail[num])

def bfs_group(x,y):
    q = deque()
    q.append([x,y])
    graph_group[x][y]= number_of_group

    while q:
        a,b = q.popleft()
        # 머리 사람인 경우
        if graph[a][b] == 1:
            dict_head[number_of_group] = [a,b]
        # 꼬리 사람인 경우
        elif graph[a][b] == 3:
            dict_tail[number_of_group] = [a, b]

        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] != 0:
                    if graph_group[nx][ny] == -1:
                        q.append([nx,ny])
                        graph_group[nx][ny]= number_of_group

def make_graph_group():
    global  number_of_group
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                if graph_group[i][j] == -1:
                    bfs_group(i,j)
                    number_of_group += 1

def make_indi_body(now_num):
    x = dict_head[now_num][0]
    y = dict_head[now_num][1]
    while 1:
        # 꼬리가 아닌 부분 먼저 찾기
        find_other = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if graph_group[nx][ny] == now_num:
                    if graph[nx][ny] == 2:
                        if [nx,ny] not in dict_body[now_num]:
                            dict_body[now_num].append([nx,ny])
                            find_other = True
                            x = nx
                            y = ny
                            break
        # 다른 거 못찾은 경우
        if find_other == False:
            return

def make_dict_body():
    for now_num in range(number_of_group):
        make_indi_body(now_num)
    return

def make_ball_pos():
    ball_pos_list = []

    for i in range(n):
        ball_pos_list.append([i,0, 0])
    for i in range(n):
        ball_pos_list.append([n-1,i,1])
    for i in range(n):
        ball_pos_list.append([n-1-i,n-1,2])
    for i in range(n):
        ball_pos_list.append([0,n-1-i,3])

    while 1:
        if len(ball_pos_list) >= k:
            return ball_pos_list[:k]
        ball_pos_list = ball_pos_list + ball_pos_list


def move_people():
    global dict_head, dict_body, dict_tail
    for group_num in range(number_of_group):
        now_head_x = dict_head[group_num][0]
        now_head_y = dict_head[group_num][1]

        now_tail_x = dict_tail[group_num][0]
        now_tail_y = dict_tail[group_num][1]

        # 머리 이동
        # 그룹 내에서 other가 아니고, 꼬리가 아닌 부분으로 이동
        head_move_flag = False
        for d in range(4):
            new_head_x = now_head_x + dx[d]
            new_head_y = now_head_y + dy[d]
            if 0<=new_head_x<n and 0<=new_head_y<n:
                if graph_group[new_head_x][new_head_y] == group_num:
                    if [new_head_x,new_head_y] not in dict_body[group_num]:
                        if [new_head_x,new_head_y] != [now_tail_x, now_tail_y]:
                            head_move_flag = True
                            dict_head[group_num] = [new_head_x, new_head_y]
                            break

        # 이동을 못하는 경우 (꽉차 있는 경우) -> 꼬리 위치로 이동
        if head_move_flag == False:
            for d in range(4):
                new_head_x = now_head_x + dx[d]
                new_head_y = now_head_y + dy[d]
                if 0 <= new_head_x < n and 0 <= new_head_y < n:
                    if graph_group[new_head_x][new_head_y] == group_num:
                        if [new_head_x, new_head_y] == [now_tail_x, now_tail_y]:
                            dict_head[group_num] = [new_head_x, new_head_y]
                            break

        # 몸통 부분 옮겨 주기
        # 몸통이 없는 경우
        if len(dict_body[group_num]) == 0:
            # 꼬리만 원래 머리가 있던 자리롤 옯겨 주기
            dict_tail[group_num] = [now_head_x,now_head_y]
        # 몸통이 있는 경우
        else:
            x = now_head_x
            y = now_head_y

            for i in range(len(dict_body[group_num])):
                # 원래 있던 장소
                ori_x = dict_body[group_num][i][0]
                ori_y = dict_body[group_num][i][1]
                dict_body[group_num][i] = [x,y]
                x = ori_x
                y = ori_y

            # 마지막 꼬리 부분만 바꿔주기
            dict_tail[group_num] = [x,y]

# 방향 전환
def switch_pos(g_num):
    global dict_head, dict_body, dict_tail
    # 머리랑 꼬리 바꾸기
    dict_head[g_num], dict_tail[g_num] = dict_tail[g_num], dict_head[g_num]

    # 가운데 바꾸기
    new_body = []
    for i in range(len(dict_body[g_num])-1,-1,-1):
        new_body.append(dict_body[g_num][i])
    dict_body[g_num] = new_body

def drow_ball(ball_x, ball_y,ball_direct):
    global total_score
    for i in range(n):
        # 공 위치 옮겨 주기
        x  = ball_x + dx[ball_direct]*i
        y  = ball_y + dy[ball_direct]*i
        if not(0<=x<n and 0<=y<n):
            break
        else:
            #머리에 맞는 경우
            for g_num in range(number_of_group):
                if [x,y] == dict_head[g_num]:
                    add_score = 1
                    total_score += (add_score*add_score)
                    switch_pos(g_num)
                    return
            # 꼬리에 맞는 경우
            for g_num in range(number_of_group):
                if [x, y] == dict_tail[g_num]:
                    add_score = (1+len(dict_body[g_num])+1)
                    total_score += (add_score * add_score)
                    switch_pos(g_num)
                    return
            # 중간에 맞는 경우
            for g_num in range(number_of_group):
                for i in range(len(dict_body[g_num])):
                    if [x, y] == dict_body[g_num][i]:
                        add_score = (2+i)
                        total_score += (add_score * add_score)
                        switch_pos(g_num)
                        return

def simulation():

    for i in range(k):
        # 사람 먼저 이동
        move_people()
        # 공 던지기
        ball_x,ball_y,ball_direct = ball_pos_list[i]
        drow_ball(ball_x, ball_y,ball_direct)


n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_group = [[-1 for _ in range(n)] for _ in range(n)]
number_of_group = 0
ball_pos_list = []

dx = [0,-1,0,1]
dy = [1,0,-1,0]

dict_head = {}
dict_body = defaultdict(lambda : [])
dict_tail = {}

total_score = 0

make_graph_group()
make_dict_body()
ball_pos_list = make_ball_pos()

simulation()

print(total_score)

"""
7 2 2
2 2 1 0 0 0 0
2 0 3 0 3 1 4
2 2 2 0 4 0 4
0 0 0 0 4 0 4
0 0 4 4 4 0 4
0 0 4 0 0 0 4
0 0 4 4 4 4 4

7 2 100
3 2 1 0 0 0 0
4 0 4 0 2 1 4
4 4 4 0 2 0 4
0 0 0 0 3 0 4
0 0 4 4 4 0 4
0 0 4 0 0 0 4
0 0 4 4 4 4 4
"""