import copy
import sys
from collections import deque, defaultdict
import heapq

def grow_tree():
    global graph
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] >= 1:
                            cnt += 1
                new_graph[i][j] += cnt
    graph = new_graph

def spread_tree():
    global graph
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1:
                able_cnt = 0
                able_list = []
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] == 0:
                            if graph_poison[nx][ny] == 0:
                                able_cnt += 1
                                able_list.append([nx,ny])
                if able_cnt == 0:
                    continue
                add_tree = graph[i][j]//able_cnt
                for a,b in able_list:
                    new_graph[a][b] += add_tree
    graph = new_graph

def count_dead(x,y):
    dead_cnt = 0
    # 시작 위치
    dead_cnt += graph[x][y]
    for d in range(4):
        for ss in range(1, k+1):
            nx = x + dx_cross[d]*ss
            ny = y + dy_cross[d]*ss
            # 영역 밖
            if not(0<=nx<n and 0<=ny<n):
                break
            # 벽
            if graph[nx][ny] == -1:
                break
            # 빈공간
            if graph[nx][ny] == -1:
                break
            dead_cnt += graph[nx][ny]
    return dead_cnt


def put_poison():
    global total_dead
    # 뿌릴 위치 찾기
    # 죽은 수, 행, 열
    hq = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                continue
            else:
                dead_cnt = count_dead(i,j)
                heapq.heappush(hq, [-dead_cnt,i,j])
    dead_cnt, x,y = heapq.heappop(hq)
    dead_cnt *= -1
    # 제초제 뿌리기
    total_dead += dead_cnt
    graph_poison[x][y] = c
    graph[x][y] = 0
    for d in range(4):
        for ss in range(1, k+1):
            nx = x + dx_cross[d]*ss
            ny = y + dy_cross[d]*ss
            # 영역 밖
            if not(0<=nx<n and 0<=ny<n):
                break
            # 벽
            if graph[nx][ny] == -1:
                break
            # 빈공간
            if graph[nx][ny] == -1:
                graph_poison[nx][ny] = c
                graph[nx][ny] = 0
                break
            graph_poison[nx][ny] = c
            graph[nx][ny] = 0

def down_poison():
    for i in range(n):
        for j in range(n):
            graph_poison[i][j] = max(0,graph_poison[i][j]-1)

def show_info():
    print("graph")
    for g in graph:
        print(g)
    print("poison")
    for g in graph_poison:
        print(g)

def simulation():
    for turn in range(1, m + 1):
        # 나무 성장
        grow_tree()
        # 번식 진행
        spread_tree()
        # 제초제 뿌림
        down_poison()
        put_poison()

n,m,k,c = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_poison = [[0 for _ in range(n)] for _ in range(n)]
total_dead = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]
dx_cross = [1,-1,-1,1]
dy_cross = [1,1,-1,-1]

simulation()
print(total_dead)