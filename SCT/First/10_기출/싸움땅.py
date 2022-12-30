from collections import deque
import sys

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    q = deque()
    for i in range(1, m+1):
        q.append([dict_pos[i][0], dict_pos[i][1], dict_direct[i], dict_first_stat[i], 0  ,1])

    while q:
        for _ in range(len(q)):
            a,b,direct, gun , stat, turn  = q.popleft()
            nx = a + dx[direct] * turn
            ny = b + dy[direct] * turn
            if 0<=nx<n and 0<=ny<n:
                gun_list = graph[nx][ny]
                if len(gun_list) != 0:
                    gun_list.sort()
                    if gun < gun_list[-1]:
                        g

            else:
                turn = -1
                nx = a + dx[direct] * turn
                ny = b + dy[direct] * turn


n,m,k = map(int, sys.stdin.readline().rstrip().split())

graph = [[[] for _ in range(n)] for _ in range(n) ]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        graph[i][j].append(temp[j])

print(graph)

reset_visited = [[-1 for _ in range(n)] for _ in range(n)]

dict_pos = {}
dict_direct = {}
dict_first_stat = {}


score_list = [0 for _ in range(m)]
for i in range(1,m+1):
    a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
    dict_pos[i] = [a,b]
    dict_direct[i] = c
    dict_first_stat = d


