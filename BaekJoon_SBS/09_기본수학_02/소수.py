import math
import sys

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

total = []

for i in range(m, n+1):
    if i == 1:
        continue
    elif i == 2:
        total.append(i)
    else:
        for j in range(2, i):
            if i % j ==0:
                break
            elif j == i-1:
                total.append(i)

if len(total) == 0:
    print(-1)
else:
    print(sum(total))
    print(min(total))