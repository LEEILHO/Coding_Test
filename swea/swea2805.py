T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board =[]
    for _ in range(N):
        board.append(list(map(int,input())))
    mid = N//2
    result =0
    for i in range(N):
        if abs(mid-i)==0:
            result +=sum(board[i])
        else:    
            result+=sum(board[i][abs(mid-i):N-abs(mid-i)])
    print(f"#{tc} {result}")