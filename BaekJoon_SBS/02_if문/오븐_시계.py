import sys


a, b = map(int, sys.stdin.readline().rstrip().split())
c = int(sys.stdin.readline())

h = c //60
m = c % 60

a += h
b += m

if b >= 60:
    b -= 60
    a += 1
if a >= 24:
    a -= 24
print(a,b)
