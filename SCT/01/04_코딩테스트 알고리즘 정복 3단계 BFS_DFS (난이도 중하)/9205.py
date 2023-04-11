from collections import deque
import sys

def bfs(x, y):
    q = deque()
    q.append([x,y])

    while q:
        a,b = q.popleft()
        if abs(a-e_x) + abs(b-e_y) <= 20 * 50:
            return 1
        for i in range(len(mart_list)):
            if abs(mart_list[i][0] - a) + abs(mart_list[i][1] - b) <= 20 * 50:
                if mart_list[i][0] != 40000 and mart_list[i][1] != 40000:
                    q.append([mart_list[i][0], mart_list[i][1]])
                    mart_list[i][0] = 40000
                    mart_list[i][1] = 40000
    return 0

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    h_x, h_y = map(int ,sys.stdin.readline().rstrip().split())
    mart_list = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        mart_list.append([a,b])
    e_x, e_y = map(int ,sys.stdin.readline().rstrip().split())

    result = bfs(h_x, h_y)
    if result:
        print("happy")
    else:
        print("sad")