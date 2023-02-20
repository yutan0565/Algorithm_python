import sys
import heapq

def daik(start):
    q = []
    heapq.heappush(q, [0, start])
    visited = [float("inf") for _ in range(n+1)]
    visited[start] = 0

    while q:
        now_dis, a = heapq.heappop(q)
        if visited[a] > now_dis:
            continue
        for dis, nx in graph[a]:
            new_dis = now_dis + dis
            if new_dis <= m:
                if visited[nx] > new_dis:
                    heapq.heappush(q, [new_dis, nx])
                    visited[nx] = new_dis

    temp_result = 0
    for i in range(len(visited)):
        if visited[i] != float("inf"):
            temp_result += item_list[i]
    return temp_result

n,m,r = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
item_list = [0] + list(map(int,sys.stdin.readline().rstrip().split()))
for _ in range(r):
    a,b,l = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append([l,b])
    graph[b].append([l,a])

result = -1
for start in range(1, n+1):
    temp = daik(start)
    result = max(result, temp)
print(result)