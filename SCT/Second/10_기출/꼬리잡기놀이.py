import sys
from collections import deque

def bfs(x,y, number,group_graph,  visited):
    q = deque()
    q.append([x,y])
    group_graph[x][y] = number
    visited[x][y] = 1
    while q:
        a,b = q.popleft()
        if graph[a][b] == 1:
            dict_head[number] = [a,b]
        elif graph[a][b] == 3:
            dict_tail[number] = [a,b]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] != 0:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        group_graph[nx][ny] = number

def bfs_make_group():
    group_graph = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    group_num = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and visited[i][j] == -1:
                group_num += 1
                dict_other[group_num] = []
                bfs(i,j, group_num, group_graph, visited)

    return group_graph, group_num

def find_other():
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for group in range(1, group_count+1):
        q = deque()
        x, y = dict_head[group]
        tail = dict_tail[group]
        dict_other[group] = []
        q.append([x,y])
        visited[x][y] = 1
        while q:
            a,b = q.popleft()
            if [a,b] == tail:
                break
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == 2:
                            dict_other[group].append([nx,ny])
                            q.append([nx,ny])
                            visited[nx][ny] = 1
        dict_len[group] = len(dict_other[group]) + 2

def make_drow_ball_list():
    drow_ball_list = []
    while 1:
        for i in range(0,n):
            drow_ball_list.append([[i,0], 0])
        for i in range(0,n):
            drow_ball_list.append([[n-1,i], 1])
        for i in range(n-1,-1,-1):
            drow_ball_list.append([[i,n-1], 2])
        for i in range(n-1,-1,-1):
            drow_ball_list.append([[0,i], 3])
        if len(drow_ball_list) >= k:
            return drow_ball_list[:k]

def reverse_list(list):
    new_list = []
    for i in range(len(list)-1, -1, -1):
        new_list.append(list[i])
    return new_list

def move_people():
    for number in range(1, group_count+1):
        # 현재 헤드 위치
        now_x, now_y = dict_head[number]

        # other 가 없는 경우 따로 해주기
        if len(dict_other[number]) == 0:
            for i in range(4):
                nx = now_x + dx[i]
                ny = now_y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if group_graph[nx][ny] == number:
                        if [nx,ny] != dict_tail[number]:
                            dict_head[number] = [nx,ny]
                            break
            dict_tail[number] = [now_x,now_y]
        else:
            # 머리 이동
            for i in range(4):
                nx = now_x + dx[i]
                ny = now_y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if group_graph[nx][ny] == number:
                        if [nx,ny] != dict_other[number][0]:
                            dict_head[number] = [nx,ny]
                            break
            # other 이동
            for i in range(len(dict_other[number])):
                old_x, old_y = dict_other[number][i]
                dict_other[number][i] = [now_x, now_y]
                now_x,now_y = old_x, old_y

            # tail 이동
            dict_tail[number] = [now_x, now_y]

def change_head_tail(number):
    dict_head[number], dict_tail[number] =  dict_tail[number], dict_head[number]
    dict_other[number] = reverse_list(dict_other[number])

def drow_ball(x,y,direct):
    # 공 위치 옮겨 주면서 확인 하기
    for mul in range(n):
        nx = x + dx[direct]*mul
        ny = y + dy[direct]*mul
        hit_flag = 0
        for number in range(1, group_count+1):
            if [nx,ny] == dict_head[number]:
                change_head_tail(number)
                return 1

            elif [nx,ny] == dict_tail[number]:
                change_head_tail(number)
                return dict_len[number]

            else:
                other_list = dict_other[number]
                for i in range(len(other_list)):
                    other = other_list[i]
                    if [nx, ny] == other:
                        change_head_tail(number)
                        return i + 2
    return 0
a = [1,2,3]

n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 그룹의 헤드와, 꼬리 위치 파악
dict_head = {}
dict_tail = {}
dict_other = {}
dict_len = {}

# 그룹 만들기
group_graph, group_count = bfs_make_group()

# 헤드 / 테일로 other 찾기
find_other()

# 공 던지기 시작 위치 만들기 / 방향
drow_ball_list = make_drow_ball_list()


result = 0
for i in range(k):
    ball_x, ball_y = drow_ball_list[i][0][0], drow_ball_list[i][0][1]
    ball_direct = drow_ball_list[i][1]
    move_people()
    hit_number =  drow_ball(ball_x, ball_y, ball_direct)
    result += (hit_number*hit_number)

print(result)
"""

"""




