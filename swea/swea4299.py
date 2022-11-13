#태현이의 사랑은 타이밍
T = int(input())
for tc in range(1,T+1):
    D,H,M = map(int,input().split())
    
    appointment_time = (11*24+11)*60 +11
    now_time = (D*24 + H)*60 + M
    result =0
    if appointment_time > now_time:
        result =-1
    else:
        result =now_time-appointment_time
    print(f"#{tc} {result}")
        
    