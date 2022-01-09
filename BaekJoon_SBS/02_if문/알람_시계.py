h, m = map(int, input().split())

if m >= 45:
    m -= 45
else:
    m_mod = 45 - m
    h -= 1
    m = 60 - m_mod
    if h < 0:
        h += 24
print(h,m)