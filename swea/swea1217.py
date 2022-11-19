def power(n,m):
    if m ==M:
        return n
    elif m < M :
        
        return n * power(n,m+1)
    
    
for _ in range(1,11):
    tc = int(input())
    N,M = map(int, input().split())
    result =power(N,1)
    print(f"#{tc} {result}")