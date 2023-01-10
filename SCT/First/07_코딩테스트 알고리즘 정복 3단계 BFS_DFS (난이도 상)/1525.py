import sys
from collections import deque

"""
1. 내가 목표로 하는것(위치나 정보) 가 q에 들어가야함
"""

def bfs():
    q = deque()
    q.append(start)
    dict = {}
    dict[start] = 0
    # dx = [3, -3, 1, -1]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        string= q.popleft()
        if string == "123456780":
            return dict[string]
        x = string.find("0")
        a = x // 3
        b = x % 3
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]

            if 0 <= na < 3 and 0 <= nb < 3:
                nx = na * 3 + nb
        # for i in range(4):  ... 이건 왜 안될까...
        #     nx = x + dx[i]
        #     if 0 <= nx <9:
                string_list = list(string)
                string_list[nx], string_list[x] = string_list[x], string_list[nx]
                new_string = "".join(string_list)
                if not(dict.get(new_string)):
                    q.append(new_string)
                    dict[new_string] = dict[string] + 1
    return -1

start = ""
for _ in range(3):
    temp = sys.stdin.readline().strip().split()
    for i in range(3):
        start += temp[i]

result = bfs()
print(result)
