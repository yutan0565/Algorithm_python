from collections import deque
import sys
from itertools import combinations

"""
바이러스가 도달하는 곳 자체는, 시간을 측정하지 아흠 
그냥 다음 시간부터 활성화 되기 시작하는 하나의 v 로 생각하기

 도달 한 virus가 지금 퍼지고 있는 지점의 끝일 수도 있기 때문에, 시간 측정은 하지 않는다.
 단 다음 경우 ( 바이러스 없는 곳) 에 도달하는 경우에는 time count가 증가할 수 있도록 해주기
"""

def bfs():
    q = deque()
    for v in virus_g:
        q.append(v)
        visited[v[0]][v[1]] = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    time = 0
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        q.append([nx,ny])
                        visited[nx][ny] = visited[a][b] + 1
                        time = max(time, visited[nx][ny])

                    if graph[nx][ny] == 2:
                        q.append([nx,ny])
                        visited[nx][ny] = visited[a][b] + 1

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] == 0:
                return 5000
    else:
        return time

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = []
virus = []
wall_count = 0
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i,j])

virus_case = list(combinations(virus, m))

result = 5000
for virus_g in virus_case:
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    not_virus = [v for v in virus if v not in virus_g]
    temp = bfs()
    result = min(result,temp)

if result == 5000:
    print(-1)
else:
    print(result)
