import sys

def count_change(g):
    a_count = 0
    b_count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if g[i][j] == 'B':
                    a_count += 1
                if g[i][j] == 'W':
                    b_count += 1
            else:
                if g[i][j] == 'W':
                    a_count += 1
                if g[i][j] == 'B':
                    b_count += 1
    return min(a_count, b_count)

n,m = map(int, sys.stdin.readline().rstrip().split())
ori_graph= [ list(sys.stdin.readline().rstrip()) for _ in range(n)]
result = 1000

for a in range(n-8+1):
    for b in range(m-8+1):
        new_graph = [ [0 for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                new_graph[i][j] = ori_graph[a+i][b+j]
        t = count_change(new_graph)
        result = min(result, t)
print(result)


