"""연산자 끼워 넣기
N개의 수로 이루어진 수열이 주어진다. 수와 수 사이에 끼어 넣을 수 있는 N-1개의 연산자가 주어진다.
수와 수 사이에 연산자를 하나씩 넣어서 수식을 하나씩 만들 수 있고 이떄 주어진 수의 순서를 바꾸면 안된다.
식의 계산은 연산자 우선순위를 무시하고 앞엑서 부터 진행해야한다. 나눗셈은 정수 나눗셈으로 몫만 취한다.
첫째 줄에 수의 개수 (2<=N<=11)이 주어진다.
둘째 줄에는 수가 주어진다. 1<=A<=100
셋째줄에는 합이 N-1인 4개의 정수가 주어지는데 차례대로 덧셈의 개수 뺄셈의 개수 곱셈의 개수 나눗셈의 개수이다.
첫째줄에 만들 수 있는 식 결과의 최대값 둘째줄에 최솟값 출력

"""
n = int(input())
arr = list(map(int,input().split()))
ad,su,mu,di = map(int,input().split())
min_value = -1e9
max_value = 1e9

def dfs(i, now):
    global min_value,max_value,ad,su,mu,di
    if i ==n:
        min_value = min(min_value,now)
        max_value = max(max_value,now)
    else:
        
        if ad>0:
            ad -=1
            dfs(i+1,now+arr[i])
            ad+=1
        
        if su>0:
            su -=1
            dfs(i+1,now-arr[i])
            su +=1
        if mu >0:
            mu -=1
            dfs(i+1,now*arr[i])
            mu+=1
        if di >0:
            di -=1
            dfs(i+1, int(now/arr[i]))
            di +=1

dfs(1,arr[0])

print(max_value)
print(min_value)