import sys
sys.setrecursionlimit(10**6)

def dfs(x,parent):
    global node_count,result_list, visited, graph
    node_count += 1
    visited[x] = node_count
    now_value = visited[x]
    for nx in graph[x]:
        if nx == parent:
            continue
        if visited[nx] == -1:
            check_node = dfs(nx, x)
            now_value = min(now_value, check_node)
            if check_node > visited[x]:
                now_edge = [x,nx]
                now_edge.sort()
                result_list.append(now_edge)
        elif visited[nx] != -1:
            now_value = min(now_value, visited[nx])

    return now_value

v,e = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(v+1)]
visited = [-1 for _ in range(v+1)]
result_list = []
node_count = 0

for _ in range(e):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, v+1):
    if visited[i] == -1:
        dfs(i,1)

result_list.sort(key = lambda x : (x[0],x[1]))
print(len(result_list))
for a,b in result_list:
    print(a,b)