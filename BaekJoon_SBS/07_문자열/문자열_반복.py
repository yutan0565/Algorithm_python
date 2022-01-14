import sys
T = int(sys.stdin.readline())

for i in range(T):
    R, s = map(str, sys.stdin.readline().strip().split())
    r = ""
    for i in s:
        r += i*int(R)
    print(r)

