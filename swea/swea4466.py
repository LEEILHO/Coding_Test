#최대 성적표 만들기
T = int(input())
for tc in range(1,T+1):
    N,K = map(int, input().split())
    score = list(map(int, input().split()))
    score = sorted(score,reverse =True)
    result =0
    for i in range(K):
        result += score[i]
    print(f"#{tc} {result}")