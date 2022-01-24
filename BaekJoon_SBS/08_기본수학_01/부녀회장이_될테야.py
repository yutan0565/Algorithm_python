import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    # 0 번쨰 층에 있는 사람들
    f_0 = [i for i in range(1, 1+n)]

    for i in range(k):   # 지정한 층수 만큼 아래 과정을 만복
        for j in range(1, n):    # 1호 부터 ~~ n 호까지 반복
            f_0[j] +=  f_0[j-1]    #  새로운 층의 2호는,
    print(f_0[n-1])



