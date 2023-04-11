import sys
import heapq

def daik():
    q = []
    heapq.heappush(q, [0, start])
    visited[start] = 0

    while q:
        now_cost,a = heapq.heappop(q)
        if a == end:
            return visited[a]
        if visited[a] > now_cost:
            continue
        for cost, nx in graph[a]:
            new_cost = now_cost + cost
            if visited[nx]> new_cost:
                visited[nx] = new_cost
                heapq.heappush(q,[new_cost,nx])

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

visited = [float('inf') for _ in range(n+1)]

start,end = 1, n
result = daik()
print(result)
