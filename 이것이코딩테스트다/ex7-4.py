"""부품 찾기
전자 매장에는 부품이 N개 있다. 정수 형태의 고유한 번호가 있다.
M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
M개 종류를 모두 확인해서 견적서를 작성해야한다.
가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성
손님이 요청한 부품이 순서대로 부품을 확인해 있으면 yes 없으면 no 출력
첫째 줄 정수 M
둘재쭐 공백구분 하여 n개의 정수
정수 M
넷째 줄 공백 구분 M개의 정수
"""

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()
def binary_search(array,target,start,end):
    while(start<=end):
        mid = (start+end)//2
        if array[mid] ==target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
            
    return None
        
        
    
    
    
for i in arr2:
    if (binary_search(arr1,i,0,n-1) !=None):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
    
    