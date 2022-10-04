"""큰수의 법칙 
    다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수로 만드는 것 단, 특정인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없음/
    첫째 줄에 N(2<=N<=1000) ,M(1<=M<=10000), K(1<=K<=10000) 공백으로 구분하여 주어짐

"""
n,m,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
arr.sort() # 정렬
first = arr[-1] # 최댓값
second = arr[-2] # 두번째로 큰값
cnt = (m //(k+1)) * k 
cnt +=  m % (k+1)

result = cnt * first
sult += (m - cnt) * second
print(result)

