import sys
from collections import deque

def change_dice(direct):
    a,b,c,d,e,f = dice_map
    if direct == 0:
        new_dice_map = [e, b, c, a, f, d]
    elif direct == 1:
        new_dice_map = [c, a, f, d, e, b]
    elif direct == 2:
        new_dice_map = [d, b, c, f, a, e]
    elif direct == 3:
        new_dice_map = [b, f, a, d, e, c]
    return new_dice_map

def cal_bfs(x,y):
    global total_socre
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    now_number = graph[x][y]
    count = 1
    while q:
        a,b = q.popleft()
        for d in range(4):
            new_x = a + dx[d]
            new_y = b + dy[d]
            if 0<=new_x<n and 0<=new_y<n:
                if visited[new_x][new_y] == -1:
                    if graph[new_x][new_y] == now_number:
                        q.append([new_x, new_y])
                        visited[new_x][new_y] = 1
                        count += 1
    total_socre += (count*now_number)


def spin_dice():
    global dice_map, now_direct, x_dice, y_dice
    nx = x_dice + dx[now_direct]
    ny = y_dice + dy[now_direct]

    # 벗어 나면
    if not(0<=nx<n and 0<=ny<n):
        now_direct = (now_direct + 2)%4
        nx = x_dice + dx[now_direct]
        ny = y_dice + dy[now_direct]

    # 주사위 모양 변경
    dice_map = change_dice(now_direct)

    # 점수 계산
    cal_bfs(nx,ny)

    # 방향 전환
    now_under = dice_map[0]
    now_graph_number = graph[nx][ny]
    if now_under > now_graph_number:
        now_direct = (now_direct + 1)%4
    elif now_under < now_graph_number:
        now_direct = (now_direct - 1) % 4
    else:
        pass
    x_dice,y_dice = nx, ny

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

total_socre = 0
now_direct = 1
x_dice, y_dice = 0,0
dice_map = [6, 4, 3, 2, 5, 1]

for _ in range(m):

    spin_dice()


print(total_socre)
"""
a아래 , b왼, c오, d아, e위, f건너
a b c d e f
6 4 3 2 5 1

위쪽  0
e b c a f d
5 4 3 6 1 2

오른쪽 1 
c a f d e b
3 6 1 2 5 4

아래쪽 2
d b c f a e
2 4 3 1 6 5

왼쪽 3
b f a d e c
4 1 6 2 5 3


4 20
1 2 4 4
4 2 2 2
5 2 6 6
5 3 3 1

4 20
1 2 3 4
4 1 2 3
1 2 3 4
4 1 2 3

"""