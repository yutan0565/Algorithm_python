from collections import deque
import sys
"""
1. 특수 이동을 몇번하는가 (벽을 몇번 부수는가)에 따라 결과가 달라지기 때문에, 그에 맞는 visited 생성 !!
2. 몇번 특수 이동을 하고, 그 자리에서 어떻게 이동하는가는 항상 다르기 때문에,
- 특수 이동 경우 / 그냥   단순 이분법으로 나누면 답이 틀림 !
3. 벽을 부수는 거도 똑같음 !! 
"""
def bfs():
    q = deque()
    count = 0
    q.append([start[0], start[1],count])
    visited[start[0]][start[1]][count] = 0

    dx_horse = [2,2,-2,-2,1,1,-1,-1]
    dy_horse = [1,-1,1,-1,2,-2,2,-2]

    dx_mon = [0,0,1,-1]
    dy_mon = [1,-1,0,0]

    while q:
        a,b, cnt= q.popleft()
        if [a,b] == end:
            return visited[a][b][cnt]

        if cnt < k:
            for i in range(8):
                nx = a + dx_horse[i]
                ny = b + dy_horse[i]
                if 0<=nx<h and 0<=ny<w :
                    if visited[nx][ny][cnt+1] == -1:
                        if graph[nx][ny] == 0:
                            q.append([nx, ny, cnt + 1])
                            visited[nx][ny][cnt+1] = visited[a][b][cnt] + 1

        for i in range(4):
            nx = a + dx_mon[i]
            ny = b + dy_mon[i]
            if 0<=nx<h and 0<=ny<w :
                if visited[nx][ny][cnt] == -1:
                    if graph[nx][ny] == 0:
                        q.append([nx,ny, cnt])
                        visited[nx][ny][cnt] = visited[a][b][cnt] +1
    return -1


k = int(sys.stdin.readline().rstrip())
w,h = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
visited = [ [[-1 for _ in range(k+1)] for _ in range(w)] for _ in range(h)]

start = [0,0]
end = [h-1, w-1]

result = bfs()
print(result)


