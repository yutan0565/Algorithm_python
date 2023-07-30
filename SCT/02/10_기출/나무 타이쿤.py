import copy
import sys

def cal_flower():
    count = 0
    for i in range(n):
        for j in range(n):
            count += graph_flower[i][j]
    return count

def move_medi_grow_flower(d,p):
    new_graph_medi = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] == 1:
                nx = (i + dx[d]*p)%n
                ny = (j + dy[d]*p) % n
                new_graph_medi[nx][ny] = 1
                # 꽃 자라기 // 양분으로
                graph_flower[nx][ny] += 1
    return new_graph_medi

def grow_cross():
    # 대각선 체크 해보기
    new_graph_flower = copy.deepcopy(graph_flower)
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] == 1:
                count = 0
                for d in range(4):
                    nx = i + dx_check[d]
                    ny = j + dy_check[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph_flower[nx][ny] >= 1:
                            count += 1
                new_graph_flower[i][j] += count
    return new_graph_flower

def cut_flower():
    new_graph_medi = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] != 1:
                if graph_flower[i][j] >= 2:
                    graph_flower[i][j] -= 2
                    new_graph_medi[i][j] = 1
    return new_graph_medi

n,m = map(int,sys.stdin.readline().rstrip().split())
graph_flower = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_medi = [[0 for _ in range(n)] for _ in range(n)]

# 초기 영양
graph_medi[n-1][0] = 1
graph_medi[n-2][0] = 1
graph_medi[n-1][1] = 1
graph_medi[n-2][1] = 1

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

dx_check = [1,1,-1,-1]
dy_check = [1,-1,1,-1]

for _ in range(m):
    d,p = map(int,sys.stdin.readline().rstrip().split())
    d = d-1
    # 영양제 이동 / 특수 영양제 있는 곳 자라기
    graph_medi =  move_medi_grow_flower(d,p)
    # 대각선 체크 및 자라기
    graph_flower = grow_cross()

    # 영양제 맞은 곳 제외 / 높이가 2 이상이면 잘라내기 / 영양제 올려주기 / 원래 있던곳은 패스
    graph_medi = cut_flower()

result = cal_flower()
print(result)
