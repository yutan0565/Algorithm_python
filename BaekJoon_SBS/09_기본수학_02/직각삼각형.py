import sys

def issqrt(x,y,z):
    if x**2 + y**2 == z**2:
        return True
    else:
        return False


while (True):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())

    if a ==0 and b ==0 and c == 0:
        break
    if issqrt(a,b,c):
        print("right")
    elif issqrt(a,c,b):
        print("right")
    elif issqrt(b,c,a):
        print("right")
    else:
        print("wrong")
