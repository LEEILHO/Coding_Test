#항구에 들어오는 배
#큰 수가 들어오면 에러가 나는 코드
# def check_ship(d,funny_day):
#     for i in range(1,len(funny_day),d):
#         if funny_day[i] ==0:
#             return False
#     return True
    
# def check_clear(funny_day):
#     if funny_day.count(1)==0:
#         return True
#     else:
#         return False
    
    
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     day =[]
#     for _ in range(N):
#         day.append(int(input()))
#     last_day = day[-1]
#     funny_day = [0] * (last_day +1)
#     for i in day:
#         funny_day[i] = 1
#     ships =0
#     for i in range(1,last_day+1):
#         if check_ship(i,funny_day) ==True:
#             ships+=1
#             for d in range(1,len(funny_day),i):
#                 funny_day[d] +=1
#             if check_clear(funny_day) ==True:
#                 break
#     print(f"#{tc} {ships}")
            
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    day =[]
    for _ in range(N):
        day.append(int(input()))        
    result =0
    ships =set()
    for i in range(1,len(day)):
        if day[i] in ships:
            continue
        gap = day[i] -1
        for j in range(1+gap,day[-1]+1,gap):
            ships.add(j)
        result +=1
    print(f"#{tc} {result}")
        
        
 