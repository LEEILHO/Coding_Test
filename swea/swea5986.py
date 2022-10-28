# 새샘이와 세 소수
T = int(input())
def is_prime(x):
    for i in range(2,x):
        if x % i ==0:
            return False
    return True
            
for tc in range(1,T+1):
    n = int(input())
    arr = []
    result =0
    for i in range(2,n):
        if is_prime(i) == True:
            arr.append(i)
    
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            for k in range(j,len(arr)):
                if arr[i] + arr[j] +arr[k] ==n:
                    result +=1
    print(f"#{tc} {result}")