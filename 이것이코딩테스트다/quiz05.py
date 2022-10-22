"""볼링공 고르기 
두사람은 서로 무게가 다른 볼링공을 고르려고 합니다.
볼링공은 N개가 있으며 공의 번호는 1번부터 순서대로 부여 같은 무게의 공이 여러개 있지만 서로 다른공으로 간주
두사람이 고를 수 있는 봉링공 번호의 조합의 수를 구하시오.
"""
n ,m = map(int, input().split())
balls = list(map(int, input().split()))
result =0

import itertools

arr = itertools.combinations(balls, 2)
for i in arr:
    if i[0] != i[1]:
        result +=1
print(result)
'''
답
n,m = map(int, input().split())
arr = [0] * (m+1)

data = list(map(int, input().split()))
for x in data:
    arr[x] +=1

result =0
for i in range(1,m+1):
    n -= arr[i]
    result += n* arr[i]
print(result)
'''