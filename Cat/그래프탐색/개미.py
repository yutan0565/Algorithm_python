import sys, heapq

def daik(x):
    q = []
    visited = [2e10 for _ in range(n)]
    visited[x] = 0
    q.append([visited[x], x])
    while q:
        now_distance, a = heapq.heappop(q)
        if visited[a] < now_distance:
            continue
        for nx,dis in graph[a]:
            new_distance = now_distance + dis
            if new_distance < visited[nx]:
                visited[nx] = new_distance
                next_visited[nx][0] = a
                heapq.heappush(q, [new_distance, nx])

def check_node():
    for i in range(1, n):
        if i == 0:
            next_visited[i] = [0,0]
            continue
        for j in range(len(graph[i])):
            nx_node = graph[i][j][0]
            dis = graph[i][j][1]
            if nx_node == next_visited[i][0]:
                next_visited[i][1] = dis

def get_result():
    result = []
    for now_node in range(n):
        if now_node == 0:
            result.append(0)
            continue
        ant_stat = ant_stat_list[now_node]
        while 1:
            ant_stat -= next_visited[now_node][1]
            if ant_stat < 0:
                result.append(now_node)
                break
            elif now_node == 0:
                result.append(now_node)
                break
            now_node = next_visited[now_node][0]

    return result

print(1569/1600)

n = int(sys.stdin.readline())
ant_stat_list = []
for i in range(n):
    ant_stat_list.append(int(sys.stdin.readline()))

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    a,b = a-1, b-1
    graph[a].append([b, c])
    graph[b].append([a, c])

next_visited= [[-1,-1] for _ in range(n)]
daik(0)
check_node()
result = get_result()
for r in result:
    print(r+1)

