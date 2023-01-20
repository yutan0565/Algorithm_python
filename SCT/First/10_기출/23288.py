import sys
from collections import deque

def roll_dice():
    global  now_direct, now_under, now_x, now_y, result

    nx = now_x + dx[now_direct]
    ny = now_y + dy[now_direct]
    if not(0<=nx<n and 0<=ny<m):
        print("Sss")
        now_direct = (now_direct + 2)%4
        nx = now_x + dx[now_direct]
        ny = now_y + dy[now_direct]

    # 수사위 밑 업데이트
    now_under = dice_dict[now_under][now_direct]
    graph_number = graph[nx][ny]
    # 굴러간 곳에서 첨수 취득
    count = cal_score(nx, ny, graph_number)
    result += count*graph_number

    print(now_under, graph_number)
    if now_under > graph_number:
        now_direct = (now_direct + 1)%4
    elif now_under< graph_number:
        now_direct = (now_direct - 1) % 4
    elif now_under == graph_number:
        pass

    now_x = nx
    now_y = ny
    # 연속 된 구할 곳의 숫자
    return graph_number

def cal_score(x, y, number):
    q = deque()
    q.append([x,y])
    visited = [[-1 for _ in range(m)] for _ in range(n)]

    visited[x][y] = 1
    count = 1

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == number:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        count += 1
    return count
dice_dict = {1:[3,2,4,5], 2:[3,1,4,6], 3:[6,5,1,2],
             4:[1,5,6,2], 5:[3,6,4,1], 6:[3,2,4,5]}

dx = [0,1,0,-1]
dy = [1,0,-1,0]

now_under = 6
now_direct = 0

now_x = 0
now_y = 0

n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

result = 0
roll_count = 0
while 1:
    number = roll_dice()
    roll_count += 1
    print(roll_count)
    if roll_count == k:
        break
print(result)