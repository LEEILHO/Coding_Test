#테네스의 특별한 소수
import math
N = 10 **6
prime = [True] * (N +1)
for i in range(2,int(math.sqrt(N)) +1):
    prime[0] =prime[1]= False
    if prime[i] == True: 
        j =2
        while i * j <=N:
            prime[i*j] = False
            j +=1
            

T = int(input())
for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    answer = []
    for i in range(A, B+1):
        if str(D) in str(i) and prime[i]== True:
            answer.append(i)
    print(f"#{tc} {len(answer)}")