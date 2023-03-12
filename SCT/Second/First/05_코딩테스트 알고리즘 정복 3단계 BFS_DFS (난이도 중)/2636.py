from collections import deque
import sys

def check_cheese():
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
    return count

def bfs():
    q = deque()
    q.append([0,0])
    visited[0][0] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                if graph[nx][ny] == 1:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = 1
                        graph[nx][ny] = 0
    return check_cheese()



n,m = map(int, sys.stdin.readline().rstrip().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(m):
        pass


result_time = 0
result_list = [check_cheese()]
while 1:
    visited = [[-1 for i in range(m)] for j in range(n)]
    if check_cheese() == 0:
        break
    else:
        temp = bfs()
        result_list.append(temp)
        result_time += 1
print(result_time)
print(result_list[result_time-1])