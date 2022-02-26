import sys
from collections import deque
import heapq

# 다익스트라 알고리즘
def bfs(n, graph, visited):
    heap = []
    heapq.heappush(heap, (graph[0][0], 0,0) )
    visited[0][0] = graph[0][0]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while heap:
        cost, a, b = heapq.heappop(heap)  # cost가 가장 적은거 빼내기
        if a == n-1 and b == n-1:
            for k in visited:
                print(k)
            return visited[a][b]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]
                if new_cost < visited[nx][ny]:
                    visited[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

count = 0
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    visited = [[2e10] * n for _ in range(n)]

    result = bfs(n, graph, visited)
    count += 1
    print("Problem {}: {}".format(count, result))