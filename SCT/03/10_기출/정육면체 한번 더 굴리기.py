import sys
from collections import deque

def roll_dice(direct, list):
    a,b,c,d,e,f = list
    new_list = []
    # 오 / 아 / 왼 / 위
    if direct == 0:
        new_list = [b, c, d, a, e, f]
    elif direct == 1:
        new_list = [e, b, f, d, c, a]
    elif direct == 2:
        new_list = [d, a, b, c, e, f]
    elif direct == 3:
        new_list = [f, b, e, d, a, c]
    return new_list
    """
    6 3 1 4 2 5
    a b c d e f   
    오
    3 1 4 6 2 5
    [b,c,d,a,e,f]
    아
    2 3 5 4 1 6
    [e,b,f,d,c,a]
    왼
    4 6 3 1 2 5
    [d,a,b,c,e,f]
    위
    5 3 2 4 6 1
    [f,b,e,d,a,c]
    """

def move_dice():
    global  now_direct, dice_x, dice_y, now_dice
    x,y = dice_x, dice_y
    nx = x + dx[now_direct]
    ny = y + dy[now_direct]
    if not(0<=nx<n and 0<=ny<n):
        now_direct = (now_direct + 2)%4
        nx = x + dx[now_direct]
        ny = y + dy[now_direct]

    now_dice = roll_dice(now_direct, now_dice)
    dice_x,dice_y = nx,ny

def get_score():
    global total_score
    q = deque()
    x,y = dice_x, dice_y
    q.append([x,y])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    graph_num = graph[x][y]
    count = 1
    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == graph_num:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        count += 1
    temp_score = (graph_num*count)
    total_score += temp_score

def get_new_direct():
    global now_direct
    graph_num = graph[dice_x][dice_y]
    dice_num = now_dice[0]
    if dice_num > graph_num:
        now_direct = (now_direct + 1)%4
    elif dice_num < graph_num:
        now_direct = (now_direct -1)%4

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

now_direct = 0
now_dice = [6,3,1,4,2,5]
dice_x, dice_y = 0,0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

total_score = 0
for turn in range(1,m+1):
    # 주사위 움직임
    move_dice()
    # 점수 취득
    get_score()
    # 방향 전환
    get_new_direct()
print(total_score)

"""
4 6
1 3 4 4
4 2 2 2
5 2 6 6
5 3 3 1

"""