import sys
import math

m,n = map(int, sys.stdin.readline().rstrip().split())

def isprime(number):
    if number == 1:
        return False
    else:
        for i in  range(2, int(math.sqrt(number))+1):
            if number % i ==0:
                return False
        return True


for i in range(m, n+1):
    if isprime(i) == True:
        print(i)



def isprime_1(m,n):
    q = int(math.sqrt(n))
    result = [ i for i in range(m, n+1)]

    for i in range(2, q+1):
        for j in result:
            if j %i == 0 and j != i :
                result.remove(j)

    return result