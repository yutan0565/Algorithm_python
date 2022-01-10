import sys

a = int(sys.stdin.readline())
n = 0
if a < 10:
    a = a * 10
a_new = a
while (True):]
    num_1 = a_new%10
    num_2 = a_new//10
    temp = num_1+num_2

    temp_1 = temp%10
    a_new = num_1*10 + temp_1
    n += 1
    if a == a_new:
        break
print(n)

"""
n = int(input())
b = (n%10)*10 + (((n%10)+(n//10))%10)
a = 1
while  b != n :
    b = (b%10)*10 + (((b%10)+(b//10))%10)
    a = a + 1
print(a)
"""