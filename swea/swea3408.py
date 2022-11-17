T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S1 =  (N)*(N+1)//2
    #짝수일 때
    if N % 2 == 0:
        S2 = (2*N) * (N//2)
        S3 = (2*N+2) * (N//2)
    #홀수 일 때
    else:
        if N ==1:
            S2 = 1
            S3 = 2
        else:    
            S2 = (2*N) * (N//2)  +  N
            S3= (2*N+2)*(N//2) + N+1
    print("#{} {} {} {}".format(tc, S1, S2,S3))