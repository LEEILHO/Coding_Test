""" 공유기 설치
도현이의 집 N개가 수직선 위에 있다
언제 어디서나 와이파이를 즐기기 위해 공유기 C개 설치
한 집에는 공유기를 하나만 설치 가장 인접한 두 공유기 사이의 거리를 가능한 크게하여 설치
C개의 공유기를 적당히 설치하여 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
첫째 줄 집의개수 2<= N <= 200,000 공유기 개수 2<=C<=N 
둘째 줄 집의 좌표"""

n,c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

start =1
end = arr[-1]-arr[0]
result =0

while(start<=end):
    mid = (start+end)//2
    value = arr[0]
    cnt =1
    for i in range(1,n):
        if arr[i] >=value+mid:
            value = arr[i]
            cnt +=1
    if cnt >=c:
        start = mid+1
        result = mid
    else:
        end = mid -1
print(result)