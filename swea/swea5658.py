# 보물상자 비밀번호
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo

def to_dex(s):
    num =0
    for i in range(len(s)):
        
        if s[i] =="A":
            num += (16**i) *10
        elif s[i] =="B":
            num += (16**i) *11
        elif s[i] =="C":
                num += (16**i) *12
        elif s[i] =="D":
            num += (16**i) *13
        elif s[i] =="E":
            num += (16**i) *14
        elif s[i]=="F":
            num += (16**i) *15
        else:
            num += (16**i) * int(s[i])
    return num
    

T = int(input())
for tc in range(1,T+1):
    n,k = map(int,input().split())
    nums = list(input())
    width = n//4
    result = []
    for i in range(width):
        temp = nums[1]
        for j in range(n-1):
            temp = nums[j+1]
            nums[j+1] = nums[0]
            nums[0] = temp        
        first = nums[0:width]
        second =nums[width:2*width]
        third = nums[2*width:3*width]
        fourth =nums[3*width:4*width]
        result.append(to_dex(first[::-1]))
        result.append(to_dex(second[::-1]))
        result.append(to_dex(third[::-1]))
        result.append(to_dex(fourth[::-1]))
    result = set(result)
    result =sorted(result, reverse = True)
    answer =result[k-1]
        
    
            
        
        
    
    print(f"#{tc} {answer}")



    