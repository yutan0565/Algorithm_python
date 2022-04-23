import sys
from collections import deque

def bfs(point,w, h, graph, visited ):
    q = deque()
    x = point[0][0]
    y = point[0][1]
    q.append([x,y])
    visited[x][y]  = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        a,b = q.popleft()

        # 종료 지점
        if a == point[1][0] and b == point[1][1]:
            for v in visited:
                print(v)
            return visited[a][b] - 1

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            while True:
                if not(0<= nx < h and 0 <= ny < w ):
                    break
                if graph[nx][ny] == "*":
                    break
                ###### 무한대 설정
                if visited[nx][ny] < visited[a][b]+1:
                    break
                q.append([nx,ny])
                visited[nx][ny] = visited[a][b] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]

w, h = map(int, sys.stdin.readline().rstrip().split())
graph = []
visited = [ [2e10]*w for _ in range(h) ]
# print(visited)
point = []

for i in range(h):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(temp)
    for j in range(len(temp)):
        if temp[j]== 'C':
            point.append([i,j])
# print(point)

result = bfs(point,w, h, graph, visited )
print(result)




# def bfs(point,w,h, graph, visited):
#     q = deque()
#     x = point[0][0]
#     y = point[0][1]
#     q.append([x,y])
#     visited[x][y]  = True
#     graph[x][y] = 1
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     while q:
#         a, b= q.popleft()
#         if a == point[1][0] and b == point[1][1]:
#             for g in graph:
#                 print(g)
#             return graph[a][b]
#         for k in range(max(w,h),-1,-1):
#             for i in range(4):
#                 nx = a + dx[i]*k
#                 ny = b + dy[i]*k
#                 if 0<= nx < h and 0 <= ny < w :
#                     if graph[nx][ny] != "*":
#                         if visited[nx][ny] == False:
#                             q.append([nx,ny])
#                             visited[nx][ny] = True
#                             new = graph[a][b] + 1
#                             for j in range(k,-1,-1):
#                                 tx = a + dx[i]*j
#                                 ty = b + dy[i]*j
#                                 graph[tx][ty] = new
#                                 visited[tx][ty] = True
#                                 for g in graph:
#                                     print(g)
#
#                                 # for g in graph:
#                                 #     print(g)
#                                 # print()