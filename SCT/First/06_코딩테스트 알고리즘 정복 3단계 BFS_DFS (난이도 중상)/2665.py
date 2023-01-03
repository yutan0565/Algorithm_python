from collections import deque
import heapq
import sys
"""
1. heapq 구조 ->  가장 작은거를 먼저 뽑아야 하는 경우 !!
2. 첫번째 원소를 기준으로 뽑아냄 ~~
"""
def bfs():
    q = []
    heapq.heappush(q, [0,0,0])
    visited[0][0] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        b_w_block, a,b = heapq.heappop(q)
        if a == n-1 and b == n-1:
            return b_w_block
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        heapq.heappush(q, [b_w_block + 1,nx,ny])
                        visited[nx][ny] = 1
                    elif graph[nx][ny] == 1:
                        heapq.heappush(q, [b_w_block, nx, ny ])
                        visited[nx][ny] = 1


n = int(sys.stdin.readline().rstrip())
graph = [ list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n) ]
visited = [ [-1 for _ in range(n)] for _ in range(n) ]

result = bfs()
print(result)
