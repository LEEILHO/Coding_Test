def command_U(tank_x,tank_y):
    if tank_x - 1 >=0:
        if board[tank_x-1][tank_y] ==".":
            board[tank_x][tank_y] = "."
            board[tank_x-1][tank_y] ="^"
            return tank_x-1,tank_y
        else:
            board[tank_x][tank_y] ="^"
            return tank_x,tank_y
    else:
            board[tank_x][tank_y] ="^"
            return tank_x,tank_y
    
    
def command_D(tank_x,tank_y):
    if tank_x +1 <H:
        if board[tank_x+1][tank_y] ==".":
            board[tank_x][tank_y] = "."
            board[tank_x+1][tank_y] ="v"
            return tank_x+1,tank_y
        else:
            board[tank_x][tank_y] = "v"
            return tank_x,tank_y
    else:
            board[tank_x][tank_y] = "v"
            return tank_x,tank_y

def command_L(tank_x,tank_y):
    if tank_y-1 >=0:
        if board[tank_x][tank_y-1]  ==".":
            board[tank_x][tank_y] ="."
            board[tank_x][tank_y-1] ="<"
            return(tank_x,tank_y-1)
        else:
            board[tank_x][tank_y] = "<"
            return tank_x,tank_y
    else:
            board[tank_x][tank_y] = "<"
            return tank_x,tank_y
    
    
def command_R(tank_x,tank_y):
    if tank_y + 1 < W:
        if board[tank_x][tank_y+1] == ".":
            board[tank_x][tank_y] ="."
            board[tank_x][tank_y+1] =">"
            return tank_x,tank_y+1
        else:
            board[tank_x][tank_y] = ">"
            return tank_x,tank_y
    else:
            board[tank_x][tank_y] = ">"
            return tank_x,tank_y
    
    
def command_S(tank_x,tank_y):
    if board[tank_x][tank_y] =="^":
        while(tank_x >0):
            tank_x-=1
            if board[tank_x][tank_y] =="*":
                board[tank_x][tank_y] ="."
                break
            elif board[tank_x][tank_y] =="#":
                break
            
    elif board[tank_x][tank_y] =="v":
        while(tank_x <H-1):
            tank_x+=1
            if board[tank_x][tank_y] =="*":
                board[tank_x][tank_y] ="."
                break
            elif board[tank_x][tank_y] =="#":
                break
                
    elif board[tank_x][tank_y] =="<":
        while (tank_y >0):
            tank_y-=1
            if board[tank_x][tank_y] =="*":
                board[tank_x][tank_y] ="."
                break
            elif board[tank_x][tank_y] =="#":
                break
            
    else:
        while (tank_y <W-1):
            tank_y+=1
            if board[tank_x][tank_y] =="*":
                board[tank_x][tank_y] ="."
                break
            elif board[tank_x][tank_y] =="#":
                break
            
        
    
T = int(input())
for tc in range(1,T+1):
    H,W = map(int, input().split())
    board=[]
    for _ in range(H):
        board.append(list(input()))
    N = int(input())
    tank_x,tank_y, =0,0
    
    for i in range(H):
        for j in range(W):
            if board[i][j] =="<":
                tank_direction = "<"
                tank_x, tank_y = i,j
            if board[i][j] ==">":
                tank_direction = ">"
                tank_x, tank_y = i,j
            if board[i][j] =="^":
                tank_direction = "^"
                tank_x, tank_y = i,j
            if board[i][j] =="v":
                tank_direction = "v"
                tank_x, tank_y = i,j
                
        
    command = input()
    for i in command:
        if i =='S':
            command_S(tank_x,tank_y)
        
        else:
            if i=='U':
                tank_x,tank_y = command_U(tank_x,tank_y)
            elif i =="D":
                tank_x,tank_y = command_D(tank_x,tank_y)
            elif i =="L":
                tank_x,tank_y = command_L(tank_x,tank_y)
            else:
                tank_x,tank_y = command_R(tank_x,tank_y)
    print(f"#{tc}", end =' ')
    for i in range(H):
        print("".join(board[i]))
