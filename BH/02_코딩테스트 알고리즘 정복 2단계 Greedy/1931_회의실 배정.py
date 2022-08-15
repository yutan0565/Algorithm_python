import sys

n = int(sys.stdin.readline().rstrip())

s_list = []
for _ in range(n):
    s_list.append(list(map(int, sys.stdin.readline().rstrip().split())))
s_list.sort(key = lambda x: x[0])
s_list.sort(key = lambda x: x[1])

cut = 0
count = 0
for a,b in s_list:
    if a >= cut:
        count += 1
        cut = b
print(count)