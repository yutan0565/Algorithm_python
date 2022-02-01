from  itertools import permutations

def isprime(n):
    if n < 2:
       return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0

    number = [ str(i) for i in numbers]
    temp= []
    for i in range(1, len(number)+1):
        number_list = list(map(''.join,permutations(number,i)))
        for k in list(set(number_list)):
            if isprime(int(k)):
                temp.append(int(k))
    answer = len(set(temp))
    return answer

print(solution("110"))