#24시간

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int,input().split())
    result = (a+b)%24
    print("#{} {}".format(test_case,result))
    