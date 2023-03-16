import sys

def rotation(list):
    new_point_list = []
    for a,b in list:
        new_x = b
        new_y = 4-1-a
        new_point_list.append([new_x,new_y])
    return new_point_list

def check_full_line(graph):
    global score
    del_count = 0
    new_graph = []
    for now_line in range(6):
        if graph[now_line] == [1,1,1,1]:
            score += 1
            del_count += 1
        else:
            new_graph.append(graph[now_line])

    for _ in range(del_count):
        new_graph = [[0,0,0,0]] + new_graph
    return new_graph

def check_blur_line(graph):
    while 1:
        if 1 in graph[1]:
            graph = [[0,0,0,0]] + graph[:-1]
        else:
            break
    return graph

def down_block_1(graph, point):
    block_col = point[1]
    for now_line in range(0, 6):
        if now_line == 5 and graph[now_line][block_col] != 1:
            graph[now_line][block_col] = 1
            break
        elif graph[now_line+1][block_col] == 1:
            graph[now_line][block_col] = 1
            break

    graph = check_full_line(graph)
    graph = check_blur_line(graph)
    return graph

# 평평
def down_block_2(graph, point_list):
    block_col_1 = point_list[0][1]
    block_col_2 = point_list[1][1]
    for now_line in range(0, 6):
        if now_line == 5 and graph[now_line][block_col_1] != 1 and graph[now_line][block_col_2] != 1:
            graph[now_line][block_col_1] = 1
            graph[now_line][block_col_2] = 1
            break
        elif graph[now_line+1][block_col_1] == 1 or graph[now_line+1][block_col_2] == 1:
            graph[now_line][block_col_1] = 1
            graph[now_line][block_col_2] = 1
            break
    graph = check_full_line(graph)
    graph = check_blur_line(graph)
    return graph
# 수직
def down_block_3(graph, point_list):
    block_col = point_list[0][1]
    for now_line in range(1, 6):
        if now_line == 5 and graph[now_line][block_col] != 1:
            graph[now_line][block_col] = 1
            graph[now_line-1][block_col] = 1
            break
        elif graph[now_line+1][block_col] == 1:
            graph[now_line][block_col] = 1
            graph[now_line - 1][block_col] = 1
            break
    graph = check_full_line(graph)
    graph = check_blur_line(graph)
    return graph

def cal_block(graph):
    count = 0
    for i in range(6):
        for j in range(4):
            if graph[i][j] == 1:
                count += 1
    return count

yellow_graph = [[0 for _ in range(4)] for _ in range(6)]
red_graph = [[0 for _ in range(4)] for _ in range(6)]


k = int(sys.stdin.readline().rstrip())
score = 0
for _ in range(k):
    t,x,y = map(int,sys.stdin.readline().rstrip().split())
    if t == 1:
        # 노랑이
        point_list_y = [[x,y]]
        yellow_graph = down_block_1(yellow_graph, point_list_y[0])
        # 빨강이
        point_list_r = rotation(point_list_y)
        red_graph = down_block_1(red_graph, point_list_r[0])
    elif t == 2:
        # 노랑이
        point_list_y = [[x, y],[x, y+1]]
        yellow_graph = down_block_2(yellow_graph, point_list_y)
        # 빨강이
        point_list_r = rotation(point_list_y)
        red_graph = down_block_3(red_graph, point_list_r)
    elif t == 3:
        # 노랑이
        point_list_y = [[x, y], [x+1, y]]
        yellow_graph = down_block_3(yellow_graph, point_list_y)
        # 빨강이
        point_list_r = rotation(point_list_y)
        red_graph = down_block_2(red_graph, point_list_r)


count_block = cal_block(yellow_graph) + cal_block(red_graph)
print(score)
print(count_block)


"""


"""