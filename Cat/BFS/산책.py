import sys
import heapq

def daik(load_set, start):
    visited = [2e10 for _ in range(n+1)]
    visited[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        now_dis, a = heapq.heappop(q)
        if visited[a] < now_dis:
            continue
        for nx, dis in graph[a]:
            if nx in load_set:
                continue
            new_dis = now_dis + dis
            if visited[nx] >new_dis:
                visited[nx] = new_dis
                heapq.heappush(q, [new_dis, nx])
    return visited

def find_load():
    f_dis = 0
    now_node = start
    load_set = set()
    while 1:
        if now_node == end:
            break
        for nx, dis in graph[now_node]:
            if f_dis + dis + visited_go[nx] == visited_go[start]:
                f_dis += dis
                load_set.add(nx)
                now_node = nx
                break
    load_set.remove(end)
    return load_set, f_dis

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

for i in range(n+1):
    graph[i].sort()

start, end = map(int, sys.stdin.readline().rstrip().split())

visited_go = daik(set(), end)
load_set, f_dis = find_load()

visited_back = daik(load_set, start)
result = f_dis + visited_back[end]
print(result)