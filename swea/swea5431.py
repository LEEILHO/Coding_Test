#민석이의 과제 체크하기
T = int(input())
for tc in range(1,T+1):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f"#{tc}",end = ' ')
    for i in range(1,n+1):
        if i not in arr:
            print(i,end =' ')
    print()