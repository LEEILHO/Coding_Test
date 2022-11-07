# 두가지 빵의 딜레마

T = int(input())
for tc in range(1, T+1):
    A,B,C = map(int, input().split())
    result = 0
    if A<B:
        result = C//A
    else:
        result = C//B
    print(f"#{tc} {result}")
        