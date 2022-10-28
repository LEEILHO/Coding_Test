# 새샘이의 7-3-5 게임
from itertools import combinations
T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    combi = combinations(arr,3)
    result =[]
    for i in combi:
        result.append(sum(i))
    result = set(result)
    result = sorted(result, reverse = True)
    print("#{} {}".format(tc,result[4]))
    