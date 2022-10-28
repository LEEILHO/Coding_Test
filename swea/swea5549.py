# 홀수일까 짝수일까
T = int(input())
for tc in range(1,T+1):
    n = input()
    last = int(n[-1])
    if last % 2 ==1:
        print(f"#{tc} Odd")
    else:
        print(f"#{tc} Even")
        
    