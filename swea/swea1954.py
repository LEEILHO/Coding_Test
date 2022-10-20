#달팽이 숫자
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    dx =[0,1,0,-1]
    dy=[1,0,-1,0]
    d =0
    x=0
    y=0
    graph[0][0]=1
    for i in range(2,n**2 +1):
        nx = x+ dx[d]
        ny = y+dy[d]
        if nx<0 or nx>=n or ny<0 or ny>=n or graph[nx][ny]!=0:
            d +=1
            if d==4:
                d=0
            nx = x + dx[d]
            ny = y + dy[d]    
        graph[nx][ny] =i
        x= nx
        y = ny
    print(f"#{tc}")
    for i in range(n):
        for j in range(n):
            print(graph[i][j],end =" ")
        print()