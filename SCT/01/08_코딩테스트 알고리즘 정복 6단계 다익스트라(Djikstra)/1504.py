import sys
import heapq

def daik(start, end):
    q = []
    heapq.heappush(q, [0, start])
    visited = [float("inf") for _ in range(n+1)]
    visited[start] = 0

    while q:
        c, a= heapq.heappop(q)
        if a == end :
            return visited[a]
        for c_now, nx in graph[a]:
            nc = c_now + c
            if visited[nx] > nc:
                heapq.heappush(q, [nc, nx])
                visited[nx] = nc

    return -float("inf")


n,e = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c, = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

v1, v2 = map(int,sys.stdin.readline().rstrip().split())

result_1 = daik(1,v1) + daik(v1,v2) + daik(v2,n)
result_2 = daik(1,v2) + daik(v2,v1) + daik(v1,n)

result = min(result_1, result_2)
if result == -float("inf"):
    print(-1)
else:
    print(result)
