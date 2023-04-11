import sys
import heapq

def bfs(x):
    q = []
    heapq.heappush(q,[0, x])
    cost_list = [float("inf") for _ in range(n+1)]
    cost_list[x] = 0
    
    while q:
        now_cost, a = heapq.heappop(q)
        if visited[a] == -1:
            visited[a] = 1
            for new_cost, nx in graph[a]:
                if visited[nx] == -1:
                    if cost_list[nx] > new_cost:
                        heapq.heappush(q, [new_cost, nx])
                        cost_list[nx] = new_cost
    return sum(cost_list[1:])

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]


for _ in range(m):
    a,b,cost = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append([cost,b])
    graph[b].append([cost,a])


result = bfs(1)
print(result)
