import sys


n_list = list(map(int,str(sys.stdin.readline().rstrip())))
count = 0

for i in range(1, len(n_list)):
    if n_list[i-1] != n_list[i]:
        count += 1
print((count+1) // 2)





# from collections import deque
# def bfs(x, target, graph):
#     q = deque()
#     q.append(x)
#     visited[x] = True
#
#     while q:
#         a = q.popleft()
#         nx = a + 1
#         if nx < len(graph):
#             if visited[nx] == False:
#                 if graph[nx] == target:
#                     q.append(nx)
#                     visited[nx] = True
#
# graph_0 = list(map(int,str(sys.stdin.readline().rstrip())))
# graph_1 = [i for i in graph_0]
# visited = [False for _ in range(len(graph_0))]
#
# count_0 = 0
# for i in range(len(graph_0)):
#     if graph_0[i] == 0 and visited[i] == False:
#         bfs(i, 0, graph_0 )
#         count_0 += 1
#
#
# visited = [False for _ in range(len(graph_1))]
# count_1 = 0
# for i in range(len(graph_1)):
#     if graph_1[i] == 1 and visited[i] == False:
#         bfs(i, 1, graph_1 )
#         count_1 += 1
# print(min([count_0, count_1]))
#
#
#
#
