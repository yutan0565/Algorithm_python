import sys
from collections import deque

def roll_dice(direct):
    global line_row, line_col
    a,b,c,d = line_col
    e,_,f = line_row
    if direct == 0:
        line_col = [a, f, c, e]
        line_row = [b, f, d]
    elif direct == 1:
        line_col = [b, c, d, a]
        line_row = [e, c, f]
    elif direct == 2:
        line_col = [a, e, c, f]
        line_row = [d, e, b]
    elif direct == 3:
        line_col = [d, a, b, c]
        line_row = [e, a, f]


def move_dice():
    global  dice_pos, direct
    nx = dice_pos[0] + dx[direct]
    ny = dice_pos[1] + dy[direct]
    if not(0<=nx<n and 0<=ny<n):
        direct = (direct+2)%4
        nx = dice_pos[0] + dx[direct]
        ny = dice_pos[1] + dy[direct]
    dice_pos = [nx,ny]
    roll_dice(direct)
    now_num = line_row[1]

    if now_num > graph[nx][ny]:
        direct = (direct +1)%4
    elif now_num < graph[nx][ny]:
        direct = (direct - 1)%4
    else:
        pass


def cal_score(number):
    global result, d
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append([dice_pos[0], dice_pos[1]])
    visited[dice_pos[0]][dice_pos[1]] = 1
    now_num = graph[dice_pos[0]][dice_pos[1]]
    count = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == now_num:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        count += 1
    result += count*now_num


line_col = [5,6,2,1]
line_row = [4,6,3]
dx = [0,1,0,-1]
dy = [1,0,-1,0]


n,m = map(int,sys.stdin.readline().rstrip().split())
graph  = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dice_pos = [0,0]
direct = 0
result = 0
for _ in range(m):
    move_dice()
    cal_score(line_col[1])
print(result)

"""
    5a 6b 2c 1d 
    4e 6b 3f

    오른
    a f c e
    b f d
    아래
    b c d a
    e c f
    왼
    a e c f  
    d e b
    위
    d a b c
    e a f
    
    
    
    오른회전
    e b f d
    c b a
    왼쪽 회전
    f b e d
    a b c


    오른
    5 3 2 4
    6 3 1

    아래
    6 2 1 5
    4 2 3

    왼
    5 4 2 3
    1 4 6

    위
    1 5 6 2
    4 5 3

    오른쪽 회전
    4 6 3 1
    2 6 5

    왼쪽 회전
    3 6 4 1
    5 6 2
"""

"""

def spin_dice(di):
    global line_row, line_col
    a,b,c,d = line_col
    e,_,f = line_row
    if di == 1: #시계
        line_col = [e, b, f, d]
        line_row = [c, b, a]
    elif di == -1: #반시계
        line_col = [f, b, e, d]
        line_row = [a, b, c]
"""