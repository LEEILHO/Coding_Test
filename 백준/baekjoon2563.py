N = int(input())
arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
    l,b = map(int, input().split())
    for i in range(99-b,99-b-10,-1):
        for j in range(l,l+10):
            arr[i][j] =1
result =0
for i in arr:
    result += sum(i)
        
print(result)

