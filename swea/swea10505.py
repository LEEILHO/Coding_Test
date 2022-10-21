# 소득불균형
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    avg_income = sum(arr)/n
    result =0
    for i in arr:
        if i <= avg_income:
            result +=1
    print(f"#{tc} {result}")