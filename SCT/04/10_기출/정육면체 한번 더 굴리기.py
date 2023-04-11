import sys
from collections import deque

def roll_dice(dice_map, direct):
    global dice_num
    a,b,c,d,e,f = dice_map
    new_dice_map = []
    # 6 a / 3 b / 1 c / 4 d / 2 e / 5 f
    # 오른 쪽  3 1 4 6 2 5 / b,c,d,a,e,f
    if direct == 0:
        new_dice_map = [b,c,d,a,e,f]
    # 아래쪽  2,3,5,4,1,6 / e,b,f,d,c,a
    elif direct == 1:
        new_dice_map = [e,b,f,d,c,a]
    # 왼쪽    4,6,3,1,2,5 / d,a,b,c,e,f
    elif direct == 2:
        new_dice_map = [d,a,b,c,e,f]
    # 위쪽    5,3,2,4,6,1 / f,b,e,d,a,c
    elif direct == 3:
        new_dice_map = [f,b,e,d,a,c]
    dice_num = new_dice_map[0]
    return new_dice_map

def move_dice():
    global dice_x,dice_y, dice_direct, dice_map
    x,y = dice_x, dice_y
    nx = x + dx[dice_direct]
    ny = y + dy[dice_direct]
    if not(0<=nx<n and 0<=ny<n):
        dice_direct = (dice_direct+2)%4
        nx = x + dx[dice_direct]
        ny = y + dy[dice_direct]
    # 주사위 굴리기
    dice_map = roll_dice(dice_map, dice_direct)
    dice_x,dice_y = nx,ny

def get_score():
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q.append([dice_x,dice_y])
    visited[dice_x][dice_y] = 1
    count = 1
    now_num = graph[dice_x][dice_y]

    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == now_num:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        count += 1
    score = now_num*count
    return score

def check_direct():
    global dice_direct
    now_num = graph[dice_x][dice_y]
    if dice_num > now_num:
        dice_direct = (dice_direct + 1)%4
    elif dice_num < now_num:
        dice_direct = (dice_direct - 1) % 4

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dice_x,dice_y = 0,0
dice_map = [6,3,1,4,2,5]
dice_direct = 0
dice_num = 6

dx = [0,1,0,-1]
dy = [1,0,-1,0]

total_score = 0
for turn in range(1,m+1):
    # 주사위 이동
    move_dice()
    # 점수 얻기
    score = get_score()
    total_score += score
    # 방향 정하기
    check_direct()



print(total_score)

