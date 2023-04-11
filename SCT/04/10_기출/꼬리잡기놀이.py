import sys
from collections import deque, defaultdict

def bfs(x,y,graph_group,visited,g_num):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    graph_group[x][y] = g_num
    while q:
        a,b = q.popleft()
        if graph[a][b] == 1:
            dict_head[g_num] = [a,b]
        elif graph[a][b] == 3:
            dict_tail[g_num] = [a,b]
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] != 0:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        graph_group[nx][ny] = g_num

def make_group_graph():
    graph_group = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    g_num = 1
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                if visited[i][j] == -1:
                    bfs(i,j,graph_group,visited, g_num)
                    g_num += 1
    return graph_group

def find_other_member():
    for g_num in range(1,m+1):
        x,y = dict_head[g_num]
        move_list = [[x,y]]
        stop_flag = 0
        while 1:
            check_tail = 1
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph_group[nx][ny] == g_num:
                        if [nx,ny] not in move_list:
                            if graph[nx][ny] == 2:
                                dict_other[g_num].append([nx,ny])
                                move_list.append([nx,ny])
                                x,y = nx,ny
                                check_tail = 0
                                break
            if check_tail == 1:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph_group[nx][ny] == g_num:
                            if [nx, ny] not in move_list:
                                if graph[nx][ny] == 3:
                                    stop_flag = 1
                                    break
            if stop_flag == 1:
                break

def make_list_ball_start():
    list_ball_start = []
    for row in range(n):
        list_ball_start.append([row,0,0])
    for col in range(n):
        list_ball_start.append([n-1,col,1])
    for row in range(n-1,-1,-1):
        list_ball_start.append([row,n-1,2])
    for col in range(n-1,-1,-1):
        list_ball_start.append([0,col,3])

    while 1:
        if len(list_ball_start) >= k:
            return list_ball_start[:k]
        else:
            list_ball_start = list_ball_start + list_ball_start

def move_people():
    for g_num in range(1,m+1):
        # other가 없는 경우
        if dict_other[g_num] == []:
            # 머리 이동
            x, y = dict_head[g_num]
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] == 4:
                        if graph_group[nx][ny] == g_num:
                            dict_head[g_num] = [nx,ny]
                            graph[nx][ny] = 1
                            break
            # 꼬리 이동
            nx,ny = x,y
            x,y = dict_tail[g_num]
            dict_tail[g_num] = [nx,ny]
            graph[nx][ny] = 3
            graph[x][y] = 4
        # other가 있는 경우
        else:
            # 머리 이동
            x, y = dict_head[g_num]
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] == 4 or graph[nx][ny] == 3:
                        if graph_group[nx][ny] == g_num:
                            dict_head[g_num] = [nx,ny]
                            graph[nx][ny] = 1
                            break
            # 중간 이동
            nx,ny = x,y
            for i in range(len(dict_other[g_num])):
                x,y = dict_other[g_num][i]
                dict_other[g_num][i] = [nx,ny]
                graph[nx][ny] = 2
                nx,ny = x,y
            # 꼬리 이동
            x,y = dict_tail[g_num]
            dict_tail[g_num] = [nx,ny]
            graph[nx][ny] = 3
            if [x,y] != dict_head[g_num]:
                graph[x][y] = 4

def switch(g_num):
    dict_head[g_num], dict_tail[g_num] = dict_tail[g_num], dict_head[g_num]
    head_x,head_y = dict_head[g_num]
    tail_x,tail_y = dict_tail[g_num]
    graph[head_x][head_y], graph[tail_x][tail_y] = graph[tail_x][tail_y], graph[head_x][head_y]

    if len(dict_other[g_num]) != 0:
        new_other = []
        for x,y in dict_other[g_num]:
            new_other = [[x,y]] + new_other
        dict_other[g_num] = new_other

def drow_ball(x,y,direct):
    global total_score
    while 1:
        g_num = graph_group[x][y]
        if g_num != 0:
            # 머리에 맞음
            if [x,y] == dict_head[g_num]:
                index = 1
                total_score += index*index
                switch(g_num)
                return
            #꼬리에 맞음
            elif [x,y] == dict_tail[g_num]:
                index = 1 + len(dict_other[g_num])+1
                total_score += index*index
                switch(g_num)
                return
            # 중간 맞음
            elif [x,y] in dict_other[g_num]:
                index = 2
                for other_x, other_y in dict_other[g_num]:
                    if [x,y] == [other_x,other_y]:
                        break
                    index += 1
                total_score += index*index
                switch(g_num)
                return
        # 아무것도 안맞음
        x = x + dx[direct]
        y = y + dy[direct]
        if not(0<=x<n and 0<=y<n):
            break

dx = [0,-1,0,1]
dy = [1,0,-1,0]

n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dict_head = defaultdict(lambda : [])
dict_tail = defaultdict(lambda : [])
dict_other = defaultdict(lambda : [])

graph_group = make_group_graph()
find_other_member()
list_ball_start = make_list_ball_start()

total_score = 0
for round in range(1,k+1):
    ball_x, ball_y, direct = list_ball_start[round-1]
    # 한칸 이동하기
    move_people()
    # 공 던지기
    drow_ball(ball_x,ball_y,direct)

print(total_score)



"""
7 2 1
4 3 1 0 0 0 0
4 0 4 0 2 1 4
4 4 4 0 2 0 4
0 0 0 0 3 0 4
0 0 4 4 4 0 4
0 0 4 0 0 0 4
0 0 4 4 4 4 4

"""

