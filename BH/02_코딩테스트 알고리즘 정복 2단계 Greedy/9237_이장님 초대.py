import sys

n = int(sys.stdin.readline().rstrip())
t_list = list(map(int, sys.stdin.readline().rstrip().split()))
t_list.sort(reverse=True)

result = -1

for i in range(n):
    day = i + t_list[i]
    result = max(result, day)
print(result + 2)
