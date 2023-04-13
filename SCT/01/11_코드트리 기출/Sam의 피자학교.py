import copy
import sys

def add_mil():
    min_value = min(graph[-1][:])
    for i in range(n):
        if graph[-1][i] == min_value:
            graph[-1][i] += 1

def rotation(temp_graph,heigh, width):
    new_temp_graph = [[0 for _ in range(heigh)] for _ in range(width)]
    for i in range(heigh):
        for j in range(width):
            new_temp_graph[j][heigh -1-i] = temp_graph[i][j]
    return new_temp_graph

def roll_dow():
    graph[n-2][1] = graph[n-1][0]
    graph[n-1][0] = 0
    for index in range(1, len(list_end_y)):
        start_y = list_end_y[index-1]
        end_y = list_end_y[index]
        height = list_h[index]
        if end_y + height > n-1:
            break
        temp_graph = graph[n-height:]
        for j in range(len(temp_graph)):
            temp_graph[j] = temp_graph[j][start_y+1:end_y+1]
            for p in range(start_y+1, end_y+1):
                graph[n-height+j][p] = 0
        temp_height = len(temp_graph)
        temp_width = len(temp_graph[0])
        temp_graph = rotation(temp_graph,temp_height, temp_width)
        temp_height, temp_width = temp_width, temp_height
        for i in range(temp_height):
            for j in range(temp_width):
                graph[n-1-temp_height+i][end_y+1+j] = temp_graph[i][j]

def push_dow():
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                temp_mil = graph[i][j]
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] != 0:
                            if graph[i][j] - graph[nx][ny] > 0:
                                new_graph[i][j] -= (graph[i][j] - graph[nx][ny])//5
                                new_graph[nx][ny] += (graph[i][j] - graph[nx][ny]) // 5

    new_line = []
    for j in range(n):
        for i in range(n-1,-1,-1):
            if new_graph[i][j] != 0:
                new_line.append(new_graph[i][j])
    return [[0 for _ in range(n)] for _ in range(n-1)] + [new_line]

def fold_dow():
    for index in range(0, len(list_fold_end_y)):
        if index == 0:
            start_y = -1
        else:
            start_y = list_fold_end_y[index-1]
        end_y = list_fold_end_y[index]
        height = list_fold_h[index]
        temp_graph = graph[n-height:]
        for j in range(len(temp_graph)):
            temp_graph[j] = temp_graph[j][start_y+1:end_y+1]
            for p in range(start_y+1, end_y+1):
                graph[n-height+j][p] = 0
        temp_height = len(temp_graph)
        temp_width = len(temp_graph[0])
        temp_graph = rotation(temp_graph,temp_height, temp_width)
        temp_graph = rotation(temp_graph, temp_width, temp_height)
        for i in range(temp_height):
            for j in range(temp_width):
                graph[n-index-1-temp_height+i][end_y+1+j] = temp_graph[i][j]

def cal_min_max():
    max_ = max(graph[-1])
    min_ = min(graph[-1])
    if max_ - min_ <= k:
        return 1
    else:
        return -1

def show_graph():
    for g in graph:
        print(g)
    print()

n,k = map(int,sys.stdin.readline().rstrip().split())
input_line = list(map(int,sys.stdin.readline().rstrip().split()))
graph = [[0 for _ in range(n)] for _ in range(n-1)] + [input_line]

# 자르기 끝점 : 0  1  3  5  8  11   15
# 끝점 간격   : 1 2 2 3 3 4 4
# 높이        : 1 2 2 3 3 4 4 5 5

list_end_y = [0, 1]
list_h = [1]
point = 1
dis = 2

while 1:
    point += dis
    if point >= n-1:
        list_h.append(dis)
        break
    list_end_y.append(point)
    list_h.append(dis)
    point += dis
    if point >= n-1:
        list_h.append(dis)
        break
    list_end_y.append(point)
    list_h.append(dis)
    dis += 1

list_fold_end_y = [n//2-1, n//2-1 + n//4]
list_fold_h = [1, 2]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def cal_result():
    global graph
    if n == 1:
        return 0
    result = 0
    while 1:
        if cal_min_max() == 1:
            break
        # 가장 작은 위치에 모두 1만큼 더해주기
        add_mil()
        # 도우 말기
        roll_dow()
        # 눌러 주기
        graph = push_dow()
        # 두 번 반으로 접기
        fold_dow()
        # 둘러 주기
        graph = push_dow()

        result += 1
    return result

print( cal_result())