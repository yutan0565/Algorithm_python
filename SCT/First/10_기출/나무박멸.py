import copy
from collections import deque
import sys

def grow_tree():
    global graph
    temp_graph = copy.deepcopy(graph)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] > 0:
                            temp_graph[i][j] += 1
    graph = temp_graph

def spread_tree():
    global graph
    temp_graph = copy.deepcopy(graph)
    empty_count = [[0 for _ in range(n)] for _ in range(n)  ]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] == 0:
                            if gas_graph[nx][ny] == -1:
                                empty_count[i][j] += 1
                if empty_count[i][j] != 0:
                    new_tree = graph[i][j] // empty_count[i][j]
                    for d in range(4):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[nx][ny] == 0:
                                if gas_graph[nx][ny] == -1:
                                    temp_graph[nx][ny] += new_tree

    graph = temp_graph

def spread_gas(x,y):
    kill_count = 0

    kill_count += graph[x][y]
    if graph[x][y] == 0:
        return kill_count

    dx_kill = [1,1,-1,-1]
    dy_kill = [1,-1,1,-1]

    for i in range(4):
        for k_add in range(1, k + 1):
            nx = x + dx_kill[i] * k_add
            ny = y + dy_kill[i] * k_add
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > 0:
                    kill_count += graph[nx][ny]
                elif graph[nx][ny] == 0:
                    break
                elif graph[nx][ny] == -1:
                    break
    return kill_count

def find_best_spot():
    global graph, gas_graph, result
    max_kill = -1
    x_max = -1
    y_max = -1
    for i in range(n):
        for j in range(n):
            if graph[i][j]  > -1:
                count = spread_gas(i,j)
                if count > max_kill:
                    max_kill = count
                    x_max = i
                    y_max = j
    result += max_kill

    gas_graph[x_max][y_max] = c
    if graph[x_max][y_max] != 0:
        graph[x_max][y_max] = 0
        dx_kill = [1,1,-1,-1]
        dy_kill = [1,-1,1,-1]
        for i in range(4):
            for k_add in range(1, k + 1):
                nx = x_max + dx_kill[i] * k_add
                ny = y_max + dy_kill[i] * k_add
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > 0:
                        gas_graph[nx][ny] = c
                        graph[nx][ny] = 0
                    elif graph[nx][ny] == 0:
                        gas_graph[nx][ny] = c
                        break
                    elif graph[nx][ny] == -1:
                        break


def down_gas():
    for i in range(n):
        for j in range(n):
            if gas_graph[i][j] > -1:
                gas_graph[i][j] -= 1


n,m,k,c = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
gas_graph = [[-1 for _ in range(n)] for _ in range(n)]
result = 0

for year in range(1, m+1):
    grow_tree()
    spread_tree()
    find_best_spot()
    down_gas()

print(result)
"""
1. 나무 성장 ( 인접한거에 나무 있으면 ) - 동시 발생
2. 나무 번식 - 인접 빈공간 만큼 //빈칸  만큼  -> 중복 가능 (새로운 그래프 형성 ) -- 동시 발생

3. 대각선으로 퍼지는 제초제중,  가장 많이 퍼지는 곳에 뿌리기  --> 

4. 제초재 뿌린곳은 전팟 및 성장x  ->  c +1 번째 해가 되면, 없어짐

5. 제초재가 다시 부려지면, 그로부터 다시 c년 만큼 유지

"""