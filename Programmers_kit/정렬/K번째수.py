def solution(array, commands):
    answer = []

    for code in commands:
        start, end, target = map(int, code)
        new = array[start - 1:end]
        new = sorted(new)
        number = new[target - 1]
        answer.append(number)
    return answer

# 다른사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))



array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))