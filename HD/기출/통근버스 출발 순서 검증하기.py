import sys

n = int(sys.stdin.readline().rstrip())
bus_list = list(map(int,sys.stdin.readline().rstrip().split()))
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for j in range(n - 1, -1, -1):
    for x in range(1, n + 1):
        if bus_list[j] < x:
            graph[x][j] = graph[x][j + 1] + 1
        else:
            graph[x][j] = graph[x][j + 1]

result = 0
for i in range(n):
    for j in range(i, n):
        if bus_list[i] < bus_list[j]:
            result += graph[bus_list[i]][j]
print(result)






# def check_stop_flag(bus_list):
#     result_list = []
#     for i_index in range(n-2):
#         for j_index in range(i_index+1,n-1):
#             ai, aj = bus_list[i_index], bus_list[j_index]
#             if ai < aj:
#                 for k_index in range(j_index+1, n):
#                     ak = bus_list[k_index]
#                     if ai > ak:
#                         if [i_index,j_index,k_index] not in result_list:
#                             result_list.append([i_index,j_index,k_index])
#     return result_list