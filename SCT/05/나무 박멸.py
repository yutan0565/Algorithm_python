import copy
import sys

def show_info():
    print("===========================")
    for g in graph_tree:
        print(g)
    print()
    for g in graph_dead:
        print(g)
def grow_tree():
    global graph_tree
    new_graph_tree = copy.deepcopy(graph_tree)
    for i in range(n):
        for j in range(n):
            # 나무가 있는 경우에만
            if graph_tree[i][j] >= 1:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph_tree[nx][ny] >= 1:
                            cnt += 1
                new_graph_tree[i][j] += cnt
    graph_tree = new_graph_tree

def spread_tree():
    global graph_tree
    new_graph_tree = copy.deepcopy(graph_tree)
    for i in range(n):
        for j in range(n):
            # 나무가 있는 경우에만
            if graph_tree[i][j] >= 1:
                empty_pos_list = []
                now_tree = graph_tree[i][j]
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        # 빈칸이면서
                        if graph_tree[nx][ny] == 0:
                            # 제초제가 없는곳
                            if graph_dead[nx][ny] == 0:
                                empty_pos_list.append([nx,ny])
                if len(empty_pos_list) != 0:
                    add_tree = now_tree // len(empty_pos_list)
                    for a,b in empty_pos_list:
                        new_graph_tree[a][b] += add_tree
    graph_tree = new_graph_tree

def find_max_dead_pos():
    max_dead_pos_list = []
    max_dead = 0

    for i in range(n):
        for j in range(n):
            # 벽이 아닌 곳에만 뿌려보기
            if graph_tree[i][j] != -1:
                now_pos_list = []
                now_dead = 0
                # 나무가 전혀 없는 칸인 경우
                if graph_tree[i][j] == 0:
                    now_pos_list = [[i,j]]
                    now_dead = 0
                else:
                    # 나무가 있는 경우
                    now_pos_list.append([i,j])
                    now_dead += graph_tree[i][j]
                    # 대각선으로 뿌려보기
                    for d in range(4):
                        # 각 방향으로 진행
                        for speed in range(1,k+1):
                            nx = i + dx_cross[d]*speed
                            ny = j + dy_cross[d]*speed
                            # 범위 벗어나는 경우
                            if not(0<=nx<n and 0<=ny<n):
                                break
                            # 벽을 만나는 경우
                            if graph_tree[nx][ny] == -1:
                                break
                            # 빈칸인 경우
                            if graph_tree[nx][ny] == 0:
                                now_pos_list.append([nx,ny])
                                break
                            # 나무가 있는 경우
                            if graph_tree[nx][ny] >= 1:
                                now_pos_list.append([nx,ny])
                                now_dead += graph_tree[nx][ny]
                                continue
                if now_dead > max_dead:
                    max_dead_pos_list = now_pos_list
                    max_dead = now_dead
    return max_dead_pos_list, max_dead

def put_poison():
    global total_dead

    # 가장 많이 죽일 수 있는 위치 찾기
    max_dead_pos_list, max_dead = find_max_dead_pos()
    # 제초제 뿌리기, 뿌려진곳 나무 죽기
    for a,b in max_dead_pos_list:
        graph_tree[a][b] = 0
        graph_dead[a][b] = c
    total_dead += max_dead

def down_poison():
    for i in range(n):
        for j in range(n):
            if graph_dead[i][j] >= 1:
                graph_dead[i][j] -= 1

def simulation():
    for year in range(1, m+1):

        # 나무 성장
        grow_tree()
        #번식 진행
        spread_tree()
        # 제초제 줄이기
        down_poison()
        # 제초제 뿌리기
        put_poison()


# 크기, 진행 년수, 범위, 남아있는 년수
n,m,k,c = map(int,sys.stdin.readline().rstrip().split())

graph_tree = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_dead = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

dx_cross = [1,1,-1,-1]
dy_cross = [1,-1,1,-1]

total_dead = 0

simulation()
print(total_dead)