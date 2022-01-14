import sys

a,b  = map(str, sys.stdin.readline().strip().split())

new_a = a[-1]+a[-2]+a[-3]
new_b = b[-1]+b[-2]+b[-3]

if new_a > new_b:
    print(new_a)
else:
    print(new_b)