
for _ in range(1,11):
    tc = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
    left_top = 0
    right_top =0
    width_sum =[0] * 100
    height_sum = [0] * 100
    for i in range(100):
        for j in range(100):
            width_sum[i] += arr[i][j]
            height_sum[j] += arr[i][j]
            if i==j:
                left_top += arr[i][j]
            if i+j ==99:
                right_top += arr[i][j]
    max_width = max(width_sum)
    max_height = max(height_sum)
    result = max(max_height,max_width,left_top,right_top)
    print(f"#{tc} {result}")