def solution(answers):
    answer = []
    temp = []
    a = [1, 2, 3, 4, 5] * (len(answers) // 5 + 1)
    b = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1)
    temp.append(a)
    temp.append(b)
    temp.append(c)

    max = 0
    for k, n in enumerate(temp):
        score = 0
        for i in range(len(answers)):
            if answers[i] == n[i]:
                score += 1
        if max < score:
            answer = []
            answer.append(k + 1)
            max = score
        elif max == score:
            answer.append(k + 1)

    return answer


# 다른사람 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

answers = [1,2,3,4,5]

print(solution(answers))