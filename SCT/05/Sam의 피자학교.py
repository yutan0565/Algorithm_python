import copy
import sys

def show_graph():
    for g in graph:
        print(g)

def check_lastline():
    last_line = graph[-1]
    if (max(last_line) - min(last_line)) <= k:
        return True
    return False

def make_roll_end_list():
    "0 1 3 5 8 11 "
    "  1 2 2 3 3 4 4 "
    roll_end_list = [0,1]
    now_end = 1
    scale = 2
    while 1:
        for _ in range(2):
            now_end += scale
            if now_end > 2*n:
                return roll_end_list
            else:
                roll_end_list.append(now_end)
        scale += 1

def make_roll_height_width_list():
    roll_width_list = []
    roll_height_list = []
    for i in range(1, n+3):
        for _ in range(2):
            roll_width_list.append(i)

    roll_height_list = roll_width_list[1:]

    roll_width_list = roll_width_list[:len(roll_end_list)]
    roll_height_list = roll_height_list[:len(roll_end_list)]
    return roll_width_list, roll_height_list

def add_mil():
    global graph
    last_line = graph[-1]
    max_value = min(last_line)
    for i in range(len(last_line)):
        if last_line[i] == max_value:
            last_line[i] += 1
    graph = graph[:-1] + [last_line]

def rotate_right(move_block, now_width, now_height):
    new_width = now_height
    new_height = now_width
    new_block = [[0 for _ in range(new_width)] for _ in range(new_height)]
    for i in range(now_height):
        for j in range(now_width):
            new_block[j][new_width -1 -i] = move_block[i][j]
    return new_block

def roll_dow():
    for i in range(2*n):
        if i == 2*n -1:
            break
        now_end = roll_end_list[i]
        next_end = roll_end_list[i+1]
        now_width = roll_width_list[i]
        now_height = roll_height_list[i]

        # 만약 접었는데, 넘어가게 되는 거면
        if next_end >= n:
            break
        # 첫 시작인 경우
        if now_end == 0:
            graph[n-1][0],graph[n-2][1] = graph[n-2][1],graph[n-1][0]
        # end == 1 부터
        else:
            move_block = [[0 for _ in range(now_width)] for _ in range(now_height)]
            # 움직일 블록 결정
            width_start = now_end - now_width + 1
            width_end = now_end
            height_start = n - now_height
            height_end = n - 1
            for i in range(n):
                for j in range(n):
                    if height_start<=i<=height_end and  width_start <=j<=width_end:
                        nx = i - height_start
                        ny = j - width_start
                        move_block[nx][ny] = graph[i][j]
                        graph[i][j] = 0 # 옮길 부분 초기화

            # 옮길 블록 오른쪽으로 돌리기
            rotate_block =  rotate_right(move_block, now_width, now_height)

            # 그래프에 올려주기
            new_width = now_height
            new_height = now_width
            for i in range(new_height):
                for j in range(new_width):
                    nx = n - now_width - 1 + i
                    ny = now_end + 1 + j
                    graph[nx][ny] = rotate_block[i][j]

def push_dow():
    global graph
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                now_value = graph[i][j]
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        other_value = graph[nx][ny]
                        if other_value != 0:
                            moc = abs(now_value - other_value) // 5
                            if now_value > other_value:
                                new_graph[i][j] -= moc
                                new_graph[nx][ny] += moc

    # 열이 작은거, 행이 큰것 부터
    new_list = []
    for col in range(n):
        for row in range(n-1,-1,-1):
            if new_graph[row][col] != 0:
                new_list.append(new_graph[row][col])
    graph = [[0 for _ in range(n)] for _ in range(n-1)] + [new_list]

def rotate_righg_180(move_block, now_width, now_height):
    new_block = [[0 for _ in range(now_width)] for _ in range(now_height)]
    for i in range(now_height):
        for j in range(now_width):
            new_block[now_height - i - 1][now_width -1 -j] = move_block[i][j]
    return new_block

def fold_dow():
    for type in range(2):
        now_end = fold_end_list[type]
        now_width = fold_width_list[type]
        now_height = fold_height_list[type]

        move_block = [[0 for _ in range(now_width)] for _ in range(now_height)]
        # 움직일 블록 결정
        width_start = now_end - now_width + 1
        width_end = now_end
        height_start = n - now_height
        height_end = n - 1
        for i in range(n):
            for j in range(n):
                if height_start <= i <= height_end and width_start <= j <= width_end:
                    nx = i - height_start
                    ny = j - width_start
                    move_block[nx][ny] = graph[i][j]
                    graph[i][j] = 0  # 옮길 부분 초기화

        # 옮길 블록 오른쪽으로 돌리기
        rotate_block = rotate_righg_180(move_block, now_width, now_height)

        # 그래프에 올려주기
        for i in range(now_height):
            for j in range(now_width):
                if type == 0:
                    nx = n-2 + i
                    ny = now_end + 1 + j
                else:
                    nx = n-4+i
                    ny = now_end + 1 + j
                graph[nx][ny] = rotate_block[i][j]

def simulation():
    result = 0
    while 1:
        result += 1
        # 밀가루 추가
        add_mil()
        # 도우 말기
        roll_dow()
        # 도우 눌러주기
        push_dow()
        # 두번 반으로 접기
        fold_dow()
        # 도우 눌러주기
        push_dow()
        # 밀가루 최대 최소, 차이 k 이하
        if check_lastline() == True:
            return result


n,k = map(int,sys.stdin.readline().rstrip().split())
graph = [[0 for _ in range(n)] for _ in range(n-1)]
line_list = list(map(int,sys.stdin.readline().rstrip().split()))
graph = graph + [line_list]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
roll_end_list = make_roll_end_list()
roll_width_list ,roll_height_list = make_roll_height_width_list()

fold_end_list = [n//2-1, n//2 + n//4-1]
fold_width_list = [n//2, n//4]
fold_height_list = [1, 2]

result = simulation()
print(result)

