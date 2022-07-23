import sys
from collections import deque

def bfs(graph, n, k, limit):
    q = deque()
    q.append(n)
    graph[n] = 0

    while q:
        a = q.popleft()
        if a == k:
            return graph[a]

        if 0 < a*2 < limit and graph[a*2] == -1:
            graph[a*2] = graph[a]
            q.append(a*2)

        if 0 <= a-1 < limit and graph[a-1] == -1:
            graph[a-1] = graph[a] + 1
            q.append(a-1)

        if 0 <= a+1 < limit and graph[a+1] == -1:
            graph[a+1] = graph[a] + 1
            q.append(a+1)



n,k = map(int, sys.stdin.readline().rstrip().split())
limit = 100001
graph = [-1] * (limit)

print(bfs(graph, n,k, limit))
