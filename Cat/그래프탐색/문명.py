import sys
from collections import deque

def spread_mun(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    new_pos = []
    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 1:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                    elif graph[nx][ny] == 0:
                        new_pos.append([nx,ny])
    return new_pos


n,k = map(int,sys.stdin.readline().rstrip().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
graph_group = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(k):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    a,b = a-1,b-1
    graph[a][b] = 1


result = 0
while 1:
    # 근처면은 하나로 결합
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    g_count = 0
    go_pos = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                if visited[i][j] == -1:
                    new_pos = spread_mun(i,j)
                    go_pos = go_pos + new_pos
                    g_count += 1
    # 그룹 개수 1개면은 끝
    if g_count == 1:
        break
    # 채워 주기
    for x,y in go_pos:
        graph[x][y] = 1

    result += 1
print(result)
