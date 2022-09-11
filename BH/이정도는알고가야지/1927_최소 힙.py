import sys
import heapq

n = int(sys.stdin.readline().rstrip())
info_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

heap = []

for number in info_list:
    if number > 0:
        heapq.heappush(heap, number)
    else:
        if len(heap) == 0:
            print(0)
        else:
            a = heapq.heappop(heap)
            print(a)


