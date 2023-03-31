import copy
from collections import deque
import sys

""""
1. graph 가 바뀌는 것에 있어서,  일정 조건이 붙는 경우,  복사본을 만들기
2. 복사본에서 조건을 만족하면 원본에서 바꾸기 !

"""

def is_cheese():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                return -1
    return 1

def bfs():
    q = deque()
    q.append([0,0])
    visited[0][0] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    temp_graph = copy.deepcopy(graph)
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == -1:
                    if temp_graph[nx][ny] == 2:
                        temp_graph[nx][ny] = 1
                    elif temp_graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        visited[nx][ny] = 1
                    elif temp_graph[nx][ny] == 0:
                        q.append([nx,ny])
                        visited[nx][ny] = 1

n,m = map(int, sys.stdin.readline().rstrip().split())
graph = []
reset_visited = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 2

result = 0
while 1:
    visited = copy.deepcopy(reset_visited)
    # for g in graph:
    #     print(g)
    # print()

    if is_cheese() == 1:
        break
    bfs()
    result += 1

print(result)
