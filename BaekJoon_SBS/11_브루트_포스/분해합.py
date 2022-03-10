import sys

n = int(sys.stdin.readline())

for m in range(1,n+1):
    num_list = list(map(int, str(m)))
    result = sum(num_list) + m
    if result == n:
        print(m)
        break
    if m == n:
        print(0)