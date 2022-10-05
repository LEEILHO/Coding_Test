""" 게임 개발
 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다. N X M 크기의 직사각형 각각의 칸은 육지 또는 바다
 케릭터는 동서남북 중 한 곳을 바라본다 (A,B) A는 북쪽으로 떨어진 칸의 개수 B 서쪽으로 떨어진 칸의 개수 
 캐릭터는 상하좌우로 움직일수 있고 바다는 갈 수 없다.
 메뉴얼 1. 현재 위치에서 현재 방향을 기준 왼쪽 부터 차례대로 갈곳을 정한다
 2. 케릭터 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면 왼쪽방향으로 회전 왼쪽으로 한 칸을 전진 없다면 회전만 수행 1단계로 돌아감
 3. 네방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는 바라보는 방향을 유지한 채로 한 칸 뒤로가고 1단계로 돌아감 이 때 뒤쪽방향이 바다이년 움직임을 멈춘다.
 캐틱터가 방문한 칸의 수를 출력하는 프로그램
3<=N,M<=50
케릭터가 있는 좌표 방향 d d =0 북쪽,1 동쪽, 2남쪽, 3 서쪽
3째 줄 0 육지 1 바다
"""
n, m = map(int,input().split())
x,y,d = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(arr)
arr[x][y] =2 #현재 위치 갔다온 의미 2
#북서남동
dx = [-1,0,1,0]
dy = [0,-1,0,1]
count = 1
turn_time =0

def turn_left():
    global d
    d = (d+1) % 4

while True:
    turn_left()
    nx = x+ dx[d]
    ny = y +dy[d]
    if arr[nx][ny] ==0:
        arr[nx][ny] =2
        x = nx
        y = ny
        count +=1
        turn_time = 0
        continue
    else:
        turn_time +=1
    
    if turn_time ==4:
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny] ==2:
            x = nx
            y = ny
        elif arr[nx][ny] ==1:
            break
        turn_time =0




print(arr)
print(count)
    


