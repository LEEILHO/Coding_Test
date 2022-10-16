# 구구단
T = int(input())
for test_case in range(1,T+1):
    a,b = map(int,input().split())
    if a <=9 and b <=9:
        result = a * b
    else:
        result = -1
    print("#{} {}".format(test_case,result))