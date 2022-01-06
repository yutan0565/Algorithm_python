"""
내장 함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수 제공
 - 파이썬 프로그램을 작성할 때 없어서는 안되는 필수적인 기능을 포함
itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공
 - 특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 활용
heapq :  힙(Heap) 자료구조를 제공
 - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
bisect : 이진 탐색 (Binary Search)기능을 제공
collections : 덱(deque), 카운터(Counter)등의 유용한 자료구조를 포함
math : 필수적인 수학적 기능을 제공
 - 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 고나련 함수부터 파이(pi)와 같은 상수를 포함
"""

#내장 함수
#sum()
result = sum([1,2,3,4,5])
print(result)

#min(), max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result," ", max_result)

#eval() - 사람의 입장에서 수식으로 표현된 식을 계산한거를 실제 수로 계산해서 반환
result = eval("(3+5)*7")
print(result)

#sorted() 반복가능한 객체를 정렬한 결과 - default = 오름차순
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse = True)
print(result)
print(reverse_result)

#sorted() with key
array = [ ('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key = lambda x: x[1], reverse = True)
print(result)

#순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
from itertools import permutations
data = ['A','B','C']
result = list(permutations(data, 3))
print(result)

#중복 순열
from itertools import product
data = ['A','B','C']
result = list(product(data, repeat = 3))
print(result)

#조합 : 서로 다른 n개에서 순서에 상관 없이 r개를 선택하는 경우
from itertools import combinations
data = ['A','B','C']
result = list(combinations(data,2))
print(result)

#중복 조합
from itertools import combinations_with_replacement
data = ['A','B','C']
result = list(combinations_with_replacement(data, 2))
print(result)

#Counter : 등장 횟수를 세는 기능을 제공
# - 리스트와 같은 반복 가능한 객체가 주어졌을 떄 내부의 원소가 몇 번 등장한지 확인
from collections import Counter
counter = Counter(['red', 'blue' ,'red','green','blue' ,'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))

#math : 최대 공약수를 구해야 할 때는 math의 gcd()함수를 이용 가능
# 최소 공배수(LCM)을 구하는 함수
import math
def lcm(a,b):
    return a*b // math.gcd(a,b)

print(math.gcd(21,14))
print(lcm(21,14))
