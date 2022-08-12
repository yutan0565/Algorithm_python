import sys

n = int(sys.stdin.readline().rstrip())

a = 1000 - n
mon = [500, 100, 50, 10, 5, 1]
result = 0

for i in mon:
    result += a // i
    a %= i
print(result)