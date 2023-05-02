import sys
from collections import deque

def check(x):
    stack =  deque()
    stack.append(x)
    temp_visited = [0] * n
    while stack:
        a = stack.pop()
        if a == end:
            return 1
        temp_visited[a] = 1
        for nx, cost in graph[a]:
            if temp_visited[nx] == 0:
                stack.append(nx)
    return 0


def bellman_ford():
    for i in range(n+1):
        if visited[end] == -max_value and i == n:
            print("gg")
            return
        for j in range(n):
            if visited[j] == -max_value:
                continue
            for nx, cost in graph[j]:
                new_cost = visited[j] + cost
                if new_cost > visited[nx]:
                    visited[nx] = new_cost
                    if i == n :
                        if check(nx):
                            print("Gee")
                            return
    print(visited[end])
    return

n,start,end,m = map(int,sys.stdin.readline().rstrip().split())
max_value = 2e10
graph = [[] for _ in range(n)]
visited = [-max_value for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append([b,c])
max_money = list(map(int,sys.stdin.readline().rstrip().split()))

visited[start] = max_money[start]
for i in range(len(max_money)):
    for j in range(len(graph[i])):
        for k in range(len(max_money)):
            if graph[i][j][0] == k:
                graph[i][j][1] = max_money[k] - graph[i][j][1]

bellman_ford()