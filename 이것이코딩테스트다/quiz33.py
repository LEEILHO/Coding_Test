""" 퇴사
오늘부터 N+1일째 되는 날 퇴사를 하기 위해 N일동안 많은 상담
상담을 완료하는데 걸리는 시간 T 받을 수 있는 금액 P
상담하는데 필요한 기간을 1일보다 클 수 있어 모든 상담을 할 수는 없다."""

N = int(input())
t = []
p =[]
dp =[0]*(N+1)
max_value =0
for _ in range(N):
    x,y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(N-1,-1,-1):
    time = t[i] + i
    if time <= N:
        dp[i] = max(p[i] + dp[time],max_value)
        max_value =dp[i]
    else:
        dp[i] = max_value
print(max_value)        