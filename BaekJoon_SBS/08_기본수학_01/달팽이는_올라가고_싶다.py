import sys

A, B, V = map(int, sys.stdin.readline().split())

temp = V - A

if temp == 0:
    day = 1

elif temp % (A-B) == 0:
    day = temp // (A-B)  + 1
else:
    day = temp // (A-B) + 2

print(day)



