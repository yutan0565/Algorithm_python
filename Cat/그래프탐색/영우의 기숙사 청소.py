import sys
from collections import deque

def bfs():
    q = deque()
    for x,y in poison_list:
        q.append([x, y, 0])
    while q:
        # 위치와 거리
        x, y, dis = q.popleft()
        if dis >= 10001:
            break
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[(dis + 1) % 2][nx][ny] == 10001:
                    graph[(dis + 1) % 2][nx][ny] = dis + 1
                    q.append([nx, ny, dis + 1])
    claen_flag = 0
    for x, y in check_pos:
        if graph[t % 2][x][y] <= t:
            claen_flag = 1
            break
    return claen_flag

n, m, k, t = map(int, sys.stdin.readline().rstrip().split())
poison_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
check_pos = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(k)]

graph = [[[10001 for _ in range(n+1)] for _ in range(n+1)] for _ in range(2)]
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

claen_flag = bfs()

if claen_flag == 1:
    print("YES")
elif claen_flag == 0:
    print("NO")