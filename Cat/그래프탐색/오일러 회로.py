import sys
from collections import deque
def dfs(x):
    s = []
    s.append(0)
    result = []

    while s:
        a = s[-1]
        if len(graph[a]) != 0:
            nx = next(iter(graph[a]))
            visited[a][nx] -= 1
            visited[nx][a] -= 1
            if visited[a][nx] == 0:
                del graph[a][nx]
                del graph[nx][a]
            s.append(nx)
        else:
            result.append(s.pop()+1)
    return result

n = int(sys.stdin.readline().rstrip())
visited = []

odd_flag = 1
for i in range(n):
    visited.append(list(map(int,sys.stdin.readline().rstrip().split())))
    if sum(visited[i]) % 2 != 0:
        odd_flag = 0
        break

if odd_flag == 0:
    print(-1)
else:
    graph = [dict() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            num_line = visited[i][j]
            if num_line != 0:
                for _ in range(num_line):
                    graph[i][j] = i
    result  = dfs(0)
    for v in result:
        print(v, end = " ")
