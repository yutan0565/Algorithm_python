import copy
import sys

def grow_tree():
    new_graph_tree = copy.deepcopy(graph_tree)
    for i in range(n):
        for j in range(n):
            # 나무가 있는 곳인 경우 / 성장 시작
            if graph_tree[i][j] >= 1:
                count = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph_tree[nx][ny] >= 1:
                            count += 1
                new_graph_tree[i][j] += count
    return new_graph_tree

def spread_tree():
    new_graph_tree = copy.deepcopy(graph_tree)
    for i in range(n):
        for j in range(n):
            # 나무가 있는 곳인 경우 / 빈곳 찾고 / 번식 하기
            if graph_tree[i][j] >= 1:
                empty_count = 0
                empty_list = []
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph_tree[nx][ny] == 0:
                            if graph_poison[nx][ny] == -1:
                                empty_count += 1
                                empty_list.append([nx,ny])
                if empty_count != 0:
                    move_tree = graph_tree[i][j] // empty_count
                    for x,y in empty_list:
                        new_graph_tree[x][y] += move_tree
    return new_graph_tree

def find_kill_count(x,y):
    temp_kill = 0
    # 시작점
    temp_kill += graph_tree[x][y]
    temp_kill_pos = [[x,y]]

    # 시작 점이 0 인 경우
    if temp_kill == 0:
        return temp_kill, temp_kill_pos

    # 대각선 4 방향 체크 하기
    for d in range(4):
        # k 까지 확장 / 벽 /0 만나면, 그자리까지 뿌리고 끝남
        for mul in range(1, k+1):
            nx = x + dx_cross[d]*mul
            ny = y + dy_cross[d]*mul
            if 0<=nx<n and 0<=ny<n:
                if graph_tree[nx][ny] >= 1:
                    temp_kill += graph_tree[nx][ny]
                    temp_kill_pos.append([nx,ny])
                elif graph_tree[nx][ny] == 0:
                    temp_kill_pos.append([nx,ny])
                    break
                elif graph_tree[nx][ny] == -1 :
                    break
    return temp_kill, temp_kill_pos


def put_poison():
    max_kill = -1
    max_kill_pos = []
    # 가장 많이 죽이는 부분 찾기
    for i in range(n):
        for j in range(n):
            # 벽다는 못뿌림
            if graph_tree[i][j] == -1 or graph_poison[i][j] == 0 :
                continue

            else:
                temp_kill, temp_kill_pos = find_kill_count(i,j)
                if temp_kill > max_kill:
                    max_kill = temp_kill
                    max_kill_pos = temp_kill_pos
    # 제초제 뿌려주기
    for x,y in max_kill_pos:
        graph_poison[x][y] = c
        graph_tree[x][y] = 0
    return max_kill

def down_poison():
    for i in range(n):
        for j in range(n):
            if graph_poison[i][j] != -1:
                graph_poison[i][j] -= 1

n,m,k,c = map(int,sys.stdin.readline().rstrip().split())
graph_tree = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_poison = [[-1 for _ in range(n)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dx_cross = [1,1,-1,-1]
dy_cross = [1,-1,1,-1]

total_count = 0

for year in range(1, m+1):
    # print("============================")
    # print("year : ", year)
    # 나무 성장
    graph_tree = grow_tree()
    # 나무 번식
    graph_tree = spread_tree()
    # 제초제 뿌리기
    kill_count = put_poison()
    total_count += kill_count
    # 제초제 down
    down_poison()
    #
    # print("나무")
    # for g in graph_tree:
    #     print(g)
    # print("독")
    # for g in graph_poison:
    #     print(g)



print(total_count)

"""
11 446 20 3
0 0 0 -1 57 0 -1 0 0 0 0 
0 18 0 -1 -1 0 0 0 0 0 45 
64 0 10 0 0 -1 74 0 0 33 0 
0 61 0 0 -1 0 0 0 0 0 -1 
0 66 0 0 0 0 0 0 16 0 0 
7 0 0 0 6 0 0 -1 27 72 0 
0 0 0 0 0 54 0 42 -1 -1 0 
0 0 -1 0 0 0 0 1 0 0 98 
-1 98 68 0 0 75 1 93 0 0 0 
0 0 0 0 77 0 0 -1 0 0 0 
0 -1 0 -1 0 0 0 0 45 0 0 


5 1 2 6
0 0 0 0 0
0 0 0 0 0
0 0 -1 0 0
0 0 0 0 0
0 0 0 0 0


"""