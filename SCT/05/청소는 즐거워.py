import sys

def rotate_left(sub_map):
    new_sub_map = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_sub_map[5-1-j][i] = sub_map[i][j]
    return new_sub_map

def make_move_list():
    move_list = []

    cnt = 1
    now_direct = 0
    while 1:
        for _ in range(2):
            for _ in range(cnt):
                move_list.append(now_direct)
                if len(move_list) == n*n-1:
                    return move_list
            now_direct = (now_direct + 1)%4
        cnt += 1
    return move_list

def make_dust_map(sub_map):
    dust_map = [[0 for _ in range(5)] for _ in range(5)]
    center_dust = graph[x][y]
    graph[x][y] = 0
    al_x,al_y = 0,0
    use_dust = 0

    for i in range(5):
        for j in range(5):
            if sub_map[i][j] == -1:
                al_x = i
                al_y = j
            else:
                dust_map[i][j] = sub_map[i][j]*center_dust//100
                use_dust += dust_map[i][j]
    dust_map[al_x][al_y] = center_dust - use_dust
    return dust_map

def sum_map_to_graph(dust_map):
    global out_dust
    for i in range(5):
        for j in range(5):
            nx = x - 2 + i
            ny = y -2 + j
            # 범위 안
            if 0<=nx<n and 0<=ny<n:
                graph[nx][ny] += dust_map[i][j]
            # 범위 밖
            else:
                out_dust += dust_map[i][j]

def simulation():
    global x,y
    for now_d in move_list:
        # 빗자루 이동
        x = x + dx[now_d]
        y = y + dy[now_d]
        now_sub_map = sub_map_list[now_d]
        # 먼지 map 만들기
        now_dust_map = make_dust_map(now_sub_map)
        # 먼지 map 씌우기
        sum_map_to_graph(now_dust_map)
    return

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
out_dust = 0
x,y = n//2, n//2

dx = [0,1,0,-1]
dy = [-1,0,1,0]

sub_map_list = []
sub_map_0 = [[0,0,2,0,0],
           [0,10,7,1,0],
           [5,-1,0,0,0],
           [0,10,7,1,0],
           [0,0,2,0,0]]
sub_map_list.append(sub_map_0)
sub_map_1 = rotate_left(sub_map_0)
sub_map_list.append(sub_map_1)
sub_map_2 = rotate_left(sub_map_1)
sub_map_list.append(sub_map_2)
sub_map_3 = rotate_left(sub_map_2)
sub_map_list.append(sub_map_3)

move_list = make_move_list()

simulation()
print(out_dust)

