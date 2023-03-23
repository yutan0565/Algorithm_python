import copy
import sys

# 나무 성장
def grow_tree():
    for i in range(n):
        for j in range(n):
            if graph_tree[i][j] >= 1:
                count = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph_tree[nx][ny] >= 1:
                            count += 1
                graph_tree[i][j] += count
    return graph_tree

# 나부 번식
def spread_tree():
    new_graph_tree = copy.deepcopy(graph_tree)
    for i in range(n):
        for j in range(n):
            if graph_tree[i][j] >= 1:
                count = 0
                list_grow = []
                now_tree = graph_tree[i][j]
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 다른 나무 없고 and 제초제 없음
                        if graph_tree[nx][ny] == 0 and graph_poison[nx][ny] == 0:
                            count += 1
                            list_grow.append([nx,ny])
                if len(list_grow) != 0:
                    plus_tree = now_tree // count
                    for x,y in list_grow:
                        new_graph_tree[x][y] += plus_tree
    return new_graph_tree

def find_kill_count(x,y):
    kill, poison = 0 , []
    # 첫 시작 위치
    kill += graph_tree[x][y]
    poison.append([x,y])
    for d in range(4):
        for mul in range(1, k+1):
            nx = x + dx_p[d]*mul
            ny = y + dy_p[d]*mul
            if not(0 <= nx < n and 0 <= ny < n):
                break
            if graph_tree[nx][ny] < 1:
                if graph_tree[nx][ny] != -1:
                    kill += graph_tree[nx][ny]
                    poison.append([nx, ny])
                break
            kill += graph_tree[nx][ny]
            poison.append([nx,ny])
    return kill, poison

# 가장 많은 나무 죽이는 곳에, 뿌리기
def put_poison():
    global result
    poison_list = []
    max_kill = -1
    for i in range(n):
        for j in range(n):
            # 나무가 있는 곳만 탐색
            if graph_tree[i][j] >=  1:
                kill, poison = find_kill_count(i,j)
                if kill > max_kill:
                    max_kill = kill
                    poison_list = poison
    # 실제 독 뿌리기
    if max_kill != -1:
        result += max_kill
    for x,y in poison_list:
        graph_tree[x][y] = 0
        graph_poison[x][y] = c+1


# 독 성능 감소
def down_poison():
    for i in range(n):
        for j in range(n):
            if graph_poison[i][j] != 0:
                graph_poison[i][j] -= 1


#  k  확산 범위,  c   남아 있는 년수
n,m,k,c = map(int,sys.stdin.readline().rstrip().split())
graph_tree = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_poison = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dx_p = [1,1,-1,-1]
dy_p = [1,-1,1,-1]

result = 0
for round in range(1,m+1):
    graph_tree = grow_tree()
    graph_tree = spread_tree()
    put_poison()
    down_poison()
    # print("라운드 : ", round)
    # print("kill : ", result)
    # for g in graph_tree:
    #     print(g)
    # print("---------")
    # for g in graph_poison:
    #     print(g)
    # print("---------")


print(result)