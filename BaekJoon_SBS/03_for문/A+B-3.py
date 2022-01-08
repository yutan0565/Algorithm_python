T = int(input())

def add(a,b):
    return a+b

for _ in range(T):
    a,b = map(int, input().split())
    print(add(a,b))