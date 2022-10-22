t = int(input())

for tc in range(1, t+1):
    command = input()
    N = int(command.split(' ')[0])  # 누를 버튼의 개수
    command = command.split(' ')[1:]    # 누를 버튼의 순서 저장
    pos = [1,1] #블루와 오렌지의 위치
    B = []
    O = []      # 블루와 오렌지가 눌러야 하는 버튼 저장

    for i in range(len(command)):
        if command[i] == 'B':
            B.append(int(command[i+1])) # 블루 버튼 저장
        elif command[i] == 'O':
            O.append(int(command[i+1])) # 오렌지 버튼 저장

    time = 0    # 시간
    while command:  # command 리스트안 요소가 없어질 때까지 반복
        if command[0] == 'B':   # 누를 버튼이 블루라면
            if pos[0] < int(command[1]):
                pos[0] += 1
            elif pos[0] > int(command[1]):
                pos[0] -= 1                 # 버튼 위치까지 이동
            elif pos[0] == int(command[1]):
                command.pop(0)
                command.pop(0)
                B.pop(0)            #버튼 위치까지 이동했다면 버튼을 누르고 리스트에서 삭제

            if len(O) != 0:         #블루가 이동하는 중 오렌지도 버튼을 누르기 위해 이동해야 한다면
                if pos[1] < O[0]:
                    pos[1] += 1
                elif pos[1] > O[0]:
                    pos[1] -= 1
                else:
                    pass            # 오렌지도 이동(버튼을 누르진 않음)

        elif command[0] == 'O':     # 누를 버튼이 오렌지
            if pos[1] < int(command[1]):
                pos[1] += 1
            elif pos[1] > int(command[1]):
                pos[1] -= 1
            elif pos[1] == int(command[1]):
                command.pop(0)
                command.pop(0)
                O.pop(0)            #블루와 마찬가지로 이동 후 버튼을 누름, 리스트 요소 삭제

            if len(B) != 0:     #오렌지가 버튼을 누르는 과정에서 블루도 누를 버튼이 있다면 이동
                if pos[0] < B[0]:
                    pos[0] += 1
                elif pos[0] > B[0]:
                    pos[0] -= 1
                else:
                    pass

        time += 1

    print(f"#{tc} {time}")