import copy
import sys

def grow_tree():
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1:
                count = 0
                for d in range(4):
                    nx = i + dx_check[d]
                    ny = j + dy_check[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] >= 1:
                            count += 1
                new_graph[i][j] += count
    return new_graph

def spread_tree():
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1:
                count = 0
                candi_pos = []
                for d in range(4):
                    nx = i + dx_check[d]
                    ny = j + dy_check[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] == 0:
                            if graph_dead[nx][ny] == -1:
                                count += 1
                                candi_pos.append([nx,ny])
                if len(candi_pos) != 0:
                    gap = graph[i][j] // count
                    for x,y in candi_pos:
                        new_graph[x][y] += gap
    return new_graph

def find_kill_count(x,y):
    temp_kill, temp_kill_list = graph[x][y], [[x,y]]
    for d in range(4):
        for mul in range(1, k+1):
            nx = x + dx[d]*mul
            ny = y + dy[d]*mul
            if 0<=nx<n and 0<=ny<n:
                # 성이 나오는 경우
                if graph[nx][ny] == -1:
                    break
                # 빈칸 나오는 경우
                elif graph[nx][ny] == 0:
                    temp_kill_list.append([nx,ny])
                    break
                # 나무 있는 경우
                else:
                    temp_kill_list.append([nx, ny])
                    temp_kill += graph[nx][ny]
    return temp_kill, temp_kill_list


def spread_poison():
    # 최적 지점 찾기
    max_kill = 0
    max_kill_list = [[0,0]]
    for i in range(n):
        for j in range(n):
            # 나무 있는 곳
            if graph[i][j] >= 1:
                temp_kill, temp_kill_list = find_kill_count(i,j)
                if temp_kill > max_kill:
                    max_kill = temp_kill
                    max_kill_list = temp_kill_list

    # 실제로 뿌리기
    for x,y in max_kill_list:
        graph_dead[x][y] = c
        graph[x][y] = 0
    return max_kill

def down_poison():
    for i in range(n):
        for j in range(n):
            if graph_dead[i][j] != -1:
                graph_dead[i][j] -= 1

# 격자 크기,  박멸 진행 년수,  제초제 범위,  제조제 남아있는 년 수
n,m,k,c = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_dead = [[-1 for _ in range(n)] for _ in range(n)]

dx_check = [0,0,1,-1]
dy_check = [1,-1,0,0]

dx = [1,1,-1,-1]
dy = [1,-1,1,-1]
total_kill = 0
for year in range(1,m+1):
    # 인접 나무 칸 수 만큼, 나무 성장
    graph = grow_tree()
    # 벽/나무/제초제 없는 만큼 번식
    graph = spread_tree()
    # 독 뿌리기
    kill_count = spread_poison()
    total_kill += kill_count
    # 독 감소
    down_poison()
print(total_kill)