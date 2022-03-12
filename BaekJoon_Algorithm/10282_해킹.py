import sys
from collections import deque
import heapq

def daik(n, d, c, graph, visited):
    heap = []
    heapq.heappush(heap, [c,0])
    visited[c] = 0
    while heap:
        now, time = heapq.heappop(heap)
        for go, go_time in graph[now]:
            new_time = time + go_time
            if visited[go] > new_time:
                visited[go] = new_time
                heapq.heappush(heap,[go, new_time])
    result = [ i for i in visited if i!= 2e10]
    print(len(result), max(result) )

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    # 컴퓨터 수,  의존수,  시작 컴
    n,d,c = map(int, sys.stdin.readline().rstrip().split())

    # 연결, 연결, s초 후 감염
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a,b,s = map(int, sys.stdin.readline().rstrip().split())
        graph[b].append([a,s])

    visited = [2e10]*(n+1)
    daik(n, d, c, graph, visited)



# # def bfs(n, d, c, graph, visited):
# #     heap = []
# #     for g in graph:
# #         if g[1] == c:
# #             heapq.heappush(heap, [0 , g[0] , c ])
# #             visited[c] = 0
# #             print(heap)
# #
# #     while heap:
# #         time, go, now = heapq.heappop(heap)
# #
# #         for g in graph:
# #             if g[0] == go and g[1] == now:
# #                 new_time = time + g[2]
# #                 if new_time < visited[go]:
# #                     visited[go] = new_time
# #                     for g_new in graph:
# #                         if g_new[1] == go:
# #                             heapq.heappush(heap, [new_time ,g_new[0], go])
# #
# #     result = [ i for i in visited if i!= 2e10]
# #     print(len(result), max(result) )
#
# def bfs(n, d, c, graph, visited):
#     heap = []
#     for g in graph:
#         if g[1] == c:
#             heapq.heappush(heap, [g[2] , g[0] , c ])
#             visited[c] = 0
#             visited[g[0]] = g[2]
#
#     while heap:
#         go_time, go, now = heapq.heappop(heap)
#         for g in graph:
#             if g[1] == go:
#                 new_time = go_time + g[2]
#                 print(new_time)
#                 print(visited[go])
#                 if new_time < visited[go]:
#                     visited[go] = new_time
#                     heapq.heappush(heap, [new_time, g[0], go])
#
#     print(visited[1:])
#     result = [ i for i in visited if i!= 2e10]
#     print(len(result), max(result) )
