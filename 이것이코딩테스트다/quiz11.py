""" 
뱀
게임에는 뱀이 나와서 기어 다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다.
NxN 정사각 보드 위에서 진행 되고, 몇몇 칸에는 사과가 놓여져있음 보드의 상하좌우 끝에는 벽이 있다. 게임시작할때 뱀은 맨 위 좌측에 위치 길이는 1
뱀은 처음에 오른쪽을 향한다.
규칙:
뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다 
이동한 칸에 사과가 있다면, 칸에 있던 사과과 없어지고 꼬리는 움직이지 않는다.
이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비운다,
사과의 위치와 뱀의 이동경로가 주어질 때 게임이 몇 초에 끝나는지 계산
첫째줄 보드의 크기 2 <= n <=100
다음줄 사과의 개수  0<= K <=100
뱀의 방향 변환 횟수 L 1<= L <=100
다음 L개의 줄에는 뱀의 방향 변환 정보, 정수 X 문자 C 게임시작 시간으로부터 x초가 끝난 뒤에 
왼쪽 C가 "L" 오른쪽 C가 "D" 로 90도 방향을 회전시킨다는 뜻"""
n = int(input())
board= [[0] *(n+1) for _ in range(n+1)]
k = int(input())
for i in range(k):
    x,y = map(int,input().split())
    board[x][y] =1
l = int(input())
direction =[]
for i in range(l):
    data = input().split()
    direction.append((int(data[0]),data[1]))

# 동,남,서,북 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(d,c):
    if c =="L":
        d = (d-1) %4
    else:
        d = (d+1) %4
    return d
def simulate():
    x,y = 1,1
    board[x][y]=2 # 뱀이 존재하는 위치2로 표시 
    d =0 # 첫 방향 동쪽
    time =0 
    index =0
    q= [(x,y)] # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞쪽)
    while True:
        nx = x+ dx[d]
        ny = y+ dy[d]
        #맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1<= nx and nx <=n and 1 <= ny and  ny <= n and board[nx][ny] !=2:
            #사과가 없다면
            if board[nx][ny] ==0:
                board[nx][ny] =2
                q.append((nx,ny))
                #꼬리 삭제
                px, py = q.pop(0)
                board[px][py] =0
            if board[nx][ny] ==1:
                board[nx][ny] =2
                q.append((nx,ny))
        #벽, 몸통 부딛혔다면
        else:
            time +=1
            break
        # 다음 위치로 머리 이동
        x,y = nx,ny
        time +=1
        if index<l and time == direction[index][0]:
            d = turn(d,direction[index][1])
            index +=1
    return time

print(simulate())

    

