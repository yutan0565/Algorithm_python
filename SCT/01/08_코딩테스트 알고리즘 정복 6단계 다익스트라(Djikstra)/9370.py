import sys
import heapq


def daik(start):
    q = []
    heapq.heappush(q, [0, start])
    visited = [100000000  for _ in range(n+1)]
    visited[start] = 0

    while q:
        now_cost, a = heapq.heappop(q)
        if now_cost > visited[a]:
            continue
        for cost, nx in graph[a]:
            new_cost = now_cost + cost
            if visited[nx] > new_cost:
                visited[nx] = new_cost
                heapq.heappush(q, [new_cost, nx])
    return visited

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    # 교차로, 도로, 목적지 후부  개수
    n,m,t = map(int, sys.stdin.readline().rstrip().split())
    # 시작점, 지나간 도로 시작 끝
    s,g,h = map(int, sys.stdin.readline().rstrip().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append([d,b])
        graph[b].append([d,a])

    list_end_candi = []
    for _ in range(t):
        x = int(sys.stdin.readline().rstrip())
        list_end_candi.append(x)

    start_visited = daik(s)
    g_visited = daik(g)
    h_visited = daik(h)

    result = []
    for end in list_end_candi:
        type_1 = start_visited[g] + g_visited[h] + h_visited[end]
        type_2 = start_visited[h] + h_visited[g] + g_visited[end]
        if type_1 == start_visited[end] or type_2 == start_visited[end]:
            result.append(end)
    result.sort()
    for r in result:
        print(r, end = ' ')
    print()

