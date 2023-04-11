from collections import deque
import sys
# 부모, 자식, 가중치

"""
bfs를 두번 써서 !!!!

번주 중심으로 부터 가장 먼곳 찾고, 거기서 먼곳 또 찾기 !!

"""

def bfs(x):
    q = deque()
    q.append(x)
    visited = [-1 for _ in range(n + 1)]
    visited[x] = 0
    point = -1
    time = 0
    while q:
        a = q.popleft()
        for n_g in graph[a]:
            nx = n_g[0]
            w = n_g[1]
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[a] + w
                if time < visited[nx]:
                    point = nx
                    time =visited[nx]
    return point, time

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
start_list = [i for i in range(1,n+1)]


for _ in range(n-1):
    p,c,w = map(int, sys.stdin.readline().rstrip().split())
    graph[p].append([c,w])
    graph[c].append([p,w])

start_point, _= bfs(1)
_, result = bfs(start_point)

print(result)