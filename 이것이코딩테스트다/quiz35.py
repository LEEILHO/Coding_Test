""" 못생긴 수
2,3,5 만을 소인수로 가지는 수를 못생긴 수라 정의
1은 못생긴수라고 가정 이때, n번째 못생긴수를 찾는 프로그램을 작성"""
n = int(input())
dp = [0] * n
dp[0] =1
i2 = i3 =i5 =0
next2, next3, next5 = 2,3,5
for i in range(1,n):
    dp[i] = min(next2,next3,next5)
    
    if dp[i] == next2:
        i2+=1
        next2 = dp[i2] * 2
    if dp[i] == next3:
        i3+=1
        next2 = dp[i3] * 3
    if dp[i] == next5:
        i5+=1
        next2 = dp[i5] * 5
print(dp[n-1])
        
    
    