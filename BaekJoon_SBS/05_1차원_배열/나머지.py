import sys

a = []

for i in range(10):
    number = int(sys.stdin.readline())
    temp = number%42
    if temp not in a:
        a.append(temp)
print(len(a))