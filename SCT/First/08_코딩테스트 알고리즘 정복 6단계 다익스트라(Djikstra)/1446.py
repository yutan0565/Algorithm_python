import sys
import heapq

def daik(start):
    q = []
    heapq.heappush(q, [0, start])
    visited[start] = 0

    while q:
        now_dis, a = heapq.heappop(q)
        if visited[a] > now_dis:
            continue
        for dis, nx in graph[a]:
            new_dis  = now_dis + dis
            if visited[nx] > new_dis:
                visited[nx] = new_dis
                heapq.heappush(q, [new_dis, nx])
    return visited[d]


n,d = map(int,sys.stdin.readline().rstrip().split())
graph = [[[1,i+1]] for i in range(d)] + [[]]
visited = [float('inf') for _ in range(d+1)]

for _ in range(n):
    a,b,distance = map(int,sys.stdin.readline().rstrip().split())
    if b > d:
        continue
    graph[a].append([distance,b])

start= 0
result = daik(start)
print(result)
