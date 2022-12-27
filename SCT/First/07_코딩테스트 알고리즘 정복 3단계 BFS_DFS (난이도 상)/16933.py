from collections import deque
import sys

def bfs():
    q = deque()
    q.append([0,0,0,-1])
    visited[0][0][0] = 1
    # day = -1  night = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    count = 1

    while q:
        count += 1
        for _ in range(len(q)):
            a, b, block, type = q.popleft()
            if a == n - 1 and b == m - 1:
                return visited[a][b][block]

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if visited[nx][ny][block] == -1:
                        if graph[nx][ny] == 0:
                            q.append([nx, ny, block, -type])
                            visited[nx][ny][block] = count
                        elif block+1 <=k and visited[nx][ny][block+1] == -1:
                            if type == -1:
                                q.append([nx, ny, block + 1, -type])
                                visited[nx][ny][block + 1] = count
                            else:
                                q.append([a, b, block, -type])
                                visited[a][b][block] = count

    return -1

n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited = [[[-1 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

result = bfs()
print(result)