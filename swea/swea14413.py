T = int(input())

for test_case in range(1, T + 1):
   
    N,M = map(int, input().split())
    arr = [list(input()) for _ in range(N)] #2차원 배열 선언
    result = [0,0,0,0] # #index값의합:짝수,홀수,index값의 합:짝수,홀수 
    for col in range(N):
        for row in range(M):
            if arr[col][row] =='#':
                if (col+row)%2 ==0: #
                    result[0] = 1
                else:
                    result[1] =1
            if arr[col][row] =='.':
                if (col+row)%2 ==0:
                    result[2] = 1
                else:
                    result[3] =1
    if (result[0] ==1 and result[1] ==1) or (result[2] ==1 and result[3] ==1) or (result[0] ==1 and result[2] ==1) or (result[1] ==1 and result[3] ==1):
        print("#{0} impossible" .format(test_case))
    else:
        print("#{0} possible" .format(test_case))
        

