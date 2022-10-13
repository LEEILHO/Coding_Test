# swea 13038 교환학생


T = int(input())

for test_case in range(1, T + 1):
    n= int(input())
    arr = list(map(int,input().split()))
    start_list = []
    answer = 1e9
    for i in range(len(arr)):
        if arr[i] ==1:
            start_list.append(i)
    for i in start_list:
        day_cnt =0
        class_cnt =0
        while class_cnt < n:
            if arr[i] ==1:
                class_cnt +=1
            day_cnt +=1
            i +=1
            if i==7:
                i =0
        answer = min(answer,day_cnt)
    print(f'#{test_case} {answer} ')
        