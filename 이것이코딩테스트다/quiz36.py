""" 편집 거리
문자열A ,B가 주어졌을 때 문자열 A를 편집하여 B를 만든다
1. 삽입
2. 삭제
3. 교체
이때 편집 거리란 사용한 연산의 수를 의미
최소 편집 거리를 계산하는 프로그램을 작성하시오."""
def edit_dist(str1,str2):
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1,m+1):
        dp[0][j] = j
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if str[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
    return dp[n][m]
A = input()
B = input()
print(edit_dist(A,B))
