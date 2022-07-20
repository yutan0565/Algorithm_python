import sys
from collections import deque

# 상하 반전이 문제에 영향을 끼치진 않는 경우도 고려 해주기!!

def bfs(graph, m, n, i, j):
    q = deque()
    q.append([i,j])
    graph[i][j] = 1
    count = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx  = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and ny >=0 and nx < m and ny < n:
                if graph[nx][ny] == 0:
                    q.append([nx,ny])
                    graph[nx][ny] = 1
                    count += 1
    return count


m,n,k = map(int,sys.stdin.readline().rstrip().split()) # 좌표는 상하 뒤집기!

graph = [ [0]*n for _ in range(m)]

for _ in range(k):
    x,y,end_x,end_y = map(int, sys.stdin.readline().rstrip().split())
    for i in range(y, end_y):
        for j in range(x, end_x):
            graph[i][j] = -1

temp = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result = bfs(graph, m, n, i, j)
            temp.append(result)

temp.sort()
print(len(temp))
for a in temp:
    print(a, end = " ")

#
#
# def bfs(graph,  m, n, x, y):
#     q = deque()
#     q.append([x,y])
#     count = 2
#     graph[x][y] = count
#     r_x, r_y = 0, 0
#
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     while q:
#         a,b = q.popleft()
#         for i in range(4):
#             nx  = a + dx[i]
#             ny = b + dy[i]
#             if nx >= 0 and ny >=0 and nx < m and ny < n:
#                 if graph[nx][ny] == 0:
#                     if graph[nx][ny] != 1:
#                         q.append([nx,ny])
#                         r_x, r_y = nx, ny
#                         count += 1
#                         graph[nx][ny] = count
#     print()
#     for g in graph:
#         print(g)
#
#     return graph[r_x][r_y] - 1
#
#
#
# m,n,k = map(int,sys.stdin.readline().rstrip().split())
#
# graph = [ [0]*n for _ in range(m)]
#
# for _ in range(k):
#     x,y,end_x,end_y = map(int, sys.stdin.readline().rstrip().split())
#
#     a = x
#     b = n - y
#     end_a =  end_x
#     end_b = n - end_y
#
#     for i in range( m - end_y , m - y ):
#         for j in range(x, end_x):
#             graph[i][j] = 1
#
# temp = []
# for i in range(m):
#     for j in range(n):
#         if graph[i][j] == 0 and graph[i][j] != 1:
#             result = bfs(graph, m, n, i, j)
#             temp.append(result)
# temp.sort()
#
# print(len(temp))
# for a in temp:
#     print(a, end = " ")
