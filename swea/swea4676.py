#늘어지는 소리 만들기
T = int(input())
for tc in range(1,T+1):
    s = list(input())
    h = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse = True)
    for i in arr:
        s.insert(i,'-')
    result = "".join(s)
    print(f"#{tc} {result}")
    
    
        
    