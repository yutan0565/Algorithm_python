import sys

n = int(sys.stdin.readline().rstrip())
t_list = list(map(int, sys.stdin.readline().rstrip().split()))
t_list.sort()

sum_list = []
for i in range(n):
    temp = 0
    for j in range(i+1):
        temp += t_list[j]
    sum_list.append(temp)
print(sum(sum_list))