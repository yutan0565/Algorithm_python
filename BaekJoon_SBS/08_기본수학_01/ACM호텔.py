import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    h,w,n = map(int, sys.stdin.readline().split())
    fl = n % h
    number = n // h + 1

    if fl == 0:
        fl = h
        number = n // h

    if number < 10:
        print("{}{}{}".format(fl,0,number))
    else:
        print("{}{}".format(fl,number))

