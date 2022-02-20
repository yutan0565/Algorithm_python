import sys

a,b,c = map(int, sys.stdin.readline().rstrip().split())

if a== b and b == c:
    result = 10000 + a*1000
elif a == b :
    result = 1000 + a*100
elif a == c :
    result = 1000 + a*100
elif c == b:
    result = 1000 + b*100
else:
    result = max([a,b,c])*100
print(result)