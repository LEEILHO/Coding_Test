""" 정수 삼각형
맨 위층 부터 시작하여 아래에 있는 수 중 하나를 선택하여 아래로 내려올 때 이제까지 선택된 수의 합이 최대가 되는 경로를
구하는 프로그램을 작성하시오 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 혹은 오른쪽 있는 것 중에서만 선택할 수 있다."""


N = int(input())
dp = []
for i in range(N):
    dp.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i+1):
        if j==0:
            left_top=0
        else:
            left_top = dp[i-1][j-1]
        if j == i:
            right_top =0
        else:
            right_top=dp[i-1][j]
        dp[i][j] += max(left_top,right_top)
result = max(dp[N-1])
print(result)
            
    