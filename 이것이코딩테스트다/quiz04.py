""" 만들 수 없는 금액
N개의 동전을 가지고 있음 이때 n개의 동전을 이용하여 만들 수 없는 금액 중 최솟값을 구하는 프로그램을 작성하시오.
첫째 줄 n
둘째 줄 화폐의 단위"""

import itertools
n = int(input())
coins = list(map(int,input().split()))

coin_sum = []
result =[]
for i in range(1,n+1):
    coin_sum.append(itertools.combinations(coins,i))
for i in coin_sum:
    for j in i:
        result.append(sum(j))

result = set(result)

check =1

for i in result:
    if i != check:
        print(check)
        break
    else:
        check +=1

# 답
# n = int(input())
# data = list(map(int,input().split()))
# data.sort()

# target =1
# for x in data:
#     if target <x:
#         break
#     target += x
# print(target)

        
