import sys
from collections import deque
























def bfs(graph,visited, N, M, V):
    q = deque()
    q.append(V)
    temp = []
    temp.append(V)
    while q:
        a = q.popleft()
        for i in range(M):
            if graph[i][0] == a :
                if visited[i] == False:
                    if graph[i][1] not in temp:
                        q.append(graph[i][1])
                        visited[i] = True
                        temp.append(graph[i][1])
            elif graph[i][1] == a:
                if visited[i] == False:
                    if graph[i][0] not in temp:
                        q.append(graph[i][0])
                        visited[i] = True
                        temp.append(graph[i][0])
    return temp

def dfs(graph,visited, N, M, V, temp_d):
    temp_d.append(V)


    for i in range(M):
        if graph[i][0] == V:
            if visited[i] == False:
                if graph[i][1] not in temp_d:
                    visited[i] = True
                    dfs(graph, visited, N, M, graph[i][1],temp_Pd )

        elif graph[i][1] == V:
            if visited[i] == False:
                if graph[i][0] not in temp_d:
                    visited[i] = True
                    dfs(graph, visited, N, M, graph[i][0],temp_d)
    return temp_d



N, M, V =  map(int, sys.stdin.readline().rstrip().split())
graph = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
graph.sort(key = lambda x : x[1])


visited = [False for i in range(M)]
temp_d = []
for node in dfs(graph,visited, N, M, V, temp_d):
    print(node, end = " ")
print()

visited = [False for i in range(M)]
for node in bfs(graph,visited, N, M, V):
    print(node, end = " ")








