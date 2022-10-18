# 오목판정
T = int(input())


for tc in range(1,T+1):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(input()))

   
    # 우,아래,아래_우대각선, 아래_좌 대각선 
    dx = [0,1,1,1]
    dy = [1,0,1,-1]
    result ="NO"
    
    
    for x in range(n):
        for y in range(n):
            if board[x][y] =='o':
                
                for i in range(4):
                    cnt =1
                    nx = x + dx[i]
                    ny = y + dy[i]
                    while nx <n and ny<n and nx >= 0 and ny >=0 and board[nx][ny] =='o':
                        cnt +=1
                        nx += dx[i]
                        ny += dy[i]
                        if cnt >=5:
                            result = "YES"
                            break
                
            if result =="YES":
                break
        if result =="YES":
            break
    print("#{} {}".format(tc,result))  
                            
                        
                         
    
    
                    
                    
        