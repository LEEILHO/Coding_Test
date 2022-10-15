"""치킨 배달
NxN 도시의 각 칸은 빈칸, 치킨집, 집 중 하나이다.
r은 위에서 부터 r 번째 c는 왼쪽에서 부터 c번째 r과 c 는 1부터 시작
치킨 거리란 집과 가장 가까운 치킨집 사이의 거리 
도시의 치킨 거리는 모든 집의 치킨 거리의 합
도시에 있는 치킨집 중에서 M개를 고르고 나머지 치킨집은 모두 폐업
어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.,
첫째줄 2<= N <=50 1<=m<=13
둘째 줄 도시의 정보
0은 빈칸 1은 집 2는 치킨집 집의 개수는 2N개를 넘지 않으며 적어도 1개는 존재한다.
치킨 집의 개수는 M보다 크거나 같고, 13보다 작거나 같다
"""
from itertools import combinations
n,m = map(int,input().split())
info =[list(map(int,input().split())) for _ in range(n) ]
house = []
chicken = []
distance = []
for i in range(n):
    for j in range(n):
        if info[i][j] ==1:
            house.append((i+1,j+1))
        elif info[i][j] ==2:
            chicken.append((i+1,j+1))

chickens = combinations(chicken,m)
#경우의 수 반복
for i in chickens:
    sum_distance = 0 # 각 경우의 수의 최소 거리합
    for j in house:
        min_dis =1e9 # 집과 치킨집의 최소 거리
        x,y = j
        for k in i:
            dis = abs(x-k[0]) + abs(y-k[1])
            min_dis = min(min_dis,dis)
        sum_distance += min_dis
    distance.append(sum_distance)

print(min(distance))
        
