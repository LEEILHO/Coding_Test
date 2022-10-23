#USB 꽂기의 미스터리
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AXDNEA3aaU0DFAVX&categoryId=AXDNEA3aaU0DFAVX&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

T = int(input())
for tc in range(1,T+1):
    p,q = map(float,input().split())
    # 첫번째에 못꽂아서 뒤집어서 꽂히는 경우
    s1 = (1-p) * q
    # 처음에도 올바른 면 하지만 뒤집고 올바르면 아님 뒤집고
    s2 = p*(1-q) *q 
    print(f'#{tc}', "YES" if s2>s1 else "NO")