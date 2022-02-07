import sys

# ### 이거는 꼭 외워 두기!!!
# number_list =  [[2,4],[3,2],[1,2], [1,3]]
# number_list.sort( key = lambda x : (x[0] , x[1]))
# print(number_list)


n = int(sys.stdin.readline().rstrip())

c = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]



# 가장 빨리 끝나는 애들 순위 !!!!!!!!!!!!!!!!
c.sort(key = lambda x : (x[1], x[0] ))

end = c[0][1]
cnt = 1

for i in range(1, n):
    if c[i][0] >= end:
        cnt += 1
        end = c[i][1]

print(cnt)
