from collections import deque
import sys

"""
1. 새롭게 방문하는 곳이, 지금보다 최적경로로 먼저 방문한 곳이면 안갈거야 !
        (새로 방문하는 곳은, 다른 곳에 의해 방문 했던 곳이어야함 )
        (방문을 안한 곳이면, 당연히 지급 있는 곳보다 숫자가 작을거임 !!)
2. 일렬로 쭉 가는 방식 기억 해두기 
"""

def bfs():
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        if [a,b] == end:
            return visited[a][b] -1
        for i in range(4):
            d = 1
            while 1:
                nx = a + dx[i]*d
                ny = b + dy[i]*d
                if not(0<=nx<h and 0<=ny<w) :
                    break
                if graph[nx][ny] == '*':
                    break
                if visited[nx][ny] < visited[a][b] + 1 and visited[nx][ny] != -1:
                    break
                q.append([nx, ny])
                visited[nx][ny] = visited[a][b] + 1
                d += 1


w,h = map(int, sys.stdin.readline().rstrip().split())
graph = []
block = []
for i in range(h):
    graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(w):
        if graph[i][j] == 'C':
            block.append([i,j])

visited = [[-1 for _ in range(w)] for _ in range(h)]

start = block[0]
end = block[1]

result = bfs()

print(result)