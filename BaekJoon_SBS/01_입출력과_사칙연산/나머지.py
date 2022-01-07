a,b,c  = map(int, input().split())

def func_01(a,b,c):
    return (a+b)%c

def func_02(a,b,c):
    return ((a%c)+(b%c))%c

def func_03(a,b,c):
    return (a*b)%c

def func_04(a,b,c):
    return ((a%c)*(b%c))%c

print(func_01(a,b,c))
print(func_02(a,b,c))
print(func_03(a,b,c))
print(func_04(a,b,c))