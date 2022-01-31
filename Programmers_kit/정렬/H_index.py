def solution(citations):
    answer = 0
    list = sorted(citations, reverse=True)
    max = list[0]

    for h in range(max, -1, -1):
        new = [x for x in list if x >= h]

        if len(new) >= h and len(list) - len(new) <= h:
            answer = h
            break
    return answer

# 다른 사람
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


print(solution([3, 0, 6, 1, 5]	))