import sys
from collections import deque

def update_graph():
    graph =  [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            type =  candi_graph[i][j][0]
            graph[i][j] = type
            candi_graph[i][j].rotate(-1)
    return graph

def bfs(x,y, start_direct):
    q = deque()
    q.append([x,y, start_direct])
    graph = update_graph()

    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    now_time = 0
    total_count = 1
    while q:
        for _ in range(len(q)):
            a,b,now_direct = q.popleft()
            now_type = graph[a][b]

            candi_direct = dict_direct[now_type][1:]
            type_start_direct = dict_direct[now_type][0]

            if now_direct != type_start_direct:
                continue
            for d in candi_direct:
                nx = a + dx[d]
                ny = b + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny,d])
                        visited[nx][ny] = 1
                        total_count += 1
                    if visited[nx][ny] == 1:
                        q.append([nx,ny,d])
        now_time += 1
        graph = update_graph()
        if now_time == t:
            break
    return total_count

n,t = map(int,sys.stdin.readline().rstrip().split())
candi_graph = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        candi_direct_list = list(map(int,sys.stdin.readline().rstrip().split()))
        candi_graph[i][j] = deque(candi_direct_list)

dx = [0,-1,0,1]
dy = [1,0,-1,0]

dict_direct = {}
dict_direct[1] = [0,0,1,3]
dict_direct[2] = [1,0,1,2]
dict_direct[3] = [2,1,2,3]
dict_direct[4] = [3,0,2,3]

dict_direct[5] = [0,0,1]
dict_direct[6] = [1,1,2]
dict_direct[7] = [2,2,3]
dict_direct[8] = [3,0,3]

dict_direct[9] =  [0,0,3]
dict_direct[10] = [1,0,1]
dict_direct[11] = [2,1,2]
dict_direct[12] = [3,2,3]

result = bfs(0,0,1)
print(result)