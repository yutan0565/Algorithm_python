import sys
from collections import deque, defaultdict

def bfs(x,y,group_num):
    q = deque()
    q.append([x,y])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1

    while q:
        a,b = q.popleft()
        graph_group[a][b] = group_num
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] != 0:
                    if visited[nx][ny] == -1:
                        if graph_group[nx][ny] == 0:
                            q.append([nx,ny])
                            visited[nx][ny] = 1

def find_group():
    group_num = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                if graph_group[i][j] == 0:
                    group_num += 1
                    bfs(i,j,group_num)
    return group_num

def find_head_body_tail():
    # 1 머리, 2 몸, 3 꼬리
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                now_group_num = graph_group[i][j]
                body_list = []
                dict_head[now_group_num] = [i,j]
                visited[i][j] = 1
                # 4개 방향 탐색
                # body 부터 찾기
                x, y = i, j
                while 1:
                    body_flag = False
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0<=nx<n and 0<=ny<n:
                            if visited[nx][ny] == -1:
                                if graph[nx][ny] == 2:
                                    if graph_group[nx][ny] == now_group_num:
                                        body_list.append([nx,ny])
                                        visited[nx][ny] = 1
                                        body_flag = True
                                        x,y = nx,ny
                                        break
                    # 더이상 몸통이 없으면 그만
                    if body_flag == False:
                        break
                dict_body[now_group_num] = body_list
                # 꼬리 찾기
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if visited[nx][ny] == -1:
                            if graph[nx][ny] == 3:
                                if graph_group[nx][ny] == now_group_num:
                                    dict_tail[now_group_num] = [nx,ny]
                                    break

def show_info():
    show_graph = [[0 for _ in range(n)] for _ in range(n)]
    for g_num in dict_head.keys():
        x,y = dict_head[g_num]
        show_graph[x][y] = 1
        x,y = dict_tail[g_num]
        show_graph[x][y] = 3
        for x,y in dict_body[g_num]:
            show_graph[x][y] = 2
    for g in show_graph:
        print(g)
    print("점수 : ", total_score)

def make_drow_pos_list():
    drow_pos_list = []
    for row in range(n):
        drow_pos_list.append([row,0,0])
    for col in range(n):
        drow_pos_list.append([n-1,col,1])
    for row in range(n-1,-1,-1):
        drow_pos_list.append([row,n-1,2])
    for col in range(n-1,-1,-1):
        drow_pos_list.append([0,col,3])

    while 1:
        if len(drow_pos_list) >= k:
            return drow_pos_list[:k]
        else:
            drow_pos_list = drow_pos_list + drow_pos_list

def move_group(g_num):
    x,y = dict_head[g_num]
    # 몸통이 있는 경우
    if len(dict_body[g_num]) != 0:
        # body가 아닌 곳으로 이동
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph_group[nx][ny] == g_num:
                    if [nx, ny] not in dict_body[g_num]:
                        dict_head[g_num] = [nx, ny]
                        break

        now_body_list = dict_body[g_num]
        new_body_list = [[x,y]] + now_body_list[:-1]
        dict_body[g_num] = new_body_list
        dict_tail[g_num] = now_body_list[-1]
    # 몸통이 없는 경우
    else:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph_group[nx][ny] == g_num:
                    if [nx, ny] != dict_tail[g_num]:
                        dict_head[g_num] = [nx, ny]
                        break
        dict_tail[g_num] = [x,y]

def switch_head_tail(g_num):
    dict_head[g_num],dict_tail[g_num] = dict_tail[g_num], dict_head[g_num]
    new_body = []
    for idx in range(len(dict_body[g_num]) -1,-1,-1):
        new_body.append(dict_body[g_num][idx])
    dict_body[g_num] = new_body

def drow_ball(x,y,direct):
    global total_score
    for _ in range(n):
        for g_num in dict_head.keys():
            if [x,y] == dict_head[g_num]:
                total_score += (1*1)
                switch_head_tail(g_num)
                return
            elif [x,y] == dict_tail[g_num]:
                score = len(dict_body[g_num]) + 2
                total_score += (score * score)
                switch_head_tail(g_num)
                return
            else:
                if dict_body[g_num] != []:
                    for idx in range(len(dict_body[g_num])):
                        if [x,y] == dict_body[g_num][idx]:
                            score = idx + 2
                            total_score += (score * score)
                            switch_head_tail(g_num)
                            return
        x = x + dx[direct]
        y = y + dy[direct]


def simulation():
    for turn in range(1, k+1):
        idx = turn - 1
        # 사람 이동
        for g_num in dict_head.keys():
            move_group(g_num)
        # 공 던지기
        drow_x,drow_y,direct = drow_pos_list[idx]
        drow_ball(drow_x,drow_y,direct)


# n 격자 크기, m 팀의 개수, k 라운드 수
n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_group = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

dict_head = defaultdict(lambda  : [-1,-1])
dict_body = defaultdict(lambda  : [])
dict_tail = defaultdict(lambda  : [-1,-1])
total_score = 0

total_group = find_group()
find_head_body_tail()
drow_pos_list = make_drow_pos_list()

simulation()
print(total_score)


"""
7 2 1
2 2 1 0 0 0 0
2 0 3 0 2 1 4
2 2 2 0 2 0 4
0 0 0 0 3 0 4
0 0 4 4 4 0 4
0 0 4 0 0 0 4
0 0 4 4 4 4 4
"""

