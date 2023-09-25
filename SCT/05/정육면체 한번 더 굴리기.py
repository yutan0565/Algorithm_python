import sys
from collections import deque

def roll_dice(direct):
    global dice_list
    a,b,c,d,e,f = dice_list
    # 위 우 아 왼
    # [1,2,3,5,4,6]
    #[a,b,c,d,e,f]

    # [2,6,3,1,4,5]
    #위 [b,f,c,a,e,d]
    if direct == 0:
        dice_list = [b,f,c,a,e,d]
    # [4,2,1,5,6,3]
    #우 [e,b,a,d,f,c]
    elif direct == 1:
        dice_list = [e,b,a,d,f,c]
    # [5,1,3,6,4,2]
    # 아 [d,a,c,f,e,b]
    elif direct == 2:
        dice_list = [d,a,c,f,e,b]
    # [3,2,6,5,1,4]
    # 왼 [c,b,f,d,a,e]
    elif direct == 3:
        dice_list = [c,b,f,d,a,e]

def bfs(x,y):
    global total_score
    q = deque()
    q.append([x,y])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    cnt = 1

    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == graph[x][y]:
                    if visited[nx][ny] == -1:
                        cnt += 1
                        visited[nx][ny] = 1
                        q.append([nx,ny])
    total_score  = total_score + (cnt*graph[x][y])

def change_direct():
    global now_direct
    under_dice = dice_list[-1]
    map_num = graph[dice_x][dice_y]

    # 주사위 아래가 더 큰 경우
    if under_dice > map_num:
        now_direct = (now_direct + 1)%4
    elif under_dice < map_num:
        now_direct = (now_direct - 1) % 4

def simulation():
    global dice_x, dice_y, now_direct
    for round in range(1, m+1):
        dice_x = dice_x + dx[now_direct]
        dice_y = dice_y + dy[now_direct]
        # 범위 벗어나는 경우
        if not(0<=dice_x<n and 0<=dice_y<n):
            # 원래 위치 복구
            dice_x = dice_x - dx[now_direct]
            dice_y = dice_y - dy[now_direct]
            # 방향 전환
            now_direct = (now_direct + 2)%4
            # 다시 이동
            dice_x = dice_x + dx[now_direct]
            dice_y = dice_y + dy[now_direct]
        bfs(dice_x, dice_y)
        roll_dice(now_direct)
        change_direct()

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for  _ in range(n)]
dice_list = [1,2,3,5,4,6]
now_direct = 1
dice_x = 0
dice_y = 0
total_score = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

simulation()
print(total_score)

"""
4 4
1 2 4 4
4 2 2 2
5 2 6 6
5 3 3 1


"""