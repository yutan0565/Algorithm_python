import sys
import copy

def rotation_right(x,y):
    nx = y
    ny = 4 - x - 1
    return nx, ny

def get_score(graph):
    global score
    new_graph = []
    del_count = 0

    for now_row in range(6):
        # 꽉 채워진 곳이 아니면
        if sum(graph[now_row]) != 4:
            new_graph += [graph[now_row]]
        else:
            del_count += 1
            score += 1

    new_graph = [[0 for _ in range(4)] for _ in range(del_count)] + new_graph
    return new_graph

def get_blur(graph):
    new_graph = copy.deepcopy(graph)
    if sum(new_graph[1]) != 0:
        new_graph = [[0,0,0,0]] + new_graph[:-1]
    if sum(new_graph[1]) != 0:
        new_graph = [[0,0,0,0]] + new_graph[:-1]
    return new_graph

# 블럭 하나만 내리기
def block_down_1(graph,x,y):
    for now_row in range(6):
        # 마지막 줄인 경우, 그냥 넣기
        if now_row == 5:
            graph[now_row][y] = 1
            break
        # 마지막 줄이 아닌경우, 다음 줄에 다른거 이쓰면 끝
        else:
            # 다음 줄에 다른게 있는 경우
            if graph[now_row+1][y] == 1:
                graph[now_row][y] = 1
                break
            # 다른게 없는 경우
            else:
                continue
    # 점수 획득
    graph = get_score(graph)
    # 블러 처리
    graph = get_blur(graph)
    return graph

# 받은거랑 오른쪽꺼
def block_down_2(graph,x,y):
    for now_row in range(6):
        # 마지막 줄인 경우, 그냥 넣기
        if now_row == 5:
            graph[now_row][y] = 1
            graph[now_row][y+1] = 1
            break
        # 마지막 줄이 아닌경우, 다음 줄에 다른거 이쓰면 끝
        else:
            # 다음 줄에 다른게 있는 경우
            if graph[now_row+1][y] == 1 or graph[now_row+1][y+1] == 1:
                graph[now_row][y] = 1
                graph[now_row][y+1] = 1
                break
            # 다른게 없는 경우
            else:
                continue
    # 점수 획득
    graph = get_score(graph)
    # 블러 처리
    graph = get_blur(graph)
    return graph

# 받은거랑 위에 꺼
def block_down_3(graph, x, y):
    for now_row in range(1,6):
        # 마지막 줄인 경우, 그냥 넣기
        if now_row == 5:
            graph[now_row][y] = 1
            graph[now_row-1][y] = 1
            break
        # 마지막 줄이 아닌경우, 다음 줄에 다른거 이쓰면 끝
        else:
            # 다음 줄에 다른게 있는 경우
            if graph[now_row+1][y] == 1:
                graph[now_row][y] = 1
                graph[now_row-1][y] = 1
                break
            # 다른게 없는 경우
            else:
                continue
    # 점수 획득
    graph = get_score(graph)
    # 블러 처리
    graph = get_blur(graph)
    return graph

def block_down(t,x,y):
    global graph_yellow, graph_red
    if t == 1:
        # 노란색
        graph_yellow =  block_down_1(graph_yellow, x,y)
        #빨간색
        x,y = rotation_right(x,y)
        graph_red = block_down_1(graph_red, x, y)
    elif t == 2:
        x_1,y_1 = x,y
        x_2,y_2 = x, y+1
        graph_yellow = block_down_2(graph_yellow, x_1, y_1)

        x,y = rotation_right(x_2, y_2)
        graph_red = block_down_3(graph_red, x,y)

    elif t == 3:
        x_1, y_1 = x, y
        x_2, y_2 = x+1, y
        graph_yellow = block_down_3(graph_yellow, x_2, y_2)

        x,y = rotation_right(x_2, y_2)
        graph_red = block_down_2(graph_red, x, y)


def simulation():
    for _ in range(k):
        t,x,y = map(int,sys.stdin.readline().rstrip().split())
        block_down(t,x,y)
        # print("========")
        # print(t, x, y)
        # print("graph_yellow")
        # for g in graph_yellow:
        #     print(g)
        # print("graph_red")
        # for g in graph_red:
        #     print(g)

def get_block_count(graph):
    count = 0
    for now_row in range(6):
        for i in range(4):
            count += graph[now_row][i]
    return count

k = int(sys.stdin.readline().rstrip())
score = 0
graph_yellow = [[0 for _ in range(4)] for _ in range(6)]
graph_red = [[0 for _ in range(4)] for _ in range(6)]
simulation()

total_block_count = get_block_count(graph_yellow) + get_block_count(graph_red)

print(score)
print(total_block_count)