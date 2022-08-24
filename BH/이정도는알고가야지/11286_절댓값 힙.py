import heapq
import sys

n = int(sys.stdin.readline().rstrip())
hq = []

for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if len(hq) == 0:
            print(0)
        else:
            b = heapq.heappop(hq)[1]
            print(b)
    else:
        heapq.heappush(hq, (abs(a), a))

