#이진 탐색 소스코드 구현 (반복문)

def binary_search(array, target, start, end):
    while( start <=end):
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid +1
        else:
            end = mid -1
            


