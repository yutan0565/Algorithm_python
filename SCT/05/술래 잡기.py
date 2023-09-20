import copy
import sys

def make_sul_direct_list():
    sul_direct_list = []
    now_direct = 0
    cnt = 1
    while 1:
        for _ in range(2):
            for _ in range(cnt):
                sul_direct_list.append(now_direct)
                if len(sul_direct_list) == n*n -1:
                    reverse_sul_direct_list = []
                    for i in range(len(sul_direct_list)-1,-1,-1):
                        reverse_sul_direct_list.append((sul_direct_list[i]+2)%4)
                    sul_direct_list = sul_direct_list + reverse_sul_direct_list
                    # 수행 횟수 == k
                    while 1:
                        if len(sul_direct_list) > k+1:
                            return sul_direct_list[:k+1]
                        else:
                            sul_direct_list = sul_direct_list + sul_direct_list
            now_direct = (now_direct + 1)%4
        cnt += 1

def move_theif():
    global graph_theif
    new_graph_theif = copy.deepcopy(graph_theif)
    # 도둑이 움직이는 구역 찾기
    check_pos_list = []
    center_x = 3
    center_y = 3
    for i in range(7):
        for j in range(7):
            now_dis = abs(center_x-i) + abs(center_y-j)
            if now_dis <= 3:
                nx = sul_x - center_x + i
                ny = sul_y - center_y + j
                if 0<=nx<n and 0<=ny<n:
                    if graph_theif[nx][ny] != []:
                        check_pos_list.append([nx,ny, graph_theif[nx][ny]])
                        new_graph_theif[nx][ny] = []

    for a,b, theif_list in check_pos_list:
        for i in range(len(theif_list)):
            theif_direct = theif_list[i]
            nx = a + dx_theif[theif_direct]
            ny = b + dy_theif[theif_direct]
            # 범위 벗어나는 경우
            if not(0<=nx<n and 0<=ny<n):
                theif_direct  = (theif_direct + 2)%4
                # 원래 에서 뒤로
                nx = a + dx_theif[theif_direct]
                ny = b + dy_theif[theif_direct]
            # 술래가 있는 경우 -> 자기 자리로 돌아오기
            if [nx,ny] == [sul_x,sul_y]:
                nx = a
                ny = b
            new_graph_theif[nx][ny].append(theif_direct)
    graph_theif = new_graph_theif

def move_sul(now_direct):
    global sul_x, sul_y
    sul_x = sul_x + dx_sul[now_direct]
    sul_y = sul_y + dy_sul[now_direct]

def find_theif(now_see, now_turn):
    global total_score
    for i in range(3):
        x = sul_x + i*dx_sul[now_see]
        y = sul_y + i*dy_sul[now_see]
        if 0<=x<n and 0<=y<n:
            if graph_tree[x][y] == 0:
                total_score += (len(graph_theif[x][y])*now_turn)
                graph_theif[x][y] = []

def show_info():
    print("술래 위치 : ", [sul_x,sul_y])
    for g in graph_theif:
        print(g)

def simulation():
    now_turn = 0
    for i in range(k):

        now_turn += 1
        now_direct = sul_direct_list[i]
        now_see = sul_direct_list[i+1]

        # 도망자 움직이기
        move_theif()

        # 술래 움직이기
        move_sul(now_direct)
        # 도둑 잡기
        find_theif(now_see,now_turn)



n,m,h,k = map(int,sys.stdin.readline().rstrip().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
graph_theif = [[[] for _ in range(n)] for _ in range(n)]
graph_tree = [[0 for _ in range(n)] for _ in range(n)]
sul_x = n // 2
sul_y = n // 2

for _ in range(m):
    x,y,d = map(int,sys.stdin.readline().rstrip().split())
    x -= 1
    y -= 1
    # 우 좌
    if d == 1:
        graph_theif[x][y].append(0)
    # 아 위
    elif d == 2:
        graph_theif[x][y].append(1)

for _ in range(h):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    x -= 1
    y -= 1
    graph_tree[x][y] = 1

sul_direct_list = make_sul_direct_list()
dx_sul = [-1,0,1,0]
dy_sul = [0,1,0,-1]

# 우 아 좌 위
dx_theif = [0,1,0,-1]
dy_theif = [1,0,-1,0]

total_score = 0
simulation()

print(total_score)