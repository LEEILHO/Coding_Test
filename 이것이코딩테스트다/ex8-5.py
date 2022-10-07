""" 효율적인 화폐 구성 
N 가지의 종류의 화폐 . 이화폐들의 개수를 최소한으로 이용해서 가치의 합이 M이 되도록 하려고 한다. 각 화폐는 몇 개라도 사용할 수 있으며
구성은 같지만 순서가 다른것은 같은 경우로 구분 
첫째줄 n, m 주어짐
그이후 N개의 줄에는 각 화폐의 가치가 주어진다. M원을 만들 수 없다면 -1 출력"""
n, m = map(int, input().split())
coin =[]
for i in range(n):
    coin.append(int(input()))
    
d = [99999] * (m+1)

d[0] =0
#코인의 종류만큼 순회
for i in range(n):
    # 첫 번째 종류의 코인 부터 m+1까지 순회
    for j in range(coin[i],m+1):
        if d[j- coin[i]] != 99999: # 현재의 인덱스에서 화폐단위 만큼 뻇을 때 경우의수가 99999가 아니라면(경우의 수가 존재한다면)
            d[j] = min(d[j], d[j- coin[i]] +1) # 최솟값을 값으로 넣음

if d[m] == 99999:
    print(-1)
else:
    print(d[m])