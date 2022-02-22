import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split())
a = w-x
b = h-y

result = min([a,b,x,y])
print(result)