import sys


N = int(sys.stdin.readline())

def insu(n):
    if n == 1:
        return -1
    temp = []

    for i in range(2, n+1):
        while True:
            if n%i == 0:
                temp.append(i)
                n = int(n/i)
            else:
                break

    return temp

result = insu(N)
if result == -1:
    pass
else:
    for i in result:
        print(i)