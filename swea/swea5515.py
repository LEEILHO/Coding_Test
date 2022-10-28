#2016년 요일 맞추기
T = int(input())

for tc in range(1,T+1):
    m,d = map(int,input().split())
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day =0
    for i in range(1,m):
        day +=month[i]
    day += d
    if day %7 ==0:
        result =3
    elif day %7 ==1:
        result =4
    elif day %7 ==2:
        result =5
    elif day %7 ==3:
        result =6
    elif day %7 ==4:
        result =0
    elif day %7 ==5:
        result =1
    elif day %7 ==6:
        result =2
    print(f"#{tc} {result}")
    