""" 무지의 먹방 라이브
회전판에 먹어야 할 음식 N개, 각음시에는 1부터 n까지 번호가 붙어 있으며, 각 음식을 섭취하는데 일정 시간이 소요.
1. 1번부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 온다.
2. 마지막 번호의 음식을 섭취한 다음에는 다시 1번음식이 앞으로 온다.
3. 음식 하나를 1초 동안 섭취 후 남은 음식은 그대로 두고 다음 음식이 섭취 남은 음식중 가장 가까운 번호의 음식
4. 회전판이 다음음식을 무지앞으로 가져오는데 걸리는 시간이 없다 가정
먹방 시작한 후 K초 후 네트워크 장애로 방송 중단
음식을 모두 먹는데 필요한 시간이 담겨있는 배열 foodtimes,네트워크 장애가 발생한 시간 k초 
몇번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수 완성
"""
# def solution(food_time,k):
#     turn = 0
#     for i in range(k):
        
#         while(food_time[turn] ==0):
#             turn +=1
#             if turn == len(food_time):
#                 turn =0

#         if food_time[turn] !=0:
#             food_time[turn] -=1
#             turn +=1
#             if turn == len(food_time):
#                 turn =0
#         print(food_time)
#     if food_time[turn] ==0:
#         result = -1
#     else:
#         result = turn +1
#     return result
import heapq
def solution(food_times,k):
    if sum(food_times) < k:
        return -1
    q =[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    sum_value =0 #먹기위해 사용한 시간
    previous = 0 #직전에 다먹은 음식 시간
    length = len(food_times)
    while sum_value + ((q[0][0] -previous) * length) <=k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -=1
        previous = now

    result = sorted(q, key = lambda x: x[1])
    return result[(k-sum_value) %length][1]
food_times = [3,1,2]
k = 5
print(solution(food_times,k))