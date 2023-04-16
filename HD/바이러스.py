import sys

k,p,n = map(int,sys.stdin.readline().rstrip().split())
mod = 1000000007

value = k
for _ in range(n):
    value *= p
    value = value % mod
print(value)

"""
5으로 나눔

k = 2 p = 3 n = 4

1초
2 3 / 6 / 1

2초
6 3 / 18 / 3
1 3 / 3 / 3


3초
18 3 / 54 / 4
3 3 / 9 / 4

4초
54 3 / 162 / 2

162 3 / 486 / 1
486 3 / 1458 / 3

"""