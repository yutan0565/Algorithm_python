import math


def solution(brown, yellow):
    answer = []

    for i in range(1, int(math.sqrt(yellow) + 1)):
        if yellow % i == 0:
            if 2 * (i + (yellow / i)) + 4 == brown:
                answer = [int(yellow / i) + 2, i + 2]
                break

    return answer

print(solution(10,2))