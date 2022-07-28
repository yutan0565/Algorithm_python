import sys
import math

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())

result = []

for i in range(a,b+1):
    for j in range(1, int(math.sqrt(i)) + 1):
        if j**2 == i and i not in result:
            result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))