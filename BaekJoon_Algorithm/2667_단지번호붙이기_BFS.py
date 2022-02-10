"""
1. 방문하지 않은점
2. 그래프를 벗어나지 않은점
3. 0 이 아닌점 (벽같은거)
"""
from collections import deque

import sys
from collections import deque

def bfs(x, y ):
    global graph, visited, n

    d = deque()
    count  = 0
    # 지금 받아온거 넣어주기
    d.append([x,y])
    visited[x][y] = True
    graph[x][y] = -1
    count += 1
    # 동, 남, 서 ,북
    dx = [0,1,0,-1]
    dy = [1,0,-1,0 ]

    while d:
        a, b = d.popleft()  # 다른 변수 사용 해주기
        for i in range(len(dx)):
            nx =  a + dx[i]
            ny =  b + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if visited[nx][ny] != True:
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = -1
                        d.append([nx, ny])
                        visited[nx][ny] = True
                        count += 1
    return count
n = int(sys.stdin.readline().rstrip())
# graph = []
#
# for i in range(n):
#     temp = list(map(int, sys.stdin.readline().split()))
#     graph.append(temp)
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [ [False] * n for _ in range(n)]

result  = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_max  = bfs(i,j)
            result.append(house_max)

print(len(result))
result.sort()

for i in result:
    print(i)
