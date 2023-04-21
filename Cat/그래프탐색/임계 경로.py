import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for dis, nx in graph[a]:
            visited[nx] -= 1
            if visited_time[nx] < visited_time[a] + dis:
                visited_time[nx] = visited_time[a] + dis
                load_list[nx] = [a]
            elif visited_time[nx] == visited_time[a] + dis:
                load_list[nx].append(a)
            if visited[nx] == 0:
                q.append(nx)

def bfs_from_end(end):
    q = deque()
    q.append(end)
    load = []
    while q:
        a = q.popleft()
        for x in load_list[a]:
            if [a, x] not in load:
                load.append([a, x])
                q.append(x)
    return load

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
graph_back = [[] for _ in range(n+1)]

visited = [0 for _ in range(n+1)]
visited_time = [0 for _ in range(n+1)]
load_list = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append([c, b])
    graph_back[b].append(a)
    visited[b] += 1

start, end = map(int, sys.stdin.readline().rstrip().split())

bfs(start)
load = bfs_from_end(end)

print(visited_time[end])
print(len(load))