# swea.14692 통나무자르기
T = int(input())

for test_case in range(1, T + 1):
    
    N = int(input())
    if (N-1)%2 ==0: #n-1이 짝수이면 Bob승리
        print("#{0} {1}" .format(test_case, "Bob"))
    else:#홀수이면 Alice승리
        print("#{0} {1}" .format(test_case, "Alice"))
     
        
    


