import sys
import heapq

def daik():
    q = []
    count = 0
    heapq.heappush(q,[count, start[0], start[1]])
    visited[start[0]][start[1]] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        for _ in range(len(q)):
            cnt, a,b = heapq.heappop(q)
            if [a,b] == end:
                return count-1
            for i in range(4):
                d = 1
                while 1:
                    nx = a + dx[i]*d
                    ny = b + dy[i]*d
                    if not(0<=nx<n and 0<=ny<m):
                        break
                    if graph[nx][ny] == '*':
                        break
                    if visited[nx][ny] > cnt:
                        visited[nx][ny] = cnt
                        heapq.heappush(q, [count, nx, ny])
                    d += 1
        count += 1
m, n = map(int, sys.stdin.readline().rstrip().split())
graph = []
visited = [[float("inf") for _ in range(m)] for _ in range(n)]
c_point = []
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if graph[i][j] == 'C':
            c_point.append([i,j])

start,end = c_point[0], c_point[1]

result = daik()
print(result)
