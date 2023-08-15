import sys

def make_direct_list():
    direct = 0
    count = 1
    direct_list = []
    while 1:
        for _ in range(2):
            for _ in range(count):
                direct_list.append(direct)
                if len(direct_list) == n*n - 1:
                    return direct_list
            direct = (direct + 1)%4
        count += 1

def rotation_left(dust_mask):
    new_dust_mask = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_dust_mask[5-1-j][i] = dust_mask[i][j]
    return new_dust_mask

def make_dust_graph(x, y, direct):
    dust_mask = dict_dust_mask[direct]
    now_dust = graph[x][y]
    dust_graph = [[0 for _ in range(5)] for _ in range(5)]
    use_dust = 0
    temp_x, temp_y = 0,0
    for i in range(5):
        for j in range(5):
            if dust_mask[i][j] == -1:
                temp_x, temp_y = i,j
                continue
            if dust_mask[i][j] != 0 :
                temp = now_dust * dust_mask[i][j] // 100
                use_dust += temp
                dust_graph[i][j] = temp
    dust_graph[temp_x][temp_y] = now_dust - use_dust
    return dust_graph

n = int(sys.stdin.readline().rstrip())
graph  = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

now_x, now_y = n//2, n//2
dx = [0,1,0,-1]
dy = [-1,0,1,0]
direct_list = make_direct_list()

dict_dust_mask = {}
dict_dust_mask[0] = [[0,0,2,0,0],[0,10,7,1,0],[5,-1,0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
dict_dust_mask[1] = rotation_left(dict_dust_mask[0])
dict_dust_mask[2] = rotation_left(dict_dust_mask[1])
dict_dust_mask[3] = rotation_left(dict_dust_mask[2])

total_dust = 0
for now_direct in direct_list:
    # 빗자루 이동
    now_x = now_x + dx[now_direct]
    now_y = now_y + dy[now_direct]

    # 먼지 그래프 만들기
    dust_graph = make_dust_graph(now_x, now_y, now_direct)
    # 기존 그래프 좌표로 전환해서 붙여보기
    # 빗자루 이동한 곳은 0
    graph[now_x][now_y] = 0
    for i in range(5):
        for j in range(5):
            nx = now_x - 2 + i
            ny = now_y - 2 + j
            # 벗어 나는 먼지
            if not(0<=nx<n and 0<=ny<n):
                total_dust += dust_graph[i][j]
            else:
                graph[nx][ny] += dust_graph[i][j]
print(total_dust)

