import copy
import sys

def move_potion():
    new_graph_potion = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_potion[i][j] == 1 :
                nx = (i + dx[d]*p)%n
                ny = (j + dy[d]*p)%n
                new_graph_potion[nx][ny] = 1
    return new_graph_potion

def use_potion():
    for i in range(n):
        for j in range(n):
            if graph_potion[i][j] == 1:
                graph[i][j] += 1

def grow_leaf():
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph_potion[i][j] == 1:
                count = 0
                for k in range(4):
                    nx = i + dx_find[k]
                    ny = j + dy_find[k]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] != 0:
                            count += 1
                new_graph[i][j] += count
    return new_graph

def on_potion():
    for i in range(n):
        for j in range(n):
            if graph_potion[i][j] != 1:
                if graph[i][j] >= 2:
                    graph[i][j] -= 2
                    graph_potion[i][j] = 1
            elif graph_potion[i][j] == 1:
                graph_potion[i][j] = -1

def cal_result():
    result = 0
    for i in range(n):
        for j in range(n):
            result += graph[i][j]
    return result

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

dx_find = [1,1,-1,-1]
dy_find = [1,-1,1,-1]

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_potion = [[-1 for _ in range(n)] for _ in range(n)]
graph_potion[n-1][0],graph_potion[n-2][0],graph_potion[n-1][1],graph_potion[n-2][1] = 1,1,1,1

def show_graph():
    for g in graph_potion:
        print(g)
    print()

for _ in range(m):
    d,p = map(int,sys.stdin.readline().rstrip().split())
    d = d-1
    # 특수 영양제 이동
    graph_potion = move_potion()

    # 영양제 투입
    use_potion()

    # 대각선 있는 잎, 대각선에 있는 1 이상의 개수 만큼 높이 성장 (대각선은 연결 x)
    graph = grow_leaf()

    # 영양제 투입한 잎 제외, 높이가 2 이상인거는 2를 베어냄, 베어낸 곳은 영양제 올려두기
    on_potion()

result = cal_result()
print(result)
"""
5 1
1 0 0 4 2
2 1 3 2 1
0 0 0 2 5
1 0 0 0 3
1 2 1 3 3
2 4

"""