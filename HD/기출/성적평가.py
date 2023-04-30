import sys
import heapq

# 값 / index 형태

n = int(sys.stdin.readline().rstrip())

score_q = [[] for _ in range(4)]
score_1 = list(map(int, sys.stdin.readline().rstrip().split()))
score_2 = list(map(int, sys.stdin.readline().rstrip().split()))
score_3 = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(n):
    heapq.heappush(score_q[0], [-score_1[i], i])
    heapq.heappush(score_q[1], [-score_2[i], i])
    heapq.heappush(score_q[2], [-score_3[i], i])
    heapq.heappush(score_q[3], [-score_1[i] - score_2[i] - score_3[i], i])

graph_result = [[-1 for _ in range(n)] for _ in range(4)]

prev_value_list = [score_q[0][0][0], score_q[1][0][0], score_q[2][0][0], score_q[3][0][0]]
count_list = [1, 1, 1, 1]
last_pri_list = [1, 1, 1, 1]

for type in range(4):
    now_score_q = score_q[type]
    count = 1
    last_pri = 1
    prev_value = now_score_q[0]
    while now_score_q:
        now_value, now_index = heapq.heappop(score_q[type])
        if now_value == prev_value:
            graph_result[type][now_index] = last_pri
            count += 1
        else:
            graph_result[type][now_index] = count
            last_pri = count
            count += 1
            prev_value = now_value

for i in range(4):
    for j in range(n):
        print(graph_result[i][j], end=" ")
    print()

"""
4
80 80 80 40
30 30 50 20
100 70 30 40

3 1 2
1 3 2
1 2 3
1 2 3
"""