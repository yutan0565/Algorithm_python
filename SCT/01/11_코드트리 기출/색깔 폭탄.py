from collections import deque
import sys


def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    color = graph[x][y]
    red = []
    temp_visit = [[x,y]]
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == color:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        temp_visit.append([nx,ny])
                    elif graph[nx][ny] == 0:
                        if [nx,ny] not in red:
                            q.append([nx,ny])
                            red.append([nx,ny])
                            temp_visit.append([nx, ny])

    temp_visit.sort(key = lambda x : (-x[0], x[1]))
    for a,b in temp_visit:
        if graph[a][b] != 0:
            cen = [a,b]
            break
    count = len(temp_visit)
    return count, len(red), cen, temp_visit

def find_bomb_group():
    max_count = -float("inf")
    max_red_count = -float("inf")  # 적은거 부터,
    max_center = [-1,-1] # 행 큰거, 열 작은거
    max_visit = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                if graph[i][j] >= 1:
                    count,red,cen,visit = bfs(i,j)
                    if count < 2:
                        continue
                    if count > max_count:
                        max_count = count
                        max_red_count = red
                        max_center = cen
                        max_visit = visit
                    elif count == max_count:
                        if red < max_red_count:
                            max_count = count
                            max_red_count = red
                            max_center = cen
                            max_visit = visit
                        elif red == max_red_count:
                            if cen[0] > max_center[0]:
                                max_count = count
                                max_red_count = red
                                max_center = cen
                                max_visit = visit
                            elif cen[0] == max_center[0]:
                                if cen[1] < max_center[1]:
                                    max_count = count
                                    max_red_count = red
                                    max_center = cen
                                    max_visit = visit
    return max_visit

def del_bomb(bomb_group):
    for a,b in bomb_group:
        graph[a][b] = -2

def gravity():
    for i in range(n-2,-1,-1):
        for j in range(n-1,-1,-1):
            if graph[i][j] >=0:
                x,y = i,j
                while 1:
                    x += 1
                    if not(0<=x<n):
                        x -= 1
                        break
                    if graph[x][y] != -2:
                        x -= 1
                        break
                graph[x][y], graph[i][j] = graph[i][j], graph[x][y]
def rotation():
    new_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[n-1-j][i] = graph[i][j]
    return new_graph

def count_bomb():
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 0:
                return -1
    return 1
def show_graph():
    print("------------------")
    for g in graph:
        print(g)

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
score = 0
while 1:
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    bomb_group= find_bomb_group()
    if len(bomb_group) == 0:
        break
    del_bomb(bomb_group)
    score += len(bomb_group) * len(bomb_group)
    gravity()
    graph = rotation()
    gravity()

print(score)

"""
-1 검정
0 빨간
1 ~ m 다른 색
"""
