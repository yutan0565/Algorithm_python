import copy
import sys
from collections import deque

def spread_pirate_area(nx, ny):
    pirate_area[nx][ny].append(-1)
    for d in range(4):
        x,y= nx,ny
        while 1:
            x = x + dx[d]
            y = y + dy[d]
            if not(0<=x<n and 0<=y<m):
                break
            if graph[x][y] == "I":
                break
            if d in pirate_area[x][y]:
                break
            pirate_area[x][y].append(d)

def move_pirate():
    for _ in range(len(q_pirate)):
        now_pirate_x, now_pirate_y = q_pirate.popleft()
        for d in range(4):
            nx_pirate = now_pirate_x + dx[d]
            ny_pirate = now_pirate_y + dy[d]
            if 0 <= nx_pirate < n and 0 <= ny_pirate < m:
                if visited_pirate[nx_pirate][ny_pirate] == -1:
                    if graph[nx_pirate][ny_pirate] == ".":
                        q_pirate.append([nx_pirate, ny_pirate])
                        visited_pirate[nx_pirate][ny_pirate] = 1
                        spread_pirate_area(nx_pirate, ny_pirate)

def bfs():
    q = deque()
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[sua[0]][sua[1]] = 1
    q.append([sua[0], sua[1]])

    while q:
        move_pirate()
        for _ in range(len(q)):
            now_sua_x, now_sua_y = q.popleft()
            if [now_sua_x, now_sua_y] == treasure:
                return 1
            # 수아가 이동할 수 있는 곳 탐색
            for d in range(4):
                nx_sua = now_sua_x + dx[d]
                ny_sua = now_sua_y + dy[d]
                if 0<=nx_sua<n and 0<=ny_sua<m:
                    if visited[nx_sua][ny_sua] == -1:
                        if graph[nx_sua][ny_sua] == ".":
                            visited[nx_sua][ny_sua] = 1
                            if pirate_area[nx_sua][ny_sua] == []:
                                q.append([nx_sua,ny_sua])
    return 0

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = []
sua, pirate, treasure = [],[],[]
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        # 해적
        if graph[i][j] == "Y":
            sua = [i,j]
            graph[i][j] = "."
        # 수아
        elif graph[i][j] == "V":
            pirate = [i,j]
            graph[i][j] = "."
        # 보물
        elif graph[i][j] == "T":
            treasure = [i,j]
            graph[i][j] = "."

dx = [-1,0,1,0]
dy = [0,1,0,-1]

q_pirate = deque()
visited_pirate = [[-1 for _ in range(m)] for _ in range(n)]
pirate_area = [[[] for _ in range(m)] for _ in range(n)]
visited_pirate[pirate[0]][pirate[1]] = 1
pirate_area[pirate[0]][pirate[1]].append(-1)
q_pirate.append([pirate[0], pirate[1]])
spread_pirate_area(pirate[0], pirate[1])

if bfs():
    print("YES")
else:
    print("NO")

# 수아 먼저 이동
    # 보물 위치에서 끝남
    # 위, 아, 오 , 왼
    # 섬은 접근 불가
# 해적이 이동
# 수아가 해적과 바라 보고 있으면,(그 사이에 섬이 없으면.) 수아 죽음



# import copy
# import sys
# from collections import deque
#
# def spread_pirate_area(nx, ny):
#     pirate_area[nx][ny] = 1
#     for d in range(4):
#         x,y= nx,ny
#         while 1:
#             x = x + dx[d]
#             y = y + dy[d]
#             if not(0<=x<n and 0<=y<m):
#                 break
#             if graph[x][y] == "I":
#                 break
#             pirate_area[x][y] = 1
#
# def move_pirate():
#     for _ in range(len(q_pirate)):
#         now_pirate_x, now_pirate_y = q_pirate.popleft()
#         for d in range(4):
#             nx_pirate = now_pirate_x + dx[d]
#             ny_pirate = now_pirate_y + dy[d]
#             if 0 <= nx_pirate < n and 0 <= ny_pirate < m:
#                 if visited_pirate[nx_pirate][ny_pirate] == -1:
#                     if graph[nx_pirate][ny_pirate] == ".":
#                         q_pirate.append([nx_pirate, ny_pirate])
#                         visited_pirate[nx_pirate][ny_pirate] = 1
#                         spread_pirate_area(nx_pirate, ny_pirate)
#
# def bfs():
#     q = deque()
#     visited = [[-1 for _ in range(m)] for _ in range(n)]
#     visited[sua[0]][sua[1]] = 1
#     q.append([sua[0], sua[1]])
#
#     while q:
#         move_pirate()
#         for _ in range(len(q)):
#             now_sua_x, now_sua_y = q.popleft()
#             if [now_sua_x, now_sua_y] == treasure:
#                 return 1
#             # 수아가 이동할 수 있는 곳 탐색
#             for d in range(4):
#                 nx_sua = now_sua_x + dx[d]
#                 ny_sua = now_sua_y + dy[d]
#                 if 0<=nx_sua<n and 0<=ny_sua<m:
#                     if visited[nx_sua][ny_sua] == -1:
#                         if graph[nx_sua][ny_sua] == ".":
#                             visited[nx_sua][ny_sua] = 1
#                             if pirate_area[nx_sua][ny_sua] == -1:
#                                 q.append([nx_sua,ny_sua])
#     return 0
#
# n,m = map(int,sys.stdin.readline().rstrip().split())
# graph = []
# pirate_area = [[-1 for _ in range(m)] for _ in range(n)]
# sua, pirate, treasure = [],[],[]
# for i in range(n):
#     graph.append(list(sys.stdin.readline().rstrip()))
#     for j in range(m):
#         # 해적
#         if graph[i][j] == "Y":
#             sua = [i,j]
#             graph[i][j] = "."
#         # 수아
#         elif graph[i][j] == "V":
#             pirate = [i,j]
#             graph[i][j] = "."
#         # 보물
#         elif graph[i][j] == "T":
#             treasure = [i,j]
#             graph[i][j] = "."
#
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# q_pirate = deque()
# visited_pirate = [[-1 for _ in range(m)] for _ in range(n)]
# pirate_area = [[-1 for _ in range(m)] for _ in range(n)]
# visited_pirate[pirate[0]][pirate[1]] = 1
# pirate_area[pirate[0]][pirate[1]] = 1
# q_pirate.append([pirate[0], pirate[1]])
# spread_pirate_area(pirate[0], pirate[1])
#
# if bfs():
#     print("YES")
# else:
#     print("NO")
#
# # 수아 먼저 이동
#     # 보물 위치에서 끝남
#     # 위, 아, 오 , 왼
#     # 섬은 접근 불가
# # 해적이 이동
# # 수아가 해적과 바라 보고 있으면,(그 사이에 섬이 없으면.) 수아 죽음
#
