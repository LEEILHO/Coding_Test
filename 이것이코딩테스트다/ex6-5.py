"""
위에서 아래로
하나의 수열에는 다양한 수가 존재 크기에 상관없이 나열 되어있다. 큰수부터 작은 수의 순서로 정렬 수열을 내림차순으로 정렬하는 포로 그램을 만드시오
입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력 동일한 수의 순서는 자유롭게 출력
"""
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
arr.reverse()
# arr = sorted(arr, reversed = True) 로도 출력가능
for i in arr:
    print(i , end = " ")
    