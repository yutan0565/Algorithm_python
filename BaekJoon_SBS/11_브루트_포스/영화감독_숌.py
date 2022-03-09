import sys

n = int(sys.stdin.readline())

name = 666

while True:
    if "666" in str(name):
        n -= 1
    if n == 0:
        break
    name += 1
print(name)


