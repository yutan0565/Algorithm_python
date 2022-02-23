import sys


def fac(result, n):
    result *= n
    if n ==0:
        return 1

    if n >= 2:
        return fac(result, n-1)
    return result

n = int(sys.stdin.readline())
result = 1
print(fac(result, n))