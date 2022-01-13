import sys

s = list(map(int,sys.stdin.readline().strip().split()))

result = s[0]

for i in s:
    if i <=1 or result <=1:
        result += i
    else:
        result *= i
print(result)