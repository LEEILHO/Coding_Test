

for tc in range(1,11):
    l = int(input())
    board = []
    for _ in range(8):
        board.append(list(input()))
    cnt =0
    for i in range(8):
        for j in range(8):
            #오른쪽 확인
            if (j+(l-1)<=7):
                word = "".join(board[i][j:j+l])
                # print("오",word)
                if word == word[::-1]:
                    cnt +=1
                
            # #왼쪽 확인
            # if (j-(l-1)>-1):
            #     word = "".join(board[i][j-(l-1):j+1])
            #     # print("왼",word)
            #     if word == word[::-1]:
            #         cnt +=1
                
            # #위쪽 확인
            # if (i-(l-1)>-1):
            #     word =""
            #     for x in range(i-(l-1),i+1):
            #         word +=board[x][j]             
            #     # print("위",word)
            #     if word == word[::-1]:
            #         cnt +=1
            
            
            #아래쪽 확인
            if (i+(l-1)<=7):
                word =""
                for x in range(i,i+l):
                    word +=board[x][j]

                # print("아",word)
                if word == word[::-1]:
                    cnt +=1
    print(f"#{tc} {cnt}")
            
