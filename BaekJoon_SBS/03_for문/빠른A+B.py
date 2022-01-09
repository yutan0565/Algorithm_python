import sys

T = int(input())

def add(a,b):
    return a+b

for _ in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(add(a,b))


# sys.stdin.readline() -- 저수준 입력 방식 - input()보다 더 빠름