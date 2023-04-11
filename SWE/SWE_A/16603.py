

def find_pos():
    x,y = 0,0
    pos_list = []
    num_list = []
    for direct in range(4):
        if direct % 2 == 0 :
            len_ = m
        else:
            len_ = n
        for _ in range(len_ -1 ):
            x = x + dx[direct]
            y = y + dy[direct]
            pos_list.append([x,y])
            num_list.append(graph[x][y])
    return pos_list, num_list

def rotation_right(pos_list, num_list,k):
    new_num_list = num_list[-k:] + num_list[:-k]
    for i in range(len(pos_list)):
        nx,ny = pos_list[i]
        graph[nx][ny] = new_num_list[i]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 테스트 케이스 번호
    t = int(input())
    n,m,k = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]

    pos_list, num_list = find_pos()
    rotation_right(pos_list, num_list,k)
    print("#{}".format(t))
    for i in range(n):
        for j in range(m):
            print(graph[i][j], end = " ")
        print()