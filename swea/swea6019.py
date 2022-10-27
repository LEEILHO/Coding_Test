# 기차사이의 파리
T = int(input())
for tc in range(1,T+1):
    d,a,b,f = map(int,input().split())
    time = d/(a+b)
    dis = time * f
    print(f"#{tc} {dis}")