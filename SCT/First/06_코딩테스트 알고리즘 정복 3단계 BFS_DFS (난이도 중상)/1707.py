from collections import deque
import sys

"""
문제 그대로만 따라가려고 하지말고 !!
이분그래프면은 ->  내가 이동하는 곳은 지금하고 다른 그룹이어야함 !!!
근데 내가 더이상 갈곳이 없다면 ?? -> 이분 그래프가 아닌거임 !
"""

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == 0:
                q.append(nx)
                visited[nx] = -visited[a]
            elif visited[nx] == visited[a]:
                return -1
    return 1

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    n,e = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for _ in range(e):
        u,v =  map(int, sys.stdin.readline().rstrip().split())
        graph[u].append(v)
        graph[v].append(u)

    result = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            result = bfs(i)
            if result == -1:
                break

    if result == 1:
        print("YES")
    else:
        print("NO")