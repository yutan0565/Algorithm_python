import sys

a,b = map(str, sys.stdin.readline().rstrip().split())

a = list(a)
b = list(b)

result = float('inf')

gap = len(b) - len(a)

for i in range(gap + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    result = min(result, count)

print(result)