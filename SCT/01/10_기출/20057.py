import sys

# 좌 아 우 위
dx_direct = [0,1,0,-1]
dy_direct = [-1,0,1,0]
dx = []
dy = []
direct_list = []

def make_root():
    direct_index = 0
    direct_count = 1
    dx = []
    dy = []
    direct_list = []
    while 1:
        for _ in range(2):
            for _ in range(direct_count):
                dx.append(dx_direct[direct_index])
                dy.append(dy_direct[direct_index])
                direct_list.append(direct_index)
                if len(dx) == n**2:
                    return dx,dy,direct_list
            direct_index = (direct_index + 1) % 4
        direct_count += 1

def rotation(mask):
    temp = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp[5-1-j][i] = mask[i][j]
    return temp

def move_sand(x,y, direct):
    global  result
    total_sand = graph[x][y]
    move_sand_sum = 0
    point = [0,0]
    mask = wind_mask[direct]
    for i in range(5):
        for j in range(5):
            if mask[i][j] != 0 and mask[i][j] != -1 :
                sand = int(total_sand * (0.01*mask[i][j]))
                move_sand_sum += sand
                if not(0<=x+i-2<n and 0<=y+j-2<n):
                    result += sand
                else:
                    graph[x+i-2][y+j-2] += sand
            elif mask[i][j] == -1:
                point = [x+i-2,y+j-2]

    res_sand = total_sand -move_sand_sum
    if not (0 <=point[0] < n and 0 <= point[1]< n):
        result += res_sand
    else:
        graph[point[0]][point[1]] += res_sand

def move_tornado():
    x,y = n//2, n//2
    direct_index = 0

    while 1:
        # 이동
        nx = x + dx[direct_index]
        ny = y + dy[direct_index]
        direct = direct_list[direct_index]
        # 모래 날리기
        if graph[nx][ny] != 0:
            move_sand(nx,ny,direct)
        #좌표가  0,0 이면 정지
        direct_index += 1
        if nx == 0 and ny == 0 :
            break
        x,y = nx,ny

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# 방향 결정
dx,dy, direct_list = make_root()

wind_mask = []
for i in range(4):
    move_mask = [[0, 0, 2, 0, 0],
                 [0, 10, 7, 1, 0],
                 [5, -1, 0, 0, 0],
                 [0, 10, 7, 1, 0],
                 [0, 0, 2, 0, 0]]
    for j in range(i):
        move_mask = rotation(move_mask)
    wind_mask.append(move_mask)

result = 0
move_tornado()
print(result)