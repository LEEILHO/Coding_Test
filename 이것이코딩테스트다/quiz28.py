""" 고정점 찾기
고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
예를 들어 a[2] =2 이면 고정점은 2
하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있음
이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성 고정점은 최대 1개만 존재
만약 고정점이 없다면 -1 출력
시간 복잡도는 O(logN)으로 설계

"""
N = int(input())
arr = list(map(int, input().split()))

def find(arr,left,right):
    if left> right:
        return None
    mid = (left+right)//2
    if arr[mid] ==mid:
        return mid
    elif arr[mid] < mid:
        return find(arr,mid+1,right) 
    else:
        return  find(arr,left,mid-1)

fixed = find(arr,0,N-1)
if fixed ==None:
    result = -1
else:
    result = fixed
print(result)