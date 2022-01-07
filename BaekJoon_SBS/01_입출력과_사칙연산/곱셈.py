a = int(input())
b = int(input())

b = str(b)

def func_03(a,b):
    num_01 = (b%10)
    return a*num_01

def func_04(a,b):
    num_02 = (b%100)//10
    return a*num_02

def func_05(a,b):
    num_03 = b//100
    return a*num_03

def func_06(a,b):
    return a*b

print(func_03(a,b))
print(func_04(a,b))
print(func_05(a,b))
print(func_06(a,b))