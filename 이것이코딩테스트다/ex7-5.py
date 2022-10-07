""" 떡볶이 떡의 길이가 일정하지 않음 한 봉지 안에 들어있는 떡의 총길이는 절단기로 맞춰준다
절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단한다. 낮은떡은 잘리지 않음 
ex 19,14,10,17 인 떡이 나란히 있고 높이 15로 지정하면 4, 0, 0, 2 이므로 6만큼의 길이를 가져간다
손님이 왔을때 요청한 길이가 M일때 적어도 M만큼 떡을 얻기위해 절단기에 설정할수 있는 높이의 최댓값은?
첫째줄 n m
둘째줄 개별 높이
"""
n,m = map(int, input().split())
arr = list(map(int,input().split()))
start =0
end = max(arr)
#end값을 가장 큰  떡 길이로 설정 
result = 0
#이진 탐색 반복문 이용
while(start <= end):
    total = 0 #남는 떡의 총합
    # 중간은 가장 큰 값과 작은 값이 중간값
    mid = (start+end)//2
    for x in arr:
        if x > mid:
            total += x-mid
    
    if total < m: # 떡의 총합이 m 보다 작으면 end 변경 
        end = mid - 1
    else: # 떡의 총합이 m이상일때
        result = mid
        start = mid +1


print(result)

        
