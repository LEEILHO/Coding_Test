#USB 꽂기의 미스터리
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AXDNEA3aaU0DFAVX&categoryId=AXDNEA3aaU0DFAVX&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

T = int(input())
for tc in range(1,T+1):
    p,q = map(float,input().split())
    
    s1 = (1-p) * q
    s2 = p*(1-q) *q 
    print(f'#{tc}', "YES" if s2>s1 else "NO")