# 체스판 위의 룩 배치
def check(board):
    cnt =0
    rook_x =[]
    rook_y =[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] =="O":
                if i in rook_x or j in rook_y:
                    return "no"
                else:
                    rook_x.append(i)
                    rook_y.append(j)
                    cnt+=1
    if cnt ==8:
        return "yes"
    else:
        return "no"
                
    
T = int(input())
for tc in range(1,T+1):
    board =[]
    for _ in range(8):
        board.append(list(input()))
    result = check(board)
    print(f"#{tc} {result}" )
        
        
        