import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
price_pac = []
price_indi = []
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    price_pac.append(a)
    price_indi.append(b)

if min(price_pac) > 6*min(price_indi):
    result = n * min(price_indi)
else:
    if min(price_pac) >= (n%6)*min(price_indi):
        result = (n//6)*(min(price_pac)) + (n%6)*(min(price_indi))
    else:
        result = (n // 6 +1) * (min(price_pac))

print(result)
