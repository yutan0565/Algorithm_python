import sys
from itertools import combinations_with_replacement

# 짝수 조건을 활용 해주기

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    a = n//2
    b = a

    for k in range(a):
        if isprime(a) and isprime(b) and a+b == n:
            print(a,b)
            break
        else:
            a -= 1
            b += 1




"""
def isprime(n, number_list):
    for i in range(2, int(n**0.5) +1):
        if number_list[i] == True:
            for j in range(i+i, n+1, i):
                number_list[j] = False
    return [i for i in range(2,n+1) if number_list[i] == True]

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    number_list = [True] * ( n + 1)
    prime_list = isprime(n, number_list)
    combi = list(combinations_with_replacement(prime_list, 2))
    combi.sort(key = lambda x : x[1]-x[0])
    for i in combi:
        a,b = map(int, i)
        if a+b == n:
            print("{} {}".format(a,b))
            break
"""