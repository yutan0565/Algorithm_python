# DFS 방식,    최대한 방문한 것을 1개의 트리로 계산
def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                dfs(n, computers, connect, visited)


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            dfs(n, computers, com, visited)
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


# BFS 방식
from collections import deque


def bfs(n, com, computers, visited):
    visited[com] = True
    q = deque()
    q.append(com)

    while (q):
        current = q.popleft()
        visited[current] = True
        for connect in range(n):
            if connect != current and computers[current][connect] == 1:
                if visited[connect] != True:
                    q.append(connect)


def solution(n, computers):
    visited = [False] * n
    count = 0
    for i in range(n):
        if visited[i] != True:
            bfs(n, i, computers, visited)
            count += 1
    return count

