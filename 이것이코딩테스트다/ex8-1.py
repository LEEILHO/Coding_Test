#피보나치 재귀 함수

def fibo(x):
    if x ==1 or x==2:
        return 1
    return fibo(x-1)+ fibo(x-2)
print(fibo(4))

# 피보나치 재귀함수 이용 탑다운방식

d = [0] *100

def fibo2(x):
    if x==1 or x==2:
        return 1
    if d[x] !=0:
        return d[x]
    d[x] = fibo2(x-1) + fibo2(x-2)
    return d[x]
print(fibo2(99))

#피보나치 반목문 이용 바텀업방식

a=[0] *100

a[1] =1
a[2] =1
n =99

for i in range(3,n+1):
    a[i] = a[i-1] +a[i-2]
print(a[n])
