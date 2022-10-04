""" 1이 될 때까지
 어떠한 수 N이 1이 될 떄까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하고자 한다.
 단 두 번째 연산은 N이 K로 나누어 떨어질떄만 선택할 수 있다.
 1. N에서 1을 뺀다
 2. N을 K로 나눈다.
 첫째 줄 2이상 100000이하인 n,k 가 공백으로 구분되며 각각 자연수로 주어진다. 이때 n은 항상 K이상이다
"""
n,k = map(int, input().split())
cnt =0
while(n!=1):
    if (n//k)== n/k:
        n /=k
        cnt +=1
    else:
        n -=1
        cnt +=1
print(cnt)