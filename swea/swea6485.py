#삼성시의 버스 노선
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AWczm7QaACgDFAWn&categoryId=AWczm7QaACgDFAWn&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    bus_station = [0] * 5001
    for _ in range(n):
        a,b = map(int,input().split())
        for i in range(a,b+1):
            bus_station[i] +=1
    p = int(input())
    print(f"#{tc}",end =' ')
    for _ in range(p):
        c = int(input())
        print(bus_station[c],end =" ")
    print()
    