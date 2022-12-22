import sys
N = int(input())
arr=[]
for _ in range(N):
    # arr.append(int(input())) 이렇게 입력 받으면 시간초과
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)
for i in arr:
    print(i)