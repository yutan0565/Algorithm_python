import sys
import heapq

def daik(v,e,start,graph,visited):
    heap = []
    heapq.heappush(heap, [0, start ]  )
    visited[start] = 0
    while heap:
        dis, now = heapq.heappop(heap)
        for go, w in graph[now]:
            new_dis = dis + w
            if new_dis < visited[go]:
                visited[go] = new_dis
                heapq.heappush(heap, [new_dis, go])
                
    for i in range(1, len(visited)):
        if i == start -1 :
            pass
        if visited[i] == 2e10:
            print("INF")
        else:
            print(visited[i])



V, E = map(int, sys.stdin.readline().rstrip().split())
k = int(sys.stdin.readline().rstrip())
graph = [ [] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append([v,w])
visited = [2e10] * (V+1)

daik(V,E,k,graph,visited)
