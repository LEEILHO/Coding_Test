# 홀수만 더하기
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ans = 0
    arr = list(map(int,input().split()))
    for i in arr: # array값이 홀수이면 결과값에 더함
        if i %2 ==1:
            ans += i
    print("#{} {}".format(test_case, ans))