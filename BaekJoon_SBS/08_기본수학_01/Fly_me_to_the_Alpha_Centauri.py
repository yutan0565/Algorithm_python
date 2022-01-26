import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x,y = map(int, sys.stdin.readline().split())

    m = y-x
    k = 1
    total = 0
    count = 0

    while(True):
        total += k * 2

        if total < m:
            count += 2
            k += 1
            temp = total
        else:
            if (m - temp) >= k+1 :
                count += 2
            else:
                count += 1
            break
    print(count)




    # while(True):
    #     m = m - 2 * k
    #     count += 2
    #     k += 1
    #     if  m < 2*(k+1) and m > 2*(k-1):
    #         count += 2
    #         break
    #     if m <= k+1 and m >= k-1:
    #         count += 1
    #         break



