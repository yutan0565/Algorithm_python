import sys
from collections import deque

def bfs(x, y, end_x, end_y, market):
    q = deque()
    q.append([x,y])

    while q:
        a, b  = q.popleft()

        if abs(end_x - a) + abs(end_y - b) <= 20 * 50:
            return 1
        for i in range(len(market)):
            if abs(market[i][0] - a) + abs(market[i][1] - b) <= 20 * 50:
                if market[i][0] != 40000 and market[i][1] != 40000:
                    q.append([market[i][0], market[i][1]])
                    market[i][0] = 40000
                    market[i][1] = 40000

    return 0




t = int(sys.stdin.readline().rstrip())

for _ in range(t):

    n = int(sys.stdin.readline().rstrip())
    x,y = map(int, sys.stdin.readline().rstrip().split())

    market = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        market.append([a,b])
    end_x, end_y = map(int, sys.stdin.readline().rstrip().split())

    result = bfs(x, y, end_x, end_y, market)
    if result == 1:
        print("happy")
    else:
        print("sad")









