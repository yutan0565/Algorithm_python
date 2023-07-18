import copy
import sys
from collections import deque

class NODE():
    def __init__(self, name, work_list, parent_node):
        self.name = name
        self.q = deque(work_list)
        self.parent = parent_node
        self.left_q = deque()
        self.right_q = deque()

# 조직도의 높이 / 말단에서 대기하는 업무의 개수 / 업무 진행되는 날 수
h,k,r = map(int,sys.stdin.readline().rstrip().split())
work_candi = deque()
for _ in range(2**h):
    work_candi.append(list(map(int,sys.stdin.readline().rstrip().split())))

node_num = 1
node_count = 1

node_list = [NODE(i,[],None) for i in range(2**(h+1))]
check_index = 1

clear_work_list = []
for num in range(2**(h+1)):
    parent_node = num // 2
    if 2**h <= num:
        node_list[num].q = deque(work_candi.popleft())
    node_list[num].parent = parent_node

# for num in range(1,2**(h+1)):
#     print("===================")
#     print("번호 : ", num)
#     print("부모 : ", node_list[num].parent)
#     print("큐 : ", list(node_list[num].q))


for round in range(1, r+1):
    # 대장님
    if len(node_list[1].left_q) != 0 and round %2 == 1:
        up_work = node_list[1].left_q.popleft()
        node_list[0].q.append(up_work)
    elif len(node_list[1].right_q) != 0 and round %2 == 0:
        up_work = node_list[1].right_q.popleft()
        node_list[0].q.append(up_work)

    # 중간
    for node_num in range(2, 2**h):
        # 왼쪽꺼 올라감
        if round %2 == 1 :
            parent_node = node_list[node_num].parent
            # left에서 올라오는거는 왼쪽에 넣기
            if node_num %2 == 0:
                if len(node_list[node_num].left_q) != 0:
                    node_list[parent_node].left_q.append(node_list[node_num].left_q.popleft())
            elif node_num %2 == 1:
                if len(node_list[node_num].left_q) != 0:
                    node_list[parent_node].right_q.append(node_list[node_num].left_q.popleft())

        # 오른쪽꺼 올라가는날
        elif round %2 == 0 :
            parent_node = node_list[node_num].parent
            # left에서 올라오는거는 왼쪽에 넣기
            if node_num %2 == 0:
                if len(node_list[node_num].right_q) != 0:
                    node_list[parent_node].left_q.append(node_list[node_num].right_q.popleft())
            elif node_num %2 == 1:
                if len(node_list[node_num].right_q) != 0:
                    node_list[parent_node].right_q.append(node_list[node_num].right_q.popleft())

    # 맨 아래
    for node_num in range(2 ** h, 2**(h+1)):
        parent_node = node_list[node_num].parent
        if len(node_list[node_num].q) != 0:
            if node_num % 2 == 0:
                node_list[parent_node].left_q.append(node_list[node_num].q.popleft())
            elif node_num %2 == 1:
                node_list[parent_node].right_q.append(node_list[node_num].q.popleft())

    # print()
    # print()
    # for num in range(0,2**(h+1)):
    #     print("===================")
    #     print("번호 : ", num)
    #     print("부모 : ", node_list[num].parent)
    #     print("큐 : ", node_list[num].q)
    #     print("왼쪽 큐 : ", node_list[num].left_q)
    #     print("오른쪽 큐 : ", node_list[num].right_q)
#
#
# print(node_list[0].q)

print(sum(list(node_list[0].q)))
