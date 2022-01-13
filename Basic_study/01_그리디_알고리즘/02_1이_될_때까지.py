# n과, k에 입력한 값을 나눠서 할당 해주기
n, k  = map(int, input().split())

result = 0

while True:
    #N이 K로 나누어 떨어지는 수가 될 떄까지 빼기
    target = (n//k)*k # k로 나눴을때 나머지 - 빼야되는 수
    result += (n - target)  # 나눠지는 수로 만들기
    n = target   # 1씩 빼니까 target은 1을 뺀 횟수
    # N이 K보다 작을 떄 (더 이상 나눌 수 없을 떄) 반복문 탈출
    if n < k:
        break
    #K로 나누기
    result += 1
    n //=k

# k보다 작은 n에 대해서 1씩 빼기
result += (n-1)
print(result)