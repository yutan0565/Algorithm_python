import sys
import math
t = int(sys.stdin.readline())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())

    suk_jo = math.sqrt((x2-x1)**2 + (y2-y1)**2 )

    if suk_jo==0 and r1 == r2:
        print(-1)
    elif r1 + r2 == suk_jo  or abs(r1 - r2) == suk_jo:
        print(1)
    elif abs(r1-r2) < suk_jo < abs(r1+r2):
        print(2)
    else:
        print(0)

    # if r1 + r2 < suk_jo  or r1 > r2+suk_jo or r2 > r1+suk_jo or (x1==x2 and y1== y2 and r1 != r2):
    #     print(0)
    # elif r1 + r2 == suk_jo  or r1 == r2+suk_jo or r2 == r1+suk_jo:
    #     print(1)
    # elif x1==x2 and y1== y2 and r1 == r2:
    #     print(-1)
    # else:
    #     print(2)
