from collections import deque
import sys

def bfs():
    q = deque()
    for s_p in start:
        q.append([s_p[1],s_p[2]])
        visited[s_p[1]][s_p[2]] = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    time = 0
    while q:
        if time == s:
            return graph[x-1][y-1]
        for _ in range(len(q)):
            a,b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        graph[nx][ny] = graph[a][b]
        time += 1
    return graph[x-1][y-1]


n,k = map(int ,sys.stdin.readline().rstrip().split())

graph = []
start = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(temp)
    for j in range(n):
        if graph[i][j] != 0:
            start.append([ graph[i][j],i,j])


start.sort(key = lambda x: x[0])
visited = [ [-1]*n for _ in range(n) ]

# s 초,  x,y 에 바이러스의 종류 출력   없으면 0
s,x,y = map(int ,sys.stdin.readline().rstrip().split())
result = bfs()
print(result)

