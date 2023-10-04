import copy
import sys

def show_info():
    people_graph = [[[] for _ in range(n)] for _ in range(n)]
    for num in dict_pos.keys():
        if list_is_end[num] == 0: continue
        a,b = dict_pos[num]
        people_graph[a][b].append(num)
    # 사람들 위치
    print("사람들 위치")
    for g in people_graph:
        print(g)
    print("벽 위치")
    for g in graph_wall:
        print(g)
    print("total move : ", total_move)
    print("end_pos : ", [end_x,end_y])

def move_person(num):
    global total_move
    # 현재 거리 측정
    now_x,now_y = dict_pos[num]
    now_dis = abs(now_x-end_x) + abs(now_y - end_y)
    # 각 방향 이동하면서 확인 해보기
    for d in range(4):
        nx = now_x + dx[d]
        ny = now_y + dy[d]
        if 0<=nx<n and 0<=ny<n:
            if graph_wall[nx][ny] == 0:
                new_dis = abs(nx-end_x) + abs(ny - end_y)
                # 더 가까워 지는 경우, 이동하고 끝
                if new_dis < now_dis:
                    total_move += 1
                    # 만약 도착 한 경우
                    if [nx,ny] == [end_x,end_y]:
                        list_is_end[num] = 0
                        dict_pos[num] = [-1,-1]
                    else:
                        dict_pos[num] = [nx,ny]
                    return

def find_rotate_pos():
    for block_size in range(0, n+1):
        for i in range(n):
            for j in range(n):
                x_1, y_1 = i,j
                x_2, y_2 = i+block_size, j + block_size

                # end point 확인
                if x_1 <=end_x<=x_2 and y_1 <= end_y<=y_2:
                    # 사람 확인
                    in_list = []
                    for num in range(1, m + 1):
                        # 도착한 사람 제외
                        if list_is_end[num] == 0: continue
                        now_x,now_y = dict_pos[num]
                        if x_1 <= now_x <= x_2 and y_1 <= now_y <= y_2:
                            in_list.append(num)
                    if in_list != []:
                        return x_1, y_1,x_2, y_2, block_size+1,in_list

def rotate_right(x_1,y_1,x_2,y_2,block_size,in_list):
    global graph_wall,dict_pos,end_x,end_y
    # 벽 회전
    new_graph_wall = copy.deepcopy(graph_wall)
    for i in range(block_size):
        for j in range(block_size):
            # 벽 내구도 감소
            graph_wall[x_1 + i][y_1 + j] = max(0,graph_wall[x_1 + i][y_1 + j]-1)
            new_graph_wall[x_1 + j][y_1 + block_size - i - 1] = graph_wall[x_1 + i][y_1 + j]
    graph_wall = new_graph_wall
    # 사람 회전
    for num in in_list:
        x,y = dict_pos[num]
        nx = x_1 + (y - y_1)
        ny = y_1 + block_size - (x - x_1) - 1
        dict_pos[num] = [nx,ny]
    # 끝점 회전
    new_end_x = x_1 + (end_y - y_1)
    new_end_y = y_1 + block_size - (end_x - x_1) - 1
    end_x,end_y = new_end_x,new_end_y

def simulation():
    # k 초 동안
    for round in range(1, k+1):
        # 각 사람 마다 움직이기
        for num in range(1, m+1):
            # 도착한 사람 제외
            if list_is_end[num] == 0: continue
            move_person(num)
        # 모두 도착 했으면 그냥 끝
        if sum(list_is_end) == 0:
            return
        # 미로 회전
        # 회전할 좌상, 우하  좌표 찾기
        x_1,y_1,x_2,y_2, block_size, in_list = find_rotate_pos()
        # 회전 시작
        rotate_right(x_1,y_1,x_2,y_2,block_size,in_list)





n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph_wall = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

# 상하 좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 사람 위치
dict_pos = {}
for num in range(1, m+1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    dict_pos[num] = [a-1,b-1]
# 끝점 위치
end_x, end_y = map(int,sys.stdin.readline().rstrip().split())
end_x -= 1
end_y -= 1
# 도착 여부
list_is_end = [0] + [1 for  _ in range(m)]

total_move = 0

simulation()

# 모든 이동 거리
# 출구 좌표
print(total_move)
print(end_x+1,end_y+1)