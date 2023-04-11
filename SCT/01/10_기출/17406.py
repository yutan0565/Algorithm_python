import copy
import sys
from itertools import permutations


def find_array_min(list_2d):
    min_value  = int(1e9)
    for i in range(len(list_2d)):
        min_value = min(sum(list_2d[i]), min_value)
    return min_value

def block_rotation(x,y,s):
    temp_graph = copy.deepcopy(graph)
    for layer in range(1,s+1):
        # 위
        temp_graph[x-layer][y-layer+1:y+layer+1] = graph[x-layer][y-layer:y+layer]
        # 아래
        temp_graph[x+layer][y-layer:y+layer] = graph[x+layer][y-layer+1:y+layer+1]
        #오른
        for row in range(x+layer, x-layer,-1):
            temp_graph[row][y+layer] = graph[row-1][y+layer]
        #왼
        for row in range(x-layer, x+layer):
            temp_graph[row][y-layer] = graph[row+1][y-layer]
    return temp_graph


n,m,k = map(int,sys.stdin.readline().rstrip().split())
reset_graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

list_rotation =[]
for _ in range(k):
    r,c,s = map(int,sys.stdin.readline().rstrip().split())
    x_start = r - 1
    y_start = c  - 1
    list_rotation.append([x_start,y_start,s])

list_candi_rotation = list(permutations(list_rotation, len(list_rotation)))

result = int(1e9)
for candi in list_candi_rotation:
    graph = copy.deepcopy(reset_graph)
    for x,y,s in candi:
        graph = block_rotation(x,y,s)
    temp = find_array_min(graph)
    result = min(temp, result)
print(result)

