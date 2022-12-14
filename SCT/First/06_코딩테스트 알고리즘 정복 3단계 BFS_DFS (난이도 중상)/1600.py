from collections import deque
import sys

def bfs():
    q = deque()
    q.append([start[0], start[1], 0])
    visited[start[0]][start[1]] = 0

    dx_horse = [2,2,-2,-2,1,1,-1,-1]
    dy_horse = [1,-1,1,-1,2,-2,2,-2]

    dx_mon = [0,0,1,-1]
    dy_mon = [1,-1,0,0]

    dx = dx_horse + dx_mon
    dy = dy_horse + dy_mon

    while q:
        a,b, count = q.popleft()
        if [a,b] == end:
            return visited[a][b]
        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<h and 0<=ny<w:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        if count < k and 0<=i<8: #말처럼
                                print(count)
                                q.append([nx,ny, count + 1])
                                visited[nx][ny] = visited[a][b] + 1
                        else: #원숭이
                            q.append([nx,ny, count])
                            visited[nx][ny] = visited[a][b] + 1
    return -1


k = int(sys.stdin.readline().rstrip())
w,h = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
visited = [ [-1 for _ in range(w)] for _ in range(h)]

start = [0,0]
end = [h-1, w-1]

result = bfs()
for v in visited:
    print(v)

print(result)