import copy
import sys

def rotation_right(x,y):
    return y, 4-1-x

def del_line(graph):
    global total_score
    new_graph = []
    for row in range(6):
        if graph[row] == [1,1,1,1]:
            total_score += 1
            new_graph = [[0,0,0,0]] + new_graph
        else:
            new_graph.append(graph[row])
    return new_graph

def check_blur(graph):
    new_graph = copy.deepcopy(graph)
    if 1 in graph[0]:
        new_graph = [[0,0,0,0]] + new_graph[:-1]
    if 1 in graph[1]:
        new_graph = [[0,0,0,0]] + new_graph[:-1]
    return new_graph

def down_block_1(graph,x,y):
    for row in range(6):
        if row == 5:
            graph[row][y] = 1
        else:
            if graph[row+1][y] == 1:
                graph[row][y] = 1
                break
    graph = del_line(graph)
    graph = check_blur(graph)
    return graph

# 수평
def down_block_2(graph,x_1,y_1,x_2,y_2):
    for row in range(6):
        if row == 5:
            graph[row][y_1] = 1
            graph[row][y_2] = 1
        else:
            if graph[row+1][y_1] == 1 or graph[row+1][y_2] == 1:
                graph[row][y_1] = 1
                graph[row][y_2] = 1
                break
    graph = del_line(graph)
    graph = check_blur(graph)
    return graph


# 수직
def down_block_3(graph,x_1,y_1,x_2,y_2):
    for row in range(6):
        if row == 5:
            graph[row][y_1] = 1
            graph[row-1][y_1] = 1
        else:
            if graph[row+1][y_1] == 1 :
                graph[row][y_1] = 1
                graph[row-1][y_1] = 1
                break
    graph = del_line(graph)
    graph = check_blur(graph)
    return graph

def block_count(graph):
    count = 0
    for i in range(6):
        for j in range(4):
            if graph[i][j] == 1:
                count += 1
    return count

k = int(sys.stdin.readline().rstrip())

graph_yellow = [[0 for _ in range(4)] for _ in range(6)]
graph_red = [[0 for _ in range(4)] for _ in range(6)]

total_score = 0
for round in range(1,k+1):
    type,x,y = map(int,sys.stdin.readline().rstrip().split())
    if type == 1:
        graph_yellow = down_block_1(graph_yellow,x,y)
        x,y = rotation_right(x,y)
        graph_red = down_block_1(graph_red, x, y)
    # 수평
    elif type == 2:
        x_1,y_1,x_2,y_2 = x,y,x,y+1
        graph_yellow = down_block_2(graph_yellow,x_1,y_1,x_2,y_2)
        x,y = rotation_right(x,y)
        x_1,y_1,x_2,y_2 = x,y,x+1,y
        graph_red = down_block_3(graph_red, x_1,y_1,x_2,y_2)
    #수직
    elif type == 3:
        x_1,y_1,x_2,y_2 = x,y,x+1,y
        graph_yellow = down_block_3(graph_yellow,x_1,y_1,x_2,y_2)
        x,y = rotation_right(x,y)
        x_1,y_1,x_2,y_2 = x,y,x,y-1
        graph_red = down_block_2(graph_red,x_1,y_1,x_2,y_2)
    # print("round : ", round)
    # print("노랑")
    # for g in graph_yellow:
    #     print(g)
    # print("빨강")
    # for g in graph_red:
    #     print(g)
    # print("=======================")

total_count = block_count(graph_yellow) + block_count(graph_red)
print(total_score)
print(total_count)