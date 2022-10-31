""" 정렬된 배열에서 특정 수의 개수 구하기
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
x가 등장하는 횟수를 계산
[1,1,2,2,2,2,3] 있을 때 x =2이면 현재 수열에서 값이 2인 원소가 4개이므로 4 출력
문제는 시간복잡도 O(logN) 으로 알고리즘을 설계 
첫 쨰줄 N과 x
둘째 줄에 N개의 원소가 정수 형태로 구분되어 입력
x인값이 하나도 없으면 -1 출력
"""
n,x = map(int, input().split())
arr = list(map(int, input().split()))
def search_first(arr,x,left,right):
    
    if left > right:
        return None
    mid = (left+right)//2
    if arr[mid] ==x and arr[mid-1]<x:
        return mid
    if arr[mid] >=x:
        return search_first(arr,x,left,mid-1)
    if arr[mid] < x:
        return search_first(arr,x,mid+1,right)


    
    
    
def search_last(arr,x,left,right):
    if left> right:
        return None
    
    mid = (left+right)//2
    if arr[mid] == x and arr[mid+1] > x:
        return mid
    if arr[mid] <= x:
        return search_last(arr,x,mid+1,right)
    if arr[mid] > x:
        return search_last(arr,x,left,mid-1)

first = search_first(arr,x,0,n-1)
last = search_last(arr,x,0,n-1)
if first ==None or last ==None:
    answer = -1
else:
    answer = last-first +1
print(answer)