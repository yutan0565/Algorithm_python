def solution(n, lost, reserve):
    # 새로운 여분 있는사람 만들기,   잃어버린 사람은 다시 1개가 되기 때문
    _reserve = [r for r in reserve if r not in lost]

    # 아무것도 없는 사람 만들기,  여분이 있으면 제외 하기
    _lost = [l for l in lost if l not in reserve]

    # 여분이 있는 사람의 앞, 뒤 중에서
    for r in _reserve:
        front = r - 1
        back = r + 1
        # 앞 뒤 둘중에 한명만 주기
        if front in _lost:
            _lost.remove(front)
        elif back in _lost:
            _lost.remove(back)
            # 아무것도 없는사람은 제외한 나머지
    return n - len(_lost)

# 예외가 뭐지

n = 5
lost = [1,5]
reserve = [3]

print(solution(n,lost,reserve))