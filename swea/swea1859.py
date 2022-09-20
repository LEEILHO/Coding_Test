# 백만 장자 프로젝트 
T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    ans =0
    arr = list(map(int, input().split()))
    max_value = arr[-1] #제일 마지막날을 max값으로 설정
    for i in range(N-1,-1,-1): # 매매가를 마지막날 부터 보면서
        if max_value <= arr[i]: # 매매가가 최대값보다 크면
            max_value = arr[i] #최대값 변경
        ans += (max_value - arr[i]) #최대 매매값에서 현재 매매값 빼서 결과값에 더하기
    print("#{} {}".format(test_case,ans))

