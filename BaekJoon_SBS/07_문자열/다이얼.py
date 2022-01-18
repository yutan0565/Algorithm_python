## 다시 꼭 풀어보기

import sys

s_list = list(sys.stdin.readline().strip())
N_list = ['ABC','EDF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

result = 0

for s in s_list:
    for n in N_list:
        if s in n:
            ### 이거 기억해두면 좋음!!!!!!!!!
            result += N_list.index(n) +3

print(result)