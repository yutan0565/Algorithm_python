import sys

def make_brush_move():
    brush_move_x, brush_move_y, brush_direct = [], [], []
    """
     0 1  2 2 3 3 0 0 0
    """
    index = 0
    count = 1
    while 1:
        for _ in range(2):
            for _ in range(count):
                brush_move_x.append(dx[index])
                brush_move_y.append(dy[index])
                brush_direct.append(index)
                if len(brush_move_y) == n*n -1:
                    return brush_move_x, brush_move_y, brush_direct
            index  = (index + 1)%4
        count += 1

def rotation_left(mask):
    new_mask = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_mask[5-1-j][i] = mask[i][j]
    return new_mask

def make_dust_move_mask(dust, dust_mask):
    new_mask = [[0 for _ in range(5)] for _ in range(5)]
    c_x,c_y = 0,0
    temp = 0
    for i in range(5):
        for j in range(5):
            if dust_mask[i][j] >= 1:
                new_mask[i][j] = dust_mask[i][j] * dust // 100
                temp += new_mask[i][j]
            elif dust_mask[i][j] == -1:
                c_x,c_y = i,j
    new_mask[c_x][c_y] = dust - temp
    return new_mask

def move_brush():
    out_dust = 0
    x,y = n//2, n//2
    for i in range(len(brush_direct)):
        x = x + brush_move_x[i]
        y = y + brush_move_y[i]
        direct = brush_direct[i]
        dust_mask = dust_mask_list[direct]
        dust_move_mask = make_dust_move_mask(graph[x][y], dust_mask)
        for i in range(5):
            for j in range(5):
                nx = x + (i-2)
                ny = y + (j-2)
                if 0<=nx<n and 0<=ny<n:
                    graph[nx][ny] += dust_move_mask[i][j]
                else:
                    out_dust += dust_move_mask[i][j]
    return out_dust
n = int(sys.stdin.readline().rstrip())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]
brush_move_x, brush_move_y, brush_direct = make_brush_move()

dust_mask_0 = [[0,0,2,0,0],
             [0,10,7,1,0],
             [5,-1,0,0,0],
             [0,10,7,1,0],
             [0,0,2,0,0]
             ]
dust_mask_1 = rotation_left(dust_mask_0)
dust_mask_2 = rotation_left(dust_mask_1)
dust_mask_3 = rotation_left(dust_mask_2)
dust_mask_list = [dust_mask_0, dust_mask_1, dust_mask_2, dust_mask_3]

result = move_brush()
print(result)