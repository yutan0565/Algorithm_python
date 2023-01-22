import sys

def rotation_x_y(a,b):
    new_x =  b
    new_y = 4-a-1
    return new_x, new_y

def check_line(graph):
    global score
    new_graph  = [[0 for _ in range(4)] for _ in range(6)]
    point_row = 5
    for row in range(5, -1, -1):
        if graph[row].count(1) == 4:
            score += 1
        else:
            new_graph[point_row] = graph[row]
            point_row -= 1
    return new_graph

def check_special_line(graph):

    if graph[0].count(1) != 0: # 두개 라인
        graph  = [[0,0,0,0],[0,0,0,0]] + graph
        graph = graph[:6]
    elif graph[1].count(1) != 0: # 한개 라인
        graph  =  [[0,0,0,0]] + graph
        graph = graph[:6]
    return graph

def move_1x1_b(x,y):
    global green_graph, blue_graph
    #초록으로 이동
    for row in range(6):
        if row == 5:
            green_graph[row][y] = 1
            green_graph = check_line(green_graph)
            green_graph = check_special_line(green_graph)
        elif green_graph[row+1][y] == 1:
            green_graph[row][y] = 1
            green_graph = check_line(green_graph)
            green_graph = check_special_line(green_graph)
            break
        else:
            continue
    #파랑 이동
    b_x,b_y = rotation_x_y(x,y)
    for row in range(6):
        #파랑 이동
        if row == 5:
            blue_graph[row][b_y] = 1
            blue_graph = check_line(blue_graph)
            blue_graph = check_special_line(blue_graph)
        elif blue_graph[row+1][b_y] == 1:
            blue_graph[row][b_y] = 1
            blue_graph = check_line(blue_graph)
            blue_graph = check_special_line(blue_graph)
            break
        else:
            continue

def move_1x2_b(x,y):
    global green_graph, blue_graph
    # 초록으로 이동
    x_1,y_1 = x,y
    x_2, y_2 = x, y+1
    for row in range(6):
        if row == 5:
            green_graph[row][y_1], green_graph[row][y_2] = 1, 1
            green_graph = check_line(green_graph)
            green_graph = check_special_line(green_graph)
        elif green_graph[row+1][y_1] == 1 or green_graph[row+1][y_2] == 1:
            green_graph[row][y_1], green_graph[row][y_2] = 1, 1
            green_graph = check_line(green_graph)
            green_graph = check_special_line(green_graph)
            break
        else:
            continue

    # 파랑 이동
    b_x_1, b_y_1 = rotation_x_y(x_1, y_1)
    b_x_2, b_y_2 = rotation_x_y(x_2, y_2)
    for row in range(1,6):
        # 파랑 이동
        if row == 5:
            blue_graph[row][b_y_1] = 1
            blue_graph[row - 1][b_y_1] = 1
            blue_graph = check_line(blue_graph)
            blue_graph = check_special_line(blue_graph)
        elif blue_graph[row+1][b_y_1] == 1:
            blue_graph[row][b_y_1] = 1
            blue_graph[row-1][b_y_1] = 1
            blue_graph = check_line(blue_graph)
            blue_graph = check_special_line(blue_graph)
            break
        else:
            continue

def move_2x1_b(x,y):
    global green_graph, blue_graph
    # 초록으로 이동
    x_1,y_1 = x,y
    x_2, y_2 = x+1,y
    for row in range(1,6):
        if row == 5:
            green_graph[row][y_1] = 1
            green_graph[row - 1][y_1] = 1
            green_graph = check_line(green_graph)
            green_graph = check_special_line(green_graph)
        elif green_graph[row+1][y_1] == 1:
            green_graph[row][y_1] = 1
            green_graph[row-1][y_1] = 1
            green_graph = check_line(green_graph)
            green_graph = check_special_line(green_graph)
            break
        else:
            continue

    b_x_1, b_y_1 = rotation_x_y(x_1, y_1)
    b_x_2, b_y_2 = rotation_x_y(x_2, y_2)
    for row in range(6):
        if row == 5:
            blue_graph[row][b_y_1], blue_graph[row][b_y_2] = 1, 1
            blue_graph = check_line(blue_graph)
            blue_graph = check_special_line(blue_graph)
        elif blue_graph[row+1][b_y_1] == 1 or blue_graph[row+1][b_y_2] == 1:
            blue_graph[row][b_y_1], blue_graph[row][b_y_2] = 1, 1
            blue_graph = check_line(blue_graph)
            blue_graph = check_special_line(blue_graph)
            break
        else:
            continue

def fine_sum(graph):
    sum = 0
    for i in range(6):
        sum += graph[i].count(1)
    return sum

n = int(sys.stdin.readline().rstrip())

blue_graph = [[0 for _ in range(4)] for _ in range(6)]
green_graph = [[0 for _ in range(4)] for _ in range(6)]

score = 0
for i in range(n):
    type, x,y= map(int,sys.stdin.readline().rstrip().split())
    if type == 1:
        move_1x1_b(x,y)
    elif type == 2:
        move_1x2_b(x,y)
    elif type == 3:
        move_2x1_b(x,y)

    # print("turn : ", i)
    # print("초록")
    # for g in green_graph:
    #     print(g)
    # print("파랑")
    # for b in blue_graph:
    #     print(b)
    # print()

tile_in_blue = fine_sum(blue_graph)
tile_in_green = fine_sum(green_graph)
result = tile_in_blue + tile_in_green

print(score)
print(result)
"""
5
3 2 0
3 2 1
3 2 2
2 0 0
3 2 3

2
12

4
3 0 0
2 0 0
2 1 0
3 0 0

0
14


9
2 1 0
2 1 0
2 1 0
2 1 0
2 1 0
3 0 2
3 0 2
3 0 3
3 0 3

4
8

3
3 0 0
3 0 0
3 0 0
"""