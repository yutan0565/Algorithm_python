from collections import deque


# BFS
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(queue)
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])
    while queue:
        temp, idx = quequ.papleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


def solution(numbers, target):
    answer = 0
    list = [0]

    for num in numbers:
        temp = []
        for a in list:
            temp.append(a + num)
            temp.append(a - num)
        list = temp
    for num in list:
        if num == target:
            answer += 1
    return answer


# DFS 풀이

def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(idx, result):
        if idx == 0:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)
    return answer


def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer


def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += DFS(numbers, target, depth + 1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth + 1)
        return answer