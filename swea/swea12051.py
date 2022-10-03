#swea12051 프리셀
T = int(input())

for test_case in range(1, T + 1):
    N,PD, PG = map(int,input().split())
    result = "Broken"

    #pd 확률이 0이 아닌데 PG확률이 0일경우
    if (PD !=0 and PG ==0):
        result = "Broken"
    # pd 확률이 100이 아닌데 PG 확률이 100일 경우
    elif(PD !=100 and PG ==100):
        result = "Broken"        
    else:
        for d in range(1,N+1):
            if  (PD*d)/100  ==(PD*d)//100 : # PD와 D를 곱해서 정수가 나온다면 가능한 경우의 수
                result = "Possible"
                break
            
    print("#{} {}".format(test_case,result))

    
                    
                    
            
            
