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


# BFS 방식

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            # bfs로 보내서 인접한거 무두 채우도록 하기
            bfs(n, computers, com, visited)
            answer += 1
    return answer


def bfs(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)  # 맨처음꺼 꺼내기
        visited[com] = True  # 꺼낸거 방문 표기
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:  # 연결된 곳의 연결된 곳 중에 방분x 이쓰면
                    queue.append(connect)  # queue에 넣어주기