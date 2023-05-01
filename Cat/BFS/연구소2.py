import sys
from collections import deque
from itertools import combinations

def bfs(virus):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    for a,b in virus:
        q.append([a,b])
        visited[a][b] = 1
    count = 0
    while q:
        for _ in range(len(q)):
            a, b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] != 1:
                            q.append([nx, ny])
                            visited[nx][ny] = 1
        count += 1

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] != 1:
                return 2e10
    return count - 1


n, m = map(int, sys.stdin.readline().rstrip().split())
virus_pos = []
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j] == 2:
            virus_pos.append([i,j])

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 2e10
candi_virus_list = list(combinations(virus_pos, m))
for virus in candi_virus_list:
    temp_result = bfs(virus)
    result = min(temp_result,result)

if result == 2e10:
    print(-1)
else:
    print(result)