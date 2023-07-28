import copy
import sys
def dow_roll_info():
    dow_roll_end = [0, 1]
    dow_roll_height = []
    dow_roll_width = []

    index = 1
    gap = 1
    stop_flag = 0
    while 1:
        gap += 1
        for i in range(2):
            if index > n-1: # 마지막 접는 부분 까지  / 나중에 하나 뺴줘야함(이전꺼 접으면 넘어가는거니까)
                stop_flag = 1
                dow_roll_width.append(gap-1)
                if i == 0:
                    dow_roll_width.append(gap - 1)
                    dow_roll_width.append(gap)
                    dow_roll_width.append(gap)
                else:
                    dow_roll_width.append(gap)
                    dow_roll_width.append(gap)
                    dow_roll_width.append(gap+1)
                break
            index += gap
            dow_roll_end.append(index)
            dow_roll_width.append(gap-1)
        if stop_flag == 1:
            break
    dow_roll_height = dow_roll_width[1:]

    f_len = len(dow_roll_end) -1
    # print(dow_roll_end[:f_len])
    # print(dow_roll_height[:f_len])
    # print( dow_roll_width[:f_len])

    return dow_roll_end[:f_len], dow_roll_height[:f_len],dow_roll_width[:f_len]

def dow_fold_info():
    now_len = n
    half_len = n // 2
    half_half_len = half_len // 2
    dow_fold_end =[half_len-1,half_len + half_half_len-1]
    dow_fold_height = [1, 2]
    dow_fold_width = [half_len, half_half_len]

    return dow_fold_end,dow_fold_height,dow_fold_width


def cal_min_max_gap(list):
    return max(list) - min(list)

# 밀가루 넣기
def add_flour():
    min_value = min(graph[-1])
    for j in range(n):
        if graph[-1][j] == min_value:
            graph[-1][j] += 1

def rotation_right(roll_block, height, width):
    new_height, new_width = width, height
    new_block = [[0 for _ in range(new_width)] for _ in range(new_height)]
    for i in range(height):
        for j in range(width):
            new_block[j][new_width-1-i] = roll_block[i][j]
    return new_block ,new_height, new_width

# 도우 말기
def roll_dow():
    for i in range(len(dow_roll_end)):
        end_point = dow_roll_end[i]
        height = dow_roll_height[i]
        width = dow_roll_width[i]

        # 말았는데 범위 넘어 가면 ?
        if end_point + height > n-1:
            break
        # 범위 넘어가지 않으면, 말아주기
        else:
            # 첫번째 블럭인 경우 // 그냥 옮기고 끝내기
            if end_point == 0:
                graph[n-1][0], graph[n-2][1] = graph[n-2][1], graph[n-1][0]
                continue
            else:
                # 옮길 블럭 모양 잡기
                roll_block = [[0 for _ in range(width)] for _ in range(height)]
                # 기존 그래프
                for i in range(n):
                    for j in range(n):
                        # 범위 내에 있는 블럭 이면
                        if n - 1 - height < i <= n - 1:
                            if end_point-width+1 <= j <= end_point:
                                new_x = i - (n - 1 - height) - 1
                                new_y = j - (end_point-width+1)
                                roll_block[new_x][new_y] = graph[i][j]
                                graph[i][j] = 0
                # 옮길 모양 오른쪽으로 돌리기
                roll_block,  new_height, new_width = rotation_right(roll_block, height, width)
                # 기존 그래프에 붙이기
                for i in range(new_height):
                    for j in range(new_width):
                        new_x = n-1-new_height+i
                        new_y = end_point + 1 + j
                        graph[new_x][new_y] = roll_block[i][j]

# 도우 누르기
def push_dow():
    new_graph = copy.deepcopy(graph)
    do_list = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]!= 0:
                now_m = graph[i][j]
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if [[nx,ny], [i,j]] in do_list or [[i,j], [nx,ny]] in do_list:
                            continue
                        else:
                            do_list.append([[nx,ny], [i,j]])
                        check_m = graph[nx][ny]
                        if check_m != 0:
                            gap = abs(now_m - check_m) // 5
                            if now_m > check_m:
                                new_graph[i][j] -= gap
                                new_graph[nx][ny] += gap
                            else:
                                new_graph[i][j] += gap
                                new_graph[nx][ny] -= gap
    new_dow_line = []
    for col in range(0, n):
        for row in range(n-1, -1, -1):
            if new_graph[row][col] != 0:
                new_dow_line.append(new_graph[row][col])

    new_graph = [[0 for _ in range(n)] for _ in range(n - 1)] + [new_dow_line]
    return new_graph

def rotation_180(roll_block, height, width):
    new_block = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            new_block[height-1-i][width-1-j] = roll_block[i][j]
    return new_block
# 반 반 접기
def fold_dow():
    for i in range(len(dow_fold_end)):
        end_point = dow_fold_end[i]
        height = dow_fold_height[i]
        width = dow_fold_width[i]

        # 옮길 블럭 모양 잡기
        if i == 0:
            roll_block = graph[-1][:width]
            for i in range(width):
                row = n-2
                col = width + i
                graph[row][col] = roll_block[width-1-i]
                graph[n-1][i] = 0
        else:
            roll_block = [[0 for _ in range(width)] for _ in range(height)]
            # 기존 그래프
            for i in range(n):
                for j in range(n):
                    # 범위 내에 있는 블럭 이면
                    if n - 1 - height < i <= n - 1:
                        if end_point - width + 1 <= j <= end_point:
                            new_x = i - (n - 1 - height) - 1
                            new_y = j - (end_point - width + 1)
                            roll_block[new_x][new_y] = graph[i][j]
                            graph[i][j] = 0
            # 옮길 모양 오른쪽으로 돌리기
            roll_block = rotation_180(roll_block, height, width)
            # 기존 그래프에 붙이기
            for i in range(height):
                for j in range(width):
                    new_x = n - 1 - height + i-1
                    new_y = end_point + 1 + j
                    graph[new_x][new_y] = roll_block[i][j]


n,k = map(int,sys.stdin.readline().rstrip().split())
dow_line = list(map(int,sys.stdin.readline().rstrip().split()))
graph = [[0 for _ in range(n)] for _ in range(n-1)] + [dow_line]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dow_roll_end,dow_roll_height,dow_roll_width = dow_roll_info()
dow_fold_end,dow_fold_height,dow_fold_width = dow_fold_info()

def show_info():
    print("------------")
    for g in graph:
        print(g)

result = 0
while 1:
    min_max_gap = cal_min_max_gap(graph[-1])
    if min_max_gap <= k:
        break
    result += 1
    # 밀가루 넣기
    add_flour()
    # 도우 말기
    roll_dow()
    # 도우 누르기
    graph = push_dow()
    # 반 반 접기
    fold_dow()
    # 도우 누르기
    graph = push_dow()


print(result)

"""
9 4
1 10 4 13 8 3 1 7 20


"""