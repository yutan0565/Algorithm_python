import copy
from collections import deque
import sys

def bfs():
    global time, shark_size, eat_stack
    q = deque()
    q.append(shark_start + [0] )
    visited[shark_start[0]][shark_start[1]] = 0
    graph[shark_start[0]][shark_start[1]] = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    cand_list = []

    while q:
        for _ in range(len(q)):
            a,b, dis = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny]  == 0 or graph[nx][ny] == shark_size:
                        if visited[nx][ny] == -1:
                            q.append([nx,ny, dis+1])
                            visited[nx][ny] = dis + 1
                    elif 0 < graph[nx][ny] < shark_size:
                        if visited[nx][ny] == -1:
                            cand_list.append([nx,ny, dis + 1])
                            visited[nx][ny] = dis + 1

        if len(cand_list) != 0:
            cand_list.sort(key = lambda x: (x[0], x[1]))
            new_start = cand_list[0][:2]
            time += cand_list[0][2]
            eat_stack += 1
            if eat_stack == shark_size:
                shark_size += 1
                eat_stack = 0
            graph[new_start[0]][new_start[1]] = 0
            return new_start
    return [-1, -1]


n = int(sys.stdin.readline().rstrip())
graph = []
shark_start = []
time = 0
shark_size = 2
eat_stack = 0

reset_visited = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j] == 9:
            shark_start = [i,j]

while 1:
    visited = copy.deepcopy(reset_visited)
    shark_start = bfs()
    if shark_start == [-1,-1]:
        break
print(time)




