import copy
import sys
import heapq

def daik():

    reset_visited = [float("inf") for _ in range(n+1)]
    reset_visited[start] = 0

    q = []
    heapq.heappush(q, [0, start, reset_visited])

    while q:
        cost, a, visited = heapq.heappop(q)
        if a == end:
            return visited
        for c, nx in graph[a]:
            nc = cost + c
            if visited[nx] > nc:
                new_visited = copy.deepcopy(visited)
                new_visited[nx] = nc
                heapq.heappush(q, [nc, nx, new_visited ])



n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append([c,b])

start,end = map(int,sys.stdin.readline().rstrip().split())


result_visit = daik()


visit_city = [i for i in range(len(result_visit)) if result_visit[i] != float("inf")]

min_cost = result_visit[end]
city_count = len(visit_city)

print(min_cost)
print(city_count)
for c in visit_city:
    print(c, end=" ")



