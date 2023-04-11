import sys
import heapq

def bfs(start, end):
    q = []
    heapq.heappush(q, [0,start])
    visited[start] = 0

    while q:
        cost, a = heapq.heappop(q)
        print(visited)
        if visited[a] < cost:
            continue
        for c, nx in graph[a]:
            new_cost = cost + c
            if visited[nx] > new_cost:
                heapq.heappush(q, [new_cost, nx])
                visited[nx] = new_cost
    return visited[end]

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
max_cost = float("inf")
visited = [max_cost for _ in range(n+1)]


m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append([c,b])

start,end = map(int,sys.stdin.readline().rstrip().split())

result = bfs(start, end)
print(result)