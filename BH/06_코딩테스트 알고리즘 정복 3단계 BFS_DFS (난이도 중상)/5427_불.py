import sys
from collections import deque

def bfs(graph, visited, n, m , fire, start):
    p_q = deque()
    p_q.append(start)
    f_q = deque()
    for f in fire:
        f_q.append(f)
    visited[start[0]][start[1]] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while p_q:
        for _ in range(len(f_q)):
            f_a, f_b = f_q.popleft()
            for i in range(4):
                f_nx = f_a + dx[i]
                f_ny = f_b + dy[i]
                if 0<=f_nx<n and 0<=f_ny<m:
                    if graph[f_nx][f_ny] == '.':
                        graph[f_nx][f_ny] = '*'
                        f_q.append([f_nx, f_ny])
        for _ in range(len(p_q)):
            a,b = p_q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == '.':
                            p_q.append([nx,ny])
                            visited[nx][ny] = visited[a][b] + 1
                else:
                    return visited[a][b] +1
    return -1


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m,n = map(int, sys.stdin.readline().rstrip().split())
    visited = [ [-1 for _ in range(m)] for _ in range(n)]
    graph = []
    fire = []
    start = []
    for i in range(n):
        graph.append(list(sys.stdin.readline().rstrip()))
        for j in range(m):
            if graph[i][j] == '*':
                fire.append([i,j])
            if graph[i][j] == '@':
                start = [i,j]
    result = bfs(graph, visited, n, m , fire, start)
    if result == -1:
        print("IMPOSSIBLE")
    else:
        print(result)