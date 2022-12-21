maxValue =0
i_idx =0
j_idx =0
arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if maxValue < arr[i][j]:
            maxValue=arr[i][j] 
            i_idx = i
            j_idx = j
print(maxValue)
print(i_idx+1, j_idx+1)