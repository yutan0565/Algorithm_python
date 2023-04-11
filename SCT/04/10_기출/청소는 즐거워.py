import sys

def make_move_list():
    move_list = []
    direct = 0
    count = 1
    while 1:
        for _ in range(2):
            for _ in range(count):
                move_list.append(direct)
                if len(move_list) == n*n-1:
                    return move_list
            direct = (direct + 1)%4
        count += 1

def rotation_left(mask):
    new_mask = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_mask[5-1-j][i] = mask[i][j]
    return new_mask

def move_brush(direct):
    global brush_x, brush_y
    brush_x = brush_x + dx[direct]
    brush_y = brush_y + dy[direct]

def make_dust_mask(direct):
    now_mask = dict_mask[direct]
    dust_mask = [[0 for _ in range(5)] for _ in range(5)]
    now_dust = graph[brush_x][brush_y]
    dust_count = 0
    x,y = 0,0
    for i in range(5):
        for j in range(5):
            if now_mask[i][j] != -1:
                dust_mask[i][j] = now_mask[i][j]*now_dust//100
                dust_count += now_mask[i][j]*now_dust//100
            else:
                x,y = i,j
    dust_mask[x][y] = now_dust - dust_count
    return dust_mask

def put_mask(dust_mask):
    global out_dust
    graph[brush_x][brush_y] = 0
    for i in range(5):
        for j in range(5):
            nx = brush_x-2+i
            ny = brush_y-2+j
            if not(0<=nx<n and 0<=ny<n):
                out_dust += dust_mask[i][j]
            else:
                graph[nx][ny] += dust_mask[i][j]

n = int(sys.stdin.readline().rstrip())

graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
move_list = make_move_list()
dx = [0,1,0,-1]
dy = [-1,0,1,0]
mask_0 = [[0,0,2,0,0],[0,10,7,1,0],[5,-1,0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
mask_1 = rotation_left(mask_0)
mask_2 = rotation_left(mask_1)
mask_3 = rotation_left(mask_2)

dict_mask = {0 : mask_0, 1 : mask_1, 2 : mask_2, 3 : mask_3}

brush_x, brush_y = n//2, n//2

out_dust = 0
for direct in move_list:
    # 빗자루 이동
    move_brush(direct)
    # 마스크 생성
    dust_mask = make_dust_mask(direct)
    # 마스크 씌우기
    put_mask(dust_mask)

print(out_dust)