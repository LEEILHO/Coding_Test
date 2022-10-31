""" 감시 피하기
N X N 크기의 복도 칸의 특정위치에는 선생님,학생, 장애물 존재 
학생 몇 명이 수업 시간에 몰래 복도에 나왔는데 복도에 나온 학생들이 선생님의 감시에 들키지 않는 것이 목표
각 선생님은 자신의 위치에서 상,하,좌,우  방향으로 감시 단, 복도에 장애물이 있으면 장애물 뒷편으로는 볼 수 없다.
학생들은 복도의 빈칸 중에서 장애물을 설치할 위치를 골라 정확히 3개의 장애물을 설치해야한다.
첫째 줄에 자연수 3<= N <= 6
둘째 줄에 N개의 줄에 걸쳐서 복도의 정보가 주어진다,
모두 감시를 피할 수 있으면 YES 아니면 NO 출력
"""

from itertools import combinations


n= int(input())
board =[]
teachers=[]
spaces=[]
for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] =="T":
            teachers.append((i,j))
        if board[i][j] == "X":
            spaces.append((i,j))
#확인하는 함수
def watch(x,y,direction):
    #왼쪽 확인
    if direction ==0:
        while (y>=0):
            if board[x][y] =="S":
                return True
            if board[x][y] =="O":
                return False
            y -=1
    # 오른쪽 화인    
    if direction ==1:
        while (y<n):
            if board[x][y] =="S":
                return True
            if board[x][y] =="O":
                return False
            y +=1 
    #위쪽    
    if direction ==2:
        while(x >=0):
            if board[x][y] =="S":
                return True
            if board[x][y] =="O":
                return False
            x -=1
        
    # 아래쪽
    if direction ==3:
        while(x<n):
            if board[x][y] =="S":
                return True
            if board[x][y] =="O":
                return False
            x+=1
#학생이 감지 되는지 확인
def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True #학생을 감지
    return False
result = "NO"
for data in combinations(spaces,3):
    for x, y in data:
        board[x][y] ="O"
    if not process():
        result = "YES"
        break
    for x, y in data:
        board[x][y] ="X"
print(result)