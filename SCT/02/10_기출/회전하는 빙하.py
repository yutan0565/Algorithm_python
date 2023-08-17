import copy
import sys
from collections import deque

def rotation_right(level):
    total_size = 2**level
    group_size = total_size // 2
    new_graph = [[0 for _ in range(map_len)] for _ in range(map_len)]
    # 움직임 네모 칸의 시작점 / 회전 변화 없이 그대로
    for start_x in range(0,map_len, total_size):
        for start_y in range(0,map_len, total_size):
            # 그 안에서 4개의 그룹으로 나눈  시작 위치  // 회전 하게될 그룹 단위
            for i in range(0, total_size, group_size):
                for j in range(0, total_size, group_size):
                    new_group_x = start_x + j
                    new_group_y = start_y + total_size -group_size -i
                    # 움직인 그룹안에 있는 것들을 회전 시키기
                    for a in range(group_size):
                        for b in range(group_size):
                            nx = new_group_x + a
                            ny = new_group_y+ b
                            new_graph[nx][ny]  = graph[start_x+i+a][start_y+j+b]
    return new_graph


def melt_down():
    new_graph = copy.deepcopy(graph)
    for i in range(map_len):
        for j in range(map_len):
            if graph[i][j] != 0:
                count = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<map_len and 0<=ny<map_len:
                        if graph[nx][ny] != 0:
                            count += 1
                if count < 3:
                    if graph[i][j] !=0:
                        new_graph[i][j] -= 1
    return new_graph

def cal_ice():
    count = 0
    for i in range(map_len):
        for j in range(map_len):
            if graph[i][j] != 0:
                count += graph[i][j]
    return count


def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    count = 1
    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0 <= nx < map_len and 0 <= ny < map_len:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] != 0:
                        count += 1
                        q.append([nx,ny])
                        visited[nx][ny] = 1
    return count

def find_big_group():
    max_count = 0
    for i in range(map_len):
        for j in range(map_len):
            if visited[i][j] == -1:
                if graph[i][j] != 0:
                    count = bfs(i,j)
                    max_count = max(max_count, count)
    return max_count


n,turn = map(int,sys.stdin.readline().rstrip().split())
map_len = 2**n
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(map_len)]
level_list = list(map(int,sys.stdin.readline().rstrip().split()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for level in level_list:
    # 돌리기
    if level != 0:
        graph = rotation_right(level)
    # 녹이기
    graph = melt_down()

# 빙향의 총량
ice_count = cal_ice()
# 가장 큰 그룹
visited = [[-1 for _ in range(map_len)] for _ in range(map_len)]
big_group = find_big_group()

print(ice_count)
print(big_group)