T = int(input())
for tc in range(1,T+1):
    S = input()
    SC = []
    DC =[]
    HC =[]
    CC=[]
    result=""
    for i in range(0,len(S),3):
        if S[i] =="S":
            if S[i:i+3] in SC:
                result ="ERROR"
                break
            else:
                SC.append(S[i:i+3]) 
        elif S[i] =="D":
            if S[i:i+3] in DC:
                result ="ERROR"
                break
            else:
                DC.append(S[i:i+3]) 
        elif S[i] =="H":
            if S[i:i+3] in HC:
                result ="ERROR"
                break
            else:
                HC.append(S[i:i+3]) 
        else:
            if S[i:i+3] in CC:
                result ="ERROR"
                break
            else:
                CC.append(S[i:i+3]) 
                
    
    if result =="":
        SC_need =13-len(SC)
        DC_need= 13-len(DC)
        HC_need=13-len(HC)
        CC_need=13-len(CC)
        print("#{} {} {} {} {}".format(tc,SC_need,DC_need,HC_need,CC_need)) 
    else:
        print(f"#{tc} {result}")