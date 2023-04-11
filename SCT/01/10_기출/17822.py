import copy
from collections import deque
import sys

def rotation_circle(number, direct, move):
    if direct == 0:
        graph[number].rotate(move)
    elif direct == 1:
        graph[number].rotate(-move)

def tune_graph(graph, avg):
    for i in range(1, n + 1):
        for j in range(m):
            if graph[i][j] != -1:
                if graph[i][j] > avg:
                    graph[i][j] -= 1
                elif graph[i][j] < avg:
                    graph[i][j] += 1
    return graph
def check_circle():
    flag = 0
    temp_graph = copy.deepcopy(graph)
    sum = 0
    count = 0
    for i in range(1, n+1):
        for j in range(m):
            if graph[i][j] != -1:
                near_list = fine_near_number(i,j)
                sum += graph[i][j]
                count += 1
                for c_number, idx in near_list:
                    if graph[i][j] == graph[c_number][idx]:
                        temp_graph[i][j] = -1
                        temp_graph[c_number][idx] = -1
                        flag = 1

    if flag == 1:
        return temp_graph
    elif flag == 0: # 변화 없으면 조정
        if count != 0:
            avg = sum/count
            temp_graph = tune_graph(temp_graph, avg)
        return temp_graph

def fine_near_number(number,index):
    near_number_index = []

    # 숫자 그대로 양옆
    left_index = (index - 1)%m
    right_index = (index + 1)%m
    near_number_index.append([number,left_index])
    near_number_index.append([number,right_index])

    #위 아래 원판
    if number == 1:
        near_number_index.append([2, index])
    elif number == n:
        near_number_index.append([n-1, index])
    else: # 중간에 있는 애들
        near_number_index.append([number-1, index])
        near_number_index.append([number+1, index])
    return near_number_index

def cal_sum():
    sum = 0
    for circle in graph:
        for i in circle:
            if i != -1:
                sum += i
    return sum

n,m,t = map(int,sys.stdin.readline().rstrip().split())
graph = [deque([-1 for _ in range(m)])]

for _ in range(n):
    temp_q = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    graph.append(temp_q)

for _ in range(t):
    x,d,k = map(int, sys.stdin.readline().rstrip().split())
    # 원판 모두 돌리기
    for circle_number in range(0,n+1,x):
        if circle_number == 0:
            continue
        rotation_circle(circle_number, d, k)

    # 인접 한거 지우기 // 조정 해주기
    graph = check_circle()


result = cal_sum()
print(result)