#무한사전

T = int(input())
for test_case in range(1,T+1):
    P = input().rstrip()
    Q = input().rstrip()
    result ="Y"
    P_length = len(P)
    Q_length = len(Q)
    cnt = 0
    while( cnt <P_length):
        if P[cnt] <Q[cnt]:
            result = "Y"
            break
        elif P[cnt] == Q[cnt]:
            cnt +=1
    if cnt ==P_length and P_length<Q_length:
        for i in range(cnt,Q_length):
            if Q[i] !='a':
                result = "Y"
                break
            else:
                result = "N"
    print("#{} {}".format(test_case,result))
    