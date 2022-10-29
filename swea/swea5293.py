#이진 문자열 복원
T = int(input())
for tc in range(1,T+1):
    # a =00 b=01, c=10,d=11
    a,b,c,d = map(int, input().split())
    if a!=0 and d != 0 and b==0 and c==0:
        ans = 'impossible'
    elif abs(b-c) > 1:
        ans = 'impossible'
  
    elif b==0 and c==0:
        if a:
            ans = '0'*(a+1)
        elif d:
            ans = '1'*(d+1)
    elif b == c:
        ans = '0'*a+'01'*b+'1'*d+'0'
    elif b>c:
        ans = '0'*a+'01'*b+'1'*d
    else:
        ans = '1'*d + '10'*c + '0'*a
    print(f"#{tc} {ans}")
    