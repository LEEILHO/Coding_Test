# 파스칼의 삼각형
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] *N for _ in range(N)] #2차원 배열 선언
    for i in range(N):
        for j in range(i+1):
            if j ==0 or j ==i: #삼각형이 왼쪽이나 오른족 끝일떄
                arr[i][j] = 1 #해당위치의 배열에 1 저장
            else:
                arr[i][j] = arr[i-1][j-1] +arr[i-1][j] # 전줄의 자기의 Index값보다 하나작은 index의 저장값과 자기의 Index값의 저장값을 더하여 저장
    print("#{}".format(test_case))
    for lst in arr:
        result = [x for x in lst if x]
        print(*result)