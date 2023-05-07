import sys
import heapq
from collections import deque

def daik(graph):
    q = []
    heapq.heappush(q, [0,start])
    visited = [2e10 for _ in range(n)]
    visited[start] = 0

    while q:
        now_dis, a = heapq.heappop(q)
        if a == end:
            return now_dis, visited
        for nx, dis in graph[a]:
            new_dis = now_dis + dis
            if visited[nx] > new_dis:
                if load_graph[a][nx] == 1:
                    heapq.heappush(q, [new_dis,nx])
                    visited[nx] = new_dis
    return -1,[]

def del_short_len(visited_go):
    global load_graph
    q = deque()
    q.append([0,end])
    while q:
        now_dist, a = q.popleft()
        for nx, dis in graph_back[a]:
            new_dis = now_dist + dis
            if new_dis + visited_go[nx] == short_len:
                if load_graph[nx][a] == 1:
                    load_graph[nx][a] = -1
                    q.append([new_dis,nx])

while 1:
    n,m = map(int,sys.stdin.readline().rstrip().split())
    if [n,m] == [0,0]:
        break
    start,end = map(int,sys.stdin.readline().rstrip().split())
    graph_go = [[] for _ in range(n)]
    graph_back = [[] for _ in range(n)]
    load_graph = [[-1 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        u,v,p = map(int,sys.stdin.readline().rstrip().split())
        graph_go[u].append([v,p])
        graph_back[v].append([u,p])
        load_graph[u][v] = 1

    short_len,visited_go = daik(graph_go)
    if short_len == -1:
        print(-1)
        continue
    del_short_len(visited_go)

    short_len,visited = daik(graph_go)
    print(short_len)