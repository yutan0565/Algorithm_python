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
            direct = (direct+1)%4
        count += 1

def rotation_left(mask):
    new_mask = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_mask[5-1-j][i] = mask[i][j]
    return new_mask

def make_dust_mask(now_mask):
    dust_mask = [[0 for _ in range(5)] for _ in range(5)]
    now_dust = graph[b_x][b_y]
    use_dust = 0
    x,y = -1,-1

    for i in range(5):
        for j in range(5):
            if now_mask[i][j] == -1:
                x,y = i,j
                continue
            dust_mask[i][j] = now_dust*now_mask[i][j]//100
            use_dust += now_dust*now_mask[i][j]//100
    dust_mask[x][y] = now_dust-use_dust
    return dust_mask

def move_dust(dust_mask):
    # 지금 이동한 곳에는 먼지가 없음
    graph[b_x][b_y] = 0
    out_dust = 0

    for i in range(5):
        for j in range(5):
            nx = b_x-2+i
            ny = b_y-2+j
            if 0<=nx<n and 0<=ny<n:
                graph[nx][ny] += dust_mask[i][j]
            else:
                out_dust += dust_mask[i][j]
    return  out_dust

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

move_list = make_move_list()
dx = [0,1,0,-1]
dy = [-1,0,1,0]

mask_1 = [[0,0,2,0,0],[0,10,7,1,0],[5,-1,0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
mask_2 = rotation_left(mask_1)
mask_3 = rotation_left(mask_2)
mask_4 = rotation_left(mask_3)
mask_list = [mask_1, mask_2, mask_3, mask_4]

b_x, b_y = n//2, n//2

total_count = 0
for direct in move_list:
    # 빗자루 움직임
    b_x = b_x + dx[direct]
    b_y = b_y + dy[direct]
    # dust mask 만들기
    now_mask = mask_list[direct]
    dust_mask = make_dust_mask(now_mask)

    # 먼지 움직임 반영
    out_dust = move_dust(dust_mask)
    total_count += out_dust

print(total_count)