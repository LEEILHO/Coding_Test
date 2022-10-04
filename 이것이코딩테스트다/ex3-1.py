    """
    예제 3-1 거스름돈 그리디
    거스름돈으로 500원 100원, 50원 10원이 무한히 존재할 떄 손님에게 거슬러 줘야 할 돈 N원을 거슬러 줄수 있는 동전의 최소 개수 구하라.
    """
N = int(input())
coins = [500,100,50,10]
count =0
for i in coins:
    count += N//i
    N -= (N//i)*i
    
print(count)

