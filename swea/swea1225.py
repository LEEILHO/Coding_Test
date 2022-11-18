for _ in range(1,11):
    tc = int(input())
    arr = list(map(int, input().split()))
    ck = True
    while(ck):
        for i in range(1,6):
            if arr[0]-i >0:
                arr[0]  -= i
                arr = arr[1:] + arr[:1]
            else:
                arr[0] = 0
                arr =arr[1:] + arr[:1]
                ck = False    
                break
    print("#{} {} {} {} {} {} {} {} {}".format(tc, *arr))    