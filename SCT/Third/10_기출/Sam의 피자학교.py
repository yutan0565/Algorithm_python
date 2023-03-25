import copy
import sys

def make_roll_info():
    roll_end = []
    roll_height = []
    roll_width = []
    # 너비
    for width in range(1, n):
        roll_width.append(width)
        roll_width.append(width)
    #높이
    roll_height = roll_width[1:]

    end_point = 0
    roll_end.append(0)
    for heigt_index in range(len(roll_height)):
        end_point = end_point + roll_height[heigt_index]
        roll_end.append(end_point)
    return roll_end, roll_height, roll_width

def make_fold_info():
    fold_end, fold_height, fold_width = [], [], []
    fold_end = [n//2-1, n//2-1+n//4]
    fold_height = [1,2]
    fold_width = [n//2, n//4]
    return fold_end, fold_height, fold_width

def add_mil():
    min_value = min(graph[-1])
    for i in range(n):
        if graph[-1][i] == min_value:
            graph[-1][i] += 1

def rotate_block_90(width, height, block):
    new_width, new_height = height, width
    rotation_block = [[0 for _ in range(new_width)] for _ in range(new_height)]
    for i in range(height):
        for j in range(width):
            rotation_block[j][new_width-1-i] = block[i][j]
    return rotation_block

def roll_dow():
    for index in range(len(roll_end)):
        end_point = roll_end[index]
        next_end = roll_end[index+1]
        # 다음 끝 지점이/ 범위 넘어가면 그만
        if next_end > n-1:
            break
        else:
            # 한 블럭만 넘기는 경우에
            if index == 0:
                # 위치만 바꿔주기
                graph[n-1][0], graph[n-2][1] = graph[n-2][1], graph[n-1][0]
            else:
                width = roll_width[index]
                height = roll_height[index]
                # 돌릴 블럭 선정
                block = [[0 for _ in range(width)] for _ in range(height)]
                for i in range(n):
                    for j in range(n):
                        if n-height<= i< n and end_point-width+1<=j<=end_point:
                            new_x = i-n+height
                            new_y = j-end_point+width-1
                            block[new_x][new_y] = graph[i][j]
                            graph[i][j] = 0 # 돌릴 부분은 초기화
                # 블럭 돌리기
                rotation_block = rotate_block_90(width, height, block)
                # 블럭 올려주기
                ro_height = len(rotation_block)
                ro_width = len(rotation_block[0])
                for i in range(ro_height):
                    for j in range(ro_width):
                        new_x = n-width-1+i
                        new_y = end_point+1+j
                        graph[new_x][new_y] = rotation_block[i][j]

def push_dow():
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] != 0:
                            gap = abs(graph[i][j] - graph[nx][ny]) // 5
                            # 기존이 더 큰 경우
                            if graph[i][j] > graph[nx][ny]:
                                new_graph[i][j] -= gap
                            else:
                                new_graph[i][j] += gap
    new_line = []
    for col in range(n):
        for row in range(n-1, -1,-1):
            if new_graph[row][col] != 0:
                new_line.append(new_graph[row][col])

    new_graph = [[0 for _ in range(n)] for _ in range(n-1)] + [new_line]
    return new_graph

def rotation_180(block):
    height = len(block)
    width = len(block[0])
    rotation_block = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            rotation_block[height-1-i][width-1-j] = block[i][j]
    return rotation_block

def fold_dow():
    for index in range(len(fold_end)):
        end_point = fold_end[index]
        # 하나만 위로 올리는 경우
        width = fold_width[index]
        height = fold_height[index]
        # 돌릴 블럭 선정
        block = [[0 for _ in range(width)] for _ in range(height)]
        for i in range(n):
            for j in range(n):
                if n - height <= i < n and end_point - width + 1 <= j <= end_point:
                    new_x = i - n + height
                    new_y = j - end_point + width - 1
                    block[new_x][new_y] = graph[i][j]
                    graph[i][j] = 0  # 돌릴 부분은 초기화
        # 블럭 돌리기
        rotation_block = rotation_180(block)
        # 블럭 올려주기
        ro_height = len(rotation_block)
        ro_width = len(rotation_block[0])
        for i in range(ro_height):
            for j in range(ro_width):
                new_x = n - height-height + i
                new_y = end_point + 1 + j
                graph[new_x][new_y] = rotation_block[i][j]

n,k = map(int,sys.stdin.readline().rstrip().split())
graph = [[0 for _ in range(n)] for _ in range(n-1)] + [list(map(int,sys.stdin.readline().rstrip().split()))]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

roll_end, roll_height, roll_width = make_roll_info()
fold_end, fold_height, fold_width = make_fold_info()
result = 0
while 1:
    last_line = graph[-1]
    if max(last_line) - min(last_line) <= k:
        break
    # 밀가루 가장 적은 곳에 1 더해주기
    add_mil()
    # 도우 말기
    roll_dow()
    # 도우 누르기
    graph = push_dow()
    # 도우 두번 반으로 접기
    fold_dow()
    # 도우 누르기
    graph = push_dow()
    result += 1
print(result)

