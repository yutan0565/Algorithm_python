import sys
from collections import deque

def bfs_find_base(x,y):
    q = deque()
    q.append([x,y])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    candi_list = []
    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == 0:
                            q.append([nx,ny])
                            visited[nx][ny] = 1
                        elif graph[nx][ny] == 1:
                            candi_list.append([nx,ny])
                            visited[nx][ny] = 1
        if len(candi_list) != 0:
            break
    return candi_list

def find_base(people):
    mart_x, mart_y = dict_mart[people]
    candi_base = bfs_find_base(mart_x, mart_y)
    candi_base.sort(key = lambda x:(x[0],x[1]))
    base = candi_base[0]
    graph[base[0]][base[1]] = 9
    dict_base[people] = base

def go_to_mart(people):
    x,y = dict_base[people]
    end = dict_mart[people]

    q = deque()
    q.append([x,y])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 0
    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            if [a, b] == end:
                graph[a][b] = 5
                return visited[a][b]
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == 0 or graph[nx][ny] == 1:
                            q.append([nx,ny])
                            visited[nx][ny] = visited[a][b] + 1

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

dict_mart = {}
dict_base = {}
list_done = [0 for _ in range(m+1)]
for number in range(1, m+1):
    mart_x, mart_y = map(int,sys.stdin.readline().rstrip().split())
    dict_mart[number] = [mart_x-1, mart_y-1]
    list_done[number] = 1

result = 1
for now_time in range(1, m+1):
    find_base(now_time)

    move_time = go_to_mart(now_time)
    total_time = now_time + move_time
    result = max(result, total_time)



print(result)