"""
카드 정렬하기
정렬된 두 묶음의 숫자 카드가 존재 A,B라 하면 두 묶음을 합쳐서 하나로 만드는데 (A+B)번의 비교
N개의 숫자 카드 묶음의 크기가 각각 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성"""

import heapq 
N = int(input())
cards=[]
for _ in range(N):
    cards.append(int(input()))
heapq.heapify(cards)
print(cards)
result =0
while (len(cards) !=1):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    result += x+y
    heapq.heappush(cards,x+y)
   
    

print(result)

