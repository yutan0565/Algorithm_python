import copy
from collections import deque
import sys

# 술래 움직이는 칸 만들기
def make_sull_direct():
    dx_sull_f = [-1, 0, 1, 0]
    dy_sull_f = [0, 1, 0, -1]
    dx_sull_s = [0, -1, 0, 1]
    dy_sull_s = [1, 0, -1, 0]

    dx = []
    dy = []

    while 1:
        d_index = 0
        for move_len in range(1, n):
            for _ in range(2):
                for _ in range(move_len):
                    dx.append(dx_sull_f[d_index])
                    dy.append(dy_sull_f[d_index])
                    if len(dx) == k+1:
                        return dx,dy
                d_index = (d_index + 1)%4

        for _ in range(n-1):
            dx.append(dx_sull_f[0])
            dy.append(dy_sull_f[0])
            if len(dx) == k+1:
                return dx, dy

        for _ in range(n-1):
            dx.append(dx_sull_s[3])
            dy.append(dy_sull_s[3])
            if len(dx) == k+1:
                return dx, dy
        d_index = 0
        for move_len in range(n-1, 0,-1):
            for _ in range(2):
                for _ in range(move_len):
                    dx.append(dx_sull_s[d_index])
                    dy.append(dy_sull_s[d_index])
                    if len(dx) == k+1:
                        return dx,dy
                d_index = (d_index + 1)%4


def move_theif(theif_num):
    theif_info = dict_theif[theif_num]
    dx_direct, dy_direct = [], []
    if theif_info[2] == 1:  # 좌 우
        dx_direct = dx_right_left
        dy_direct = dy_right_left
    else:
        dx_direct = dx_down_up
        dy_direct = dy_down_up

    nx = theif_info[0] + dx_direct[theif_info[3]]
    ny = theif_info[1] + dy_direct[theif_info[3]]
    if 0<=nx<n and 0<=ny<n:
        if [nx,ny] == [sull_x, sull_y]:
            pass
        else:
            theif_info[0] = nx
            theif_info[1] = ny
    else:
        if theif_info[3] == 0:
            theif_info[3] = 1
        else:
            theif_info[3] = 0
        nx = theif_info[0] + dx_direct[theif_info[3]]
        ny = theif_info[1] + dy_direct[theif_info[3]]
        if [nx,ny] == [sull_x, sull_y]:
            pass
        else:
            theif_info[0] = nx
            theif_info[1] = ny


def find_move_theif():
    global graph
    q = deque()
    q.append([sull_x, sull_y])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[sull_x][sull_y] = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        if visited[a][b] > 3:
            break
        if len(graph[a][b]) != 0:
            for t in graph[a][b]:
                move_theif(t)
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[a][b] + 1
    graph = copy.deepcopy(reset_graph)
    for t_n in dict_theif.keys():
        graph[dict_theif[t_n][0]][dict_theif[t_n][1]].append(t_n)


def move_sull(sull_index):
    global sull_x, sull_y
    sull_x = sull_x +dx_sull[sull_index]
    sull_y = sull_y +dy_sull[sull_index]

def del_theif(del_list):

    for member in del_list:
        del dict_theif[member]

def find_theif(round):
    global result
    see_direct = round

    x_see_point = sull_x
    y_see_point = sull_y

    for _ in range(3):
        if len(graph[x_see_point][y_see_point]) != 0:
            if [x_see_point,y_see_point] not in tree_list:
                result += (len(graph[x_see_point][y_see_point]) * round)
                del_theif(graph[x_see_point][y_see_point])
                graph[x_see_point][y_see_point] = []
        x_see_point += dx_sull[see_direct]
        y_see_point += dy_sull[see_direct]
        if not(0<=x_see_point<n and 0<=y_see_point<n):
            break

n,m,h,k = map(int, sys.stdin.readline().rstrip().split())
reset_graph = [[[] for _ in range(n)] for _ in range(n)]  # type, 방향 index
dict_theif = {}

graph = copy.deepcopy(reset_graph)
for theif_number in range(1,m+1):
    a,b, type = map(int, sys.stdin.readline().rstrip().split())
    graph[a-1][b-1].append(theif_number)
    dict_theif[theif_number] = [a-1,b-1,type,0]

tree_list = []
for _ in range(h):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    tree_list.append([a-1,b-1])

dx_sull,dy_sull = make_sull_direct()
sull_x, sull_y = n//2, n//2
dx_right_left = [0,0]
dy_right_left = [1,-1]
dx_down_up = [1,-1]
dy_down_up = [0,0]

result = 0

for round in range(1, k+1):

    find_move_theif()

    move_sull(round-1)

    find_theif(round)

print(result)
"""
- n x n 격자 중앙에 술래 (n//2)
- 도망자 : m 명  -- 중앙에서는 시작 x
    - 좌우(우 시작)  or  상하(아래 시작)
- 나무 : h 개  -- 도망자와 겹치는거도 가능

순서  : k 번 반복
- 도망자 움직임(동시)  --  술래와 거리가 3이하인 경우만 움직임(술래 제외 )
    - 격자 안에
        - 움직이려는 칸에 술래 있으면 움직임 x
        - 나무는 이동 가능 o
        - 아무거것도 없어도 가능 o
    - 격자 밖
        - 방향을 반대로 틀어줌
        - 반대쪽에 술래 없으면 1칸 이동

- 술래 움직임
    - 위 / 우 / 아 / 좌
    - 1 1 2 2  3 3 4 4    (n//2)번   위로  4
    - 위 /우 /아 아 /좌 좌 /위 위 위 / 우 우 우 / 아 아 아 아 

    - 우 / 위 / 좌 / 아
    - 아래로 4    4 4 3 3 2 2 1 1  (n//2번 반복)

    - 움직이는 방향에 있는 도둑을 모두 잡음(술래 포함 3 카)
        - 나무가 있으면, 도둑을 못잡음
        - t번째 턴이면 /  t x 도망자 수    만큼 점수 얻음
        - 그 도둑은 사라짐
        
5 24 20 82
4 5 2
2 1 1
1 4 2
2 5 1
1 1 1
1 3 1
5 3 1
3 1 2
3 5 2
4 4 2
4 3 2
2 2 2
3 2 2
1 2 2
1 5 1
5 1 1
4 1 2
2 3 2
2 4 1
5 4 1
5 2 2
4 2 2
3 4 1
5 5 1
3 2
3 5
2 2
4 2
3 3
5 4
3 4
5 5
2 4
2 3
1 1
2 5
5 1
1 2
5 3
4 4
2 1
4 5
1 4
4 3

"""