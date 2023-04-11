import copy
import sys
from collections import deque

def spring():
    for i in range(n):
        for j in range(n):
            q_len = len(tree[i][j])
            for d in range(q_len):
                if graph[i][j] < tree[i][j][d]:
                    for _ in range(d, q_len):
                        dead[i][j].append(tree[i][j].pop())
                    break
                else:
                    graph[i][j] -= tree[i][j][d]
                    tree[i][j][d] += 1

def summer():
    for i in range(n):
        for j in range(n):
            while dead[i][j]:
                graph[i][j] += dead[i][j].pop() // 2

def fall_winter():
    dx = [-1,-1,-1,0,1,1,1,0]
    dy = [-1,0,1,1,1,0,-1,-1]
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for direct in range(8):
                        nx = i + dx[direct]
                        ny = j + dy[direct]
                        if not(0<=nx<n and 0<=ny<n):
                            continue
                        tree[nx][ny].appendleft(1)

            graph[i][j] += health_plus[i][j]

def cal_tree():
    count = 0
    for i in range(n):
        for j in range(n):
            count += len(tree[i][j])
    return count

n,m,k = map(int,sys.stdin.readline().rstrip().split())
health_plus = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

tree = [[deque() for _ in range(n)] for _ in range(n)]
dead = [[deque() for _ in range(n)] for _ in range(n)]


for _ in range(m):
    x,y,z = map(int,sys.stdin.readline().rstrip().split())
    tree[x-1][y-1].append(z)

graph =  [[5 for _ in range(n)] for _ in range(n)]


for _ in range(k):
    spring()
    summer()
    fall_winter()

result = cal_tree()
print(result)
