import copy
from collections import deque
import sys

def bfs():
    q = deque()
    visited = copy.deepcopy(reset_visited)
    visited[0][0] = 1

    q.append([0,0])

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    count = 0
    while q:
        a,b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n+2 and 0<=ny<m+2:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == '.':
                        visited[nx][ny] = 1
                        q.append([nx,ny])
                    elif 'a'<=graph[nx][ny]<='z':
                        if graph[nx][ny] not in key_list:
                            key_list.append(graph[nx][ny])
                            graph[nx][ny] = '.'
                            visited = copy.deepcopy(reset_visited)
                            visited[nx][ny] = 1
                            q.append([nx, ny])
                        else:
                            visited[nx][ny] = 1
                            q.append([nx, ny])
                    elif 'A'<=graph[nx][ny]<='Z':
                        if graph[nx][ny].lower() in key_list:
                            visited[nx][ny] = 1
                            graph[nx][ny] = '.'
                            q.append([nx, ny])
                    elif graph[nx][ny] == '$':
                        graph[nx][ny] = '.'
                        count += 1
                        visited[nx][ny] = 1
                        q.append([nx, ny])
    return count


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n,m = map(int, sys.stdin.readline().rstrip().split())
    empty_line = [['.' for _ in range(m+2)]]
    graph = []

    graph = empty_line + graph
    for _ in range(n):
        graph.append(['.']+list(sys.stdin.readline().rstrip())+['.'])
    graph = graph + empty_line

    key_list = list(sys.stdin.readline().rstrip())
    if key_list == ['0']:
        key_list = []
    reset_visited = [[-1 for _ in range(m+2)] for _ in range(n+2)]
    result = bfs()
    print(result)