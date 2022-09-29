import copy
T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input()))
    max_value= copy.deepcopy(arr)# 리스트 복사
    min_value = copy.deepcopy(arr)# 리스트 복사
    if len(arr)>1: # 길이가 2 이상부터
        for i in range(len(max_value)):
            max_idx = i
            for j in range(i+1,len(max_value)):
                if max_value[j] >= max_value[max_idx]: #현재값과 최대값과 비교하여 현재값이 크거나 같다면 현재 인덱스를 최대 인덱스로 설정
                    max_idx = j
            if max_value[max_idx] > max_value[i]:# 현재값을 최대값과 비교하여 최대값보다 크면 값을 서로 바꿈
                max_value[max_idx],max_value[i] = max_value[i],max_value[max_idx]
                break
        for i in range(len(min_value)):
            min_idx = i
            for j in range(i+1,len(min_value)):
                if i==0:# 현재 값이 첫번째 요소이면
                    if min_value[j] <=min_value[min_idx] and min_value[j] !=0: #현재값이 0이 아니고 최소값이면 인덱스 저장
                        min_idx = j
                else:
                    if min_value[j] <= min_value[min_idx]:#현재값이 최소값이면 인덱스 저장
                        min_idx = j
            if min_value[min_idx] < min_value[i]: #현재값을 최소값과 비교하여 작으면 값을 서로 바꿈
                min_value[min_idx], min_value[i] = min_value[i],min_value[min_idx]
                break
            
            
    max_value = int("".join(map(str,max_value)))
    min_value = int("".join(map(str,min_value)))
    print("#{} {} {}".format(test_case, min_value,max_value))
               
                   
        
    