import copy
from collections import deque
import sys

def bfs(x):
    q = deque()
    q.append(x)
    visited = copy.deepcopy(reset_visited)
    visited[x] = 0

    max_point = 1
    max_distance = 0

    while q:
        a = q.popleft()
        for nx, dis in graph[a]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[a] + dis
                if visited[nx] >= max_distance:
                    max_point = nx
                    max_distance = visited[nx]
    return max_point, max_distance


v = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(v+1)]
reset_visited = [-1 for _ in range(v+1)]
for _ in range(v):
    info = list(map(int, sys.stdin.readline().rstrip().split()))
    info_len = len(info)
    node_name = info[0]
    for i in range(1, info_len-2, 2):
        start = info[i]
        distance = info[i+1]
        graph[node_name].append([start, distance])

first_point, _ = bfs(1)
_, result = bfs(first_point)
print(result)