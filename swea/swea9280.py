#진용이네 주차타워
#주차요금 차량의무게 x 단위 무게당 금액
from collections import deque
T = int(input())
def check_place(parking_place):
        for i in range(1,len(parking_place)):
            if parking_place[i] ==0:
                return True
        return False
for tc in range(1,T+1):
    n,m = map(int,input().split())
    weight_fee =[0] *(n+1)
    car_weight = [0] *(m+1)
    parking_place = [0]*(n+1)
    waiting = deque()
    total_fee =0
    
    for i in range(1,n+1):
        weight_fee[i] =int(input())
    for i in range(1,m+1):
        car_weight[i] = int(input())
    for _ in range(2*m):
        a = int(input())
        #차가 들어올 때
        if a>0:
            #비어있는 주차장소가 있다면
            if check_place(parking_place) == True:
                for i in range(1,n+1):
                    if parking_place[i] ==0:
                        parking_place[i] = a
                        break
            #비어있는 주자장소 없다면 대기
            else:
                waiting.append(a)
        #차가 나감            
        else:
            a= abs(a)
            idx = parking_place.index(a)
            parking_place[idx] =0
            total_fee += car_weight[a] * weight_fee[idx]
            #차가 나갔을 때 기다리고 있는 차량 존재하면
            if waiting:
                a = waiting.popleft()
                parking_place[idx] = a
    print(f"#{tc} {total_fee}")
            
            
                        
        
            
        
                