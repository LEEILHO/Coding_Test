#구독자 전쟁
T = int(input())
for tc in range(1,T+1):
    n,a,b = map(int, input().split())
    max_subscriber = min(a,b)
    if (a+b)<=n:
        min_subscriber=0
    else:
        min_subscriber = (a+b) -n
    print(f"#{tc} {max_subscriber} {min_subscriber}")