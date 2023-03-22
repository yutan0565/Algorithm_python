import sys

def rotation_point(a,b):
    new_a = b
    new_b = 4-1-a
    return new_a, new_b

def dell_line(graph):
    global total_score
    new_graph = []

    count = 0
    for row in range(6):
        if graph[row] == [1, 1, 1, 1]:
            count += 1
            total_score += 1
        else:
            new_graph.append(graph[row])

    for _ in range(count):
        new_graph = [[0,0,0,0]] + new_graph
    return new_graph

def check_blur(graph):
    # 두 라인에 블럭 있는 경우
    if 1 in graph[0] and 1 in graph[1]:
        for _ in range(2):
            graph = [[0, 0, 0, 0]] + graph[:-1]
    elif 1 in graph[1]:
        graph = [[0, 0, 0, 0]] + graph[:-1]
    return graph

def down_block_1(graph,x,y):
    for row in range(0,6):
        if row == 5:
            graph[row][y] = 1
            break
        else:
            check_row = row + 1
            # 다음 칸에 블럭 있으면
            if graph[check_row][y] == 1:
                graph[row][y] = 1
                break
    graph = dell_line(graph)
    graph = check_blur(graph)
    return graph

# 수평 블럭 내리기
def down_block_2(graph,block_list):
    col_1, col_2 = block_list[0][1], block_list[1][1]
    for row in range(0,6):
        if row == 5:
            graph[row][col_1] = 1
            graph[row][col_2] = 1
            break
        else:
            check_row = row + 1
            # 다음 칸에 블럭 있으면
            if graph[check_row][col_1] == 1 or graph[check_row][col_2] == 1:
                graph[row][col_1] = 1
                graph[row][col_2] = 1
                break
    graph = dell_line(graph)
    graph = check_blur(graph)
    return graph

# 수직 블럭 내리기
def down_block_3(graph, block_list):
    col = block_list[0][1]
    for row in range(0,6):
        if row == 5:
            graph[row][col] = 1
            graph[row-1][col] = 1
            break
        else:
            check_row = row + 1
            # 다음 칸에 블럭 있으면
            if graph[check_row][col] == 1:
                graph[row][col] = 1
                graph[row-1][col] = 1
                break
    graph = dell_line(graph)
    graph = check_blur(graph)
    return graph

def cal_block(graph):
    count = 0
    for i in range(6):
        for j in range(4):
            count += graph[i][j]
    return count

def show_graph(graph):
    for g in graph:
        print(g)


k = int(sys.stdin.readline().rstrip())

graph_yellow = [[0 for _ in range(4)] for _ in range(6)]
graph_red = [[0 for _ in range(4)] for _ in range(6)]

total_score = 0
for turn in range(1,k+1):
    t,x,y = map(int,sys.stdin.readline().rstrip().split())
    s_x,s_y = x,y
    if t == 1:
        # 노란색으로 내리기
        graph_yellow = down_block_1(graph_yellow,x,y)
        # 빨간색으로 내리기
        x,y = rotation_point(x,y)
        graph_red = down_block_1(graph_red,x,y)

    elif t == 2:
        # 노란색으로 내리기 / 수평
        block_list = [[x,y],[x,y+1]]
        graph_yellow = down_block_2(graph_yellow, block_list)
        # 빨간색으로 내리기 / 수직
        x, y = rotation_point(x, y)
        block_list = [[x-1,y],[x,y]]
        graph_red = down_block_3(graph_red, block_list)

    elif t == 3:
        # 노란색으로 내리기 / 수직
        block_list = [[x+1,y],[x,y]]
        graph_yellow = down_block_3(graph_yellow, block_list)
        # 빨간색으로 내리기 / 수평
        x, y = rotation_point(x, y)
        block_list = [[x,y],[x,y-1]]
        graph_red = down_block_2(graph_red, block_list)
    # print("========================")
    # print(turn)
    # print("종류 : ", t, "위치 : ",[s_x,s_y])
    # print("점수 : ", total_score)
    # print("노락")
    # show_graph(graph_yellow)
    # print("빨강")
    # show_graph(graph_red)

count_result = cal_block(graph_yellow) + cal_block(graph_red)

print(total_score)
print(count_result)