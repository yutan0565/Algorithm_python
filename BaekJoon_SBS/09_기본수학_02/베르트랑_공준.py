import sys
import math

def isprime(prime_list, n ):
    for i in range(2, int(math.sqrt(2*n+1))+1):
        if prime_list[i] == True:
            for j in range(i*2, 2*n+1, i):
                prime_list[j] = False
    return prime_list

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    prime_list = [True] * (2*n + 1)
    result = isprime(prime_list, n)
    answer = [i for i in range(n+1,2*n+1) if result[i] == True]
    print(len(answer))

"""
시간 초과
def isprime(n):
    if n == 1:
        return False

    for i in range(2,int(math.sqrt(n))+1 ):
        if n % i == 0:
            return False
    return True

while( True):
    n = int(sys.stdin.readline())
    count = 0
    if n == 0:
        break
    else:
        for i in range(n+1, 2*n+1):
            if isprime(i) == True:
                count += 1
        print(count)
"""