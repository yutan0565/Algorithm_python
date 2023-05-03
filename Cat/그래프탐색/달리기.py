import sys
from collections import deque

def run():
    q = deque()
    visited = [[2e10 for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]] = 0
    q.append([start[0],start[1]])
    while q:
        a,b = q.popleft()
        if [a,b] == end:
            return visited[a][b]
        for i in range(4):
            for mul in range(1,k+1):
                nx = a + dx[i]*mul
                ny = b + dy[i]*mul
                if not(0<=nx<n and 0<=ny<m):
                    break
                if graph[nx][ny] == "#":
                    break
                if visited[nx][ny] <= visited[a][b]:
                    break
                if visited[nx][ny] == 2e10:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[a][b] + 1
                    continue
    return -1


n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

x_s,x_y,e_x,e_y = map(int,sys.stdin.readline().rstrip().split())
start = [x_s-1,x_y-1]
end = [e_x-1,e_y-1]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

result = run()
print(result)