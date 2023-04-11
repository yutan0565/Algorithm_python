import copy
import sys

def make_sul_move_list():
    sul_move_list = []
    max_len = n*n-1

    direct = 0
    count = 1
    while 1:
        for _ in range(2):
            for _ in range(count):
                sul_move_list.append(direct)
            direct = (direct + 1)%4
        count += 1
        if len(sul_move_list) >= max_len:
            sul_move_list = sul_move_list[:max_len]
            break

    reverse_sul_move_list = []
    for d in sul_move_list:
        reverse_sul_move_list = [(d+2)%4] + reverse_sul_move_list

    sul_move_list = sul_move_list + reverse_sul_move_list

    while 1:
        if len(sul_move_list) > k:
            return sul_move_list[:k+1]
        else:
            sul_move_list = sul_move_list + sul_move_list

def move_theif():
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 도둑이 있는
            if len(graph[i][j]) >= 1:
                # 술래랑 거리 3 이하
                if abs(sul_x-i) + abs(sul_y-j) <= 3:
                    direct_list = graph[i][j]
                    for d in direct_list:
                        new_d = d
                        nx = i + dx[new_d]
                        ny = j + dy[new_d]
                        if not(0<=nx<n and 0<=ny<n):
                            new_d = (d+2)%4
                            nx = i + dx[new_d]
                            ny = j + dy[new_d]
                        # 술래 있음
                        if [nx,ny] == [sul_x,sul_y]:
                            new_graph[i][j].append(new_d)
                        # 술래 없음
                        else:
                            new_graph[nx][ny].append(new_d)
                else:

                    new_graph[i][j]  = new_graph[i][j] + graph[i][j]
    return new_graph

def move_sul(now_see):
    global  sul_x, sul_y
    sul_x = sul_x + dx_sul[now_see]
    sul_y = sul_y + dy_sul[now_see]

def find_theif(next_see, turn):
    global total_score
    x,y = sul_x,sul_y
    count = 0
    for _ in range(3):
        if not(0<=x<n and 0<=y<n):
            break
        if graph_tree[x][y] == 0:
            if graph[x][y] != []:
                count += len(graph[x][y])
                graph[x][y] = []
        x = x + dx_sul[next_see]
        y = y + dy_sul[next_see]
    total_score += (turn*count)

# 크기 , 도망자 수 , h개의 나무, k개의 턴
n,m,h,k = map(int,sys.stdin.readline().rstrip().split())
graph  = [[[] for _ in range(n)] for _ in range(n)]
graph_tree = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

dx_sul = [-1, 0, 1, 0]
dy_sul = [0, 1, 0, -1]
sul_x, sul_y = n//2,n//2

sul_move_list = make_sul_move_list()

for num in range(1,m+1):
    x,y,type = map(int,sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    # 우 좌
    if type == 1:
        graph[x][y].append(0)
    # 하 상
    elif type == 2:
        graph[x][y].append(1)

for _ in range(h):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    graph_tree[x][y] = 1


total_score = 0
for turn in range(1,k+1):
    # 도망자 이동
    graph = move_theif()
    # 술래 이동
    now_see = sul_move_list[turn-1]
    next_see = sul_move_list[turn]
    move_sul(now_see)

    # 도둑 찾고 지우기
    find_theif(next_see, turn)

print(total_score)

"""
5 3 1 10
2 5 1
1 5 2
4 2 1
2 4

"""