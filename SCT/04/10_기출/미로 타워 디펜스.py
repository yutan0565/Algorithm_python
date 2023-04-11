import sys

def make_full_line():
    global mon_line
    new_mon_line = []
    for m in mon_line:
        if m >= 1:
            new_mon_line.append(m)
    new_mon_line = new_mon_line + [0 for _ in range(n*n-1-len(new_mon_line))]
    mon_line = new_mon_line

def make_graph_index():
    graph_index = [[-1 for _ in range(n)] for _ in range(n)]
    mon_line = []
    x,y = cen_x,cen_y
    direct = 0
    count = 1
    index = 0
    while 1:
        for _ in range(2):
            for _ in range(count):
                x = x + dx[direct]
                y = y + dy[direct]
                if not(0<=x<n and 0<=y<n):
                    return graph_index,mon_line
                graph_index[x][y] = index
                mon_line.append(graph[x][y])
                index += 1
            direct = (direct + 1)%4
        count += 1

def attack_line(direct,p):
    global total_score
    x,y = cen_x,cen_y
    for mul in range(1,p+1):
        nx = x + dx_attack[direct]*mul
        ny = y + dy_attack[direct]*mul
        del_index = graph_index[nx][ny]
        total_score += mon_line[del_index]
        mon_line[del_index] = 0
    make_full_line()

def del_same_mon():
    global total_score
    temp = []
    new_mon_line = []
    del_flag = -1
    for m in mon_line:
        if m == 0:
            if len(temp) >= 4:
                total_score += sum(temp)
                del_flag = 1
            else:
                new_mon_line = new_mon_line + temp
            break
        if temp == []:
            temp.append(m)
            continue
        else:
            if m == temp[0]:
                temp.append(m)
            else:
                if len(temp) >= 4:
                    total_score += sum(temp)
                    temp = [m]
                    del_flag = 1
                else:
                    new_mon_line = new_mon_line + temp
                    temp = [m]
    return new_mon_line,del_flag

def make_new_mon_line():
    temp = []
    new_mon_line = []
    for m in mon_line:
        if m == 0:
            new_mon_line = new_mon_line + [len(temp),temp[0]]
            break
        if temp == []:
            temp.append(m)
            continue
        else:
            if m == temp[0]:
                temp.append(m)
            else:
                new_mon_line = new_mon_line + [len(temp),temp[0]]
                temp = [m]
    return new_mon_line[:n*n-1]

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
cen_x,cen_y = n//2,n//2
dx = [0,1,0,-1]
dy = [-1,0,1,0]
graph_index, mon_line  = make_graph_index()

dx_attack = [0,1,0,-1]
dy_attack = [1,0,-1,0]

total_score = 0
for round in range(1,m+1):
    direct, p = map(int,sys.stdin.readline().rstrip().split())
    # 타워 중심 공격
    attack_line(direct,p)
    # 4번 반복되는 거 지우기
    while 1:
        mon_line,flag = del_same_mon()
        make_full_line()
        if flag == -1:
            break
    # 새로운 라인 만들기
    mon_line = make_new_mon_line()
    make_full_line()
print(total_score)