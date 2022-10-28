# 의석이의 세로로 말해요
T = int(input())
for tc in range(1, T+1):
    result =''
    arr = [list(input()) for _ in range(5)]
    max_length = 0
    for i in arr:
        if len(i) > max_length:
            max_length = len(i)
    
    for i in range(max_length):
        for j in range(5):
            if i < len(arr[j]):
                result +=arr[j][i]
            else:
                continue
    print(f"#{tc} {result}")   