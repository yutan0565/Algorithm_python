import copy
import sys
import heapq

def daik():
    q = []
    heapq.heappush(q, [0, start])
    while q:
        cost, a  = heapq.heappop(q)
        if cost > visited[a]:
            continue
        for c, nx in graph[a]:
            nc = cost + c
            if visited[nx] >  nc:
                visited[nx] = nc
                before_node[nx] = a
                heapq.heappush(q, [nc, nx])

def find_result():
    result = []
    check_node = end
    while 1:
        if check_node == start:
            break
        result.append(check_node)
        check_node = before_node[check_node]
    result.append(start)
    result.reverse()
    return result

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append([c,b])

start,end = map(int,sys.stdin.readline().rstrip().split())

visited = [float("inf") for _ in range(n + 1)]
visited[start] = 0
before_node = [-1 for _ in range(n + 1)]
before_node[start] = start

daik()
min_cost = visited[end]
result = find_result()

print(min_cost)
print(len(result))
for r in result:
    print(r, end = " ")



