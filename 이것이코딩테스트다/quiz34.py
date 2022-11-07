""" 병사 배치하기
N명의 병사가 무작위로 나열 
각 병사는 특정한 값이 전투력을 보유
병사를 배치할 때는 전투력이 높은 병사가 앞에오도록 배치
병사의 정보가 주어졌을 떄 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를
출력 하는 프로그램"""
N = int(input())
arr = list(map(int, input().split()))
dp =[1] * N
arr.reverse()

for i in range(1,N):
    for j in range(0,i):
        if arr[j] <arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(N-max(dp))
    