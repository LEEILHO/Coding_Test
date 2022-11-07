#다솔이의 다이아몬드 장식
T = int(input())
for tc in range(1,T+1):
    S = input()
    N = len(S)
    
    length = (N-1) * 3 + 4 + N
    arr = [["."] * length for _ in range(5)]
    for i in range(len(arr)):
        if i ==0 or i ==4:
            for j in range(2,length,4):
                arr[i][j] = "#"
        elif i ==1 or i ==3:
            for j in range(1,length,2):
                arr[i][j] = "#"
        else:
            for j in range(0,length,4):
                arr[i][j] = "#"
            cnt =0
            for j in range(2,length,4):
                arr[i][j] = S[cnt]
                cnt +=1
    for i in arr:
        print("".join(i))
        
            
         