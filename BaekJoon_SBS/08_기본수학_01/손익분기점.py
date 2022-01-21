import sys

a,b,c = map(int, sys.stdin.readline().split())

if c == b:
    n = -1
else:
    n = a//(c-b) + 1

if n <= 0:
    print(-1)
else:
    print(n)

