#퀵 정렬 예제


array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>= end: #원소가 1개인 경우 종료
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        
        # 피벗보다  큰 array[left] 데이터를 찾을 떄까지 반복 
        while left <= end and array[left] <= array[pivot]:
            left +=1
        # 피벗보다  작은 array[right] 데이터를 찾을 떄까지 반복
        while right > start and array[pivot] <= array[right]:
            right -=1
            
        # left와 right가 엇갈리는 경우
        if left > right:
            # pivot과  작은 데이터를 바꿈
            array[pivot], array[right] = array[right], array[pivot]  
        # 엇갈리지 않는다면
        else:
            #작은 데이터와 큰 데이터 교체 
            array[left], array[right] = array[right], array[left]
            
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)
    
quick_sort(array,0,len(array)-1)

print(array)








