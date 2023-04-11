from collections import deque
import sys

"""
1. max 함수를 통해서 결과를 출력할때, 길이가 0인 경우도 고려 해주기

"""
def bfs(x,y, height):
    q = deque()
    q.append([x,y])
    visited[x][y] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in  range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] > height:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = 0


n = int(sys.stdin.readline().rstrip())
graph_ori = []
max_height = 0
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    graph_ori.append(temp)
    max_height = max(max_height,max(temp))

result = []
for h in range(0, max_height+1):
    graph = graph_ori
    visited = [[-1] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h:
                if visited[i][j] == -1:
                    bfs(i,j,h)
                    count += 1
    result.append(count)
if len(result) == 0:
    print(0)
else:
    print(max(result))
