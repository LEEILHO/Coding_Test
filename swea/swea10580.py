#전봇대
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    wire = []
    result =0
    for _ in range(n):
        x,y = map(int,input().split())
        
        for i in range(len(wire)):
            if (wire[i][0]<x and wire[i][1]>y) or (wire[i][0]>x and wire[i][1]<y):
                result +=1
        wire.append((x,y))
    print(f"#{tc} {result}")    
    