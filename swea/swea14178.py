# 1차원 정원

T = int(input())

for test_case in range(1, T + 1):
    n,d = map(int,input().split())
    width = 2*d +1
    if n%width ==0:
        result = n//width
    else:
        result = (n//width) +1
    print("#{} {}".format(test_case,result))