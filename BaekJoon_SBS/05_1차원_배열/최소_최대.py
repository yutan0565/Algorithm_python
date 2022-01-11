import sys

N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
min = int(number[0])
max = int(number[0])

for i in number:
    if i < min:
        min = i
    if i > max:
        max = i

print(min, max)
