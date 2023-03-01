import sys
import heapq

def daik(start):
    visited = [float('inf') for _ in range(n+1)]
    before_list = [-1 for _ in range(n+1)]

    visited[start] = 0
    q = []
    heapq.heappush(q, [0,start])

    while q:
        now_time, a = heapq.heappop(q)
        # if a == end:
        #     print(before_list)
        #     for check_node in range(len(before_list)):
        #         b_node = before_list[check_node]
        #         if b_node == start:
        #             return check_node
        if visited[a] > now_time:
            continue
        for t, nx in graph[a]:
            new_time = now_time + t
            if visited[nx] > new_time:
                visited[nx] = new_time
                before_list[nx] = a
                heapq.heappush(q, [new_time, nx])
    return before_list
n,m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,t = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append([t,b])
    graph[b].append([t,a])

result_graph = [['-' for _ in range(n)] for _ in range(n)]
for i in range(n):
    start = i + 1
    temp_list = daik(start)
    for j in range(n):
        if i == j:
            continue
        end = j+1
        now_node = end
        move_noede_list = []
        while 1:
            if now_node == start:
                move_noede_list.append(start)
                break
            move_noede_list.append(now_node)
            now_node = temp_list[now_node]
        move_noede_list.reverse()
        result_graph[i][j] = str(move_noede_list[1])

for i in range(n):
    for j in range(n):
        print(result_graph[i][j], end=' ')
    print()