import sys
import heapq


def go_x(person):
    q = []
    heapq.heappush(q, [0, person])
    visited = [float("inf") for _ in range(n+1)]
    visited[person] = 0
    while q:
        t, a = heapq.heappop(q)
        if a == x:
            return visited[a]
        for move_time, nx in graph[a]:
            nt = t + move_time
            if visited[nx] > nt:
                heapq.heappush(q, [nt, nx])
                visited[nx] = nt

def back_home(person):
    q = []
    heapq.heappush(q, [0, x])
    visited = [float("inf") for _ in range(n + 1)]
    visited[x] = 0

    while q:
        t, a = heapq.heappop(q)
        if a == person:
            return visited[a]
        for move_time, nx in graph[a]:
            nt = t + move_time
            if visited[nx] > nt:
                heapq.heappush(q, [nt, nx])
                visited[nx] = nt


n,m,x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, time = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append([time,end])


max_time = -1
for person in range(1, n+1):
    time_1 = go_x(person)
    time_2 = back_home(person)
    time = time_1 + time_2
    if time > max_time:
        max_time = time
print(max_time)