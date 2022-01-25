import sys

N = int(sys.stdin.readline())
five = 0
three = 0

while(True):

    if (N - 3 * three)  == 1 or (N - 3 * three)  == 2 :
        result = -1
        break

    if (N-3*three)%5 == 0 :
        five = (N-3*three)// 5
        result = five + three
        break
    else:
        three += 1


print(result)