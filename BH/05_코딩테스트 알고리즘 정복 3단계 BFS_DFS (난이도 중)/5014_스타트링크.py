import sys
from collections import deque

def bfs(graph,f,s,g,u,d ):
    q = deque()
    q.append(s)
    graph[s] = 0

    while q:
        a = q.popleft()
        if a == g:
            return graph[a]
        for nx in [ a + u, a - d]:
            if 1<= nx < f+1:
                if graph[nx] == -1:
                    q.append(nx)
                    graph[nx] = graph[a] + 1
    warning = "use the stairs"
    return warning

f,s,g,u,d = map(int, sys.stdin.readline().rstrip().split())

# 총 층수, 시작, 목표,  위로 u , d층으로 이동

graph = [-1] * (f+1)

print(bfs(graph,f,s,g,u,d ))