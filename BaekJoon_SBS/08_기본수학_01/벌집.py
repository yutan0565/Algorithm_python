import sys


number = int(sys.stdin.readline())

count = 1
cut =1

while(True):
    if cut >= number:
        break
    cut += count * 6
    count += 1

print(count)
