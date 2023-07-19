import sys
from collections import deque
sys.setrecursionlimit(10**8)

def bfs(x,graph,type):
    visted = [-1 for _ in range(n+1)]
    q = deque()
    q.append(x)
    visted[x] = 1
    if type == 1:
        if x == start:
            visted[end] = 1
        elif x == end:
            visted[start] = 1
    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visted[nx] == -1:
                q.append(nx)
                visted[nx] = 1
    return visted


n,m = map(int,sys.stdin.readline().rstrip().split())
graph_go = [[] for _ in range(n+1)]
graph_back = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph_go[a].append(b)
    graph_back[b].append(a)

start,end =map(int,sys.stdin.readline().rstrip().split())

visited_s_go = bfs(start, graph_go,1)
visited_s_back = bfs(start, graph_back,0)

visited_e_go = bfs(end, graph_go,1)
visited_e_back = bfs(end, graph_back,0)

count = 0
for i in range(1, n+1):
    if visited_s_go[i] == 1 and visited_s_back[i] == 1 and visited_e_go[i] == 1 and visited_e_back[i] == 1:
        count += 1
print(count-2)



"""
8 13
1 2
1 5
7 1
2 3
3 1
4 1
4 2
5 4
5 8
6 2
6 3
7 6
8 7
6 5
"""