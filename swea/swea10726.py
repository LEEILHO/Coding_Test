#이진수 표현
T = int(input())

for tc in range(1,T+1):
    n,m = map(int,input().split())
    result = False
    for cnt in range(n):
        if m ==0:
            break
        elif m==1:
            if cnt ==n-1:
                result =True
            else:
                result = False
                break
        else:
            if m%2==1:
                result =True
                m =m//2
            else:
                result =False
                break
    if result ==True:
        print(f"#{tc} ON")
    else:
        print(f"#{tc} OFF")
            