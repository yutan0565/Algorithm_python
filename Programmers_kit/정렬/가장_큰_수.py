
numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    # 숫자를 모두 string으로 빠꾸고, list에 넣어준다.
    numbers = list(map(str, numbers))

    # 리스트를 내림차순으로 정렬
    # 조건에서 3자리수 이하를 비교하기 때무넹, string을 3번 나열해서
    # 아스키코드 값으로 정렬을하게 해준다.
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

print(solution(numbers))