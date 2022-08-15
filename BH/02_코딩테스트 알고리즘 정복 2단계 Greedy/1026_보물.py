import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()
b.sort(reverse=True)

sum = 0
for i in range(len(a)):
    sum += a[i]*b[i]
print(sum)