import sys

s = list(sys.stdin.readline().strip())
al_list = [chr(i) for i in range(97,123)]
n = 0
for i in al_list:
    if i in s:
        index = 0
        for j in range(len(s)):
            if i == s[j]:
                index = j
                break
        al_list[n] = index
    else:
        al_list[n] = -1
    n += 1
for i in al_list:
    print(i, end=" ")


