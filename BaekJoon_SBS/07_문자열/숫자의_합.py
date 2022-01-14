import sys

N = int(sys.stdin.readline())
number_list = list(map(int,sys.stdin.readline().strip()))

sum = 0

for i in number_list:
    sum += i
print(sum)
