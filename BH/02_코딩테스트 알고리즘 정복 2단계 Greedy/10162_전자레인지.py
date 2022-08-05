
import sys

count = [0,0,0]
t = int(sys.stdin.readline().rstrip())

while True:
    if t == 0:
        for c in count:
            print(c, end = " ")
        break

    if t//300 != 0:
        count[0] +=1
        t -= 300
    elif t//60 != 0:
        count[1] += 1
        t -= 60
    elif t // 10 != 0:
        count[2] += 1
        t -= 10
    else:
        print(-1)
        break

