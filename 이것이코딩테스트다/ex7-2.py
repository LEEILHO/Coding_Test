# 재귀 함수로 구현한 이진 탐색 소스 코드
def binary_search(array, target,start ,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        binary_search(array,target,start,mid-1)
        
    else:
        binary_search(array,target,mid +1, end)
        
        