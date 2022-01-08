import sys

N, X = map(int, sys.stdin.readline().split())

A = sys.stdin.readline().split()

for i in A:
    if int(i) < X:
        print(i, end = " ")