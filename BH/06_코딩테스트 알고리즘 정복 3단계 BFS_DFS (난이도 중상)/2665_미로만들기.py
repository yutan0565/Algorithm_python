import sys
import heapq
from collections import deque

def bfs():
    q = []
    heapq.heappush(q,[0,0,0]) # 벽 부순 수 , x, y
    visited[0][0] = True

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        pos, a, b= heapq.heappop(q)
        if a == n-1 and b == n-1:
            return pos
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == False:
                    if graph[nx][ny] == 0:
                        heapq.heappush(q, [pos+1,nx,ny])
                    elif graph[nx][ny] == 1:
                        heapq.heappush(q, [pos, nx, ny])
                    visited[nx][ny] = True

n = int(sys.stdin.readline().rstrip())
graph = []
wall_count = 0

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
    for j in range(n):
        if graph[i][j] == 0:
            wall_count += 1

visited = [ [0 for _ in range(n)]  for _ in range(n)]

result = bfs()
print(result)