n = 1260 # 금액
count = 0 # 몇개의 동전?

#큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]
for coin in array: # 모든 코인에 대해서 큰거부터 나눠 주기
    count += n//coin
    n %=coin # 거스름돈 구하기
print(count)