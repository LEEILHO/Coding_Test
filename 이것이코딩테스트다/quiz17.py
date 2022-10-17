""" 경쟁적 전염
NxN 크기의 시험관 바이러스의 종류는 1~K번 까지 K가지가 있으며 모든 바이러스는 이 중 하나에 속함
모든 바이러스는 1초마다 상,하, 좌,우의 방향으로 증식 번호가 낮은 종류의 바이러스부터 증식 이미 바이러스가 있다면 
다른 바이러스는 들어갈 수 없다 
시험관의 크기와 바이러스의 위치정보가 주어졌을 때 S초가 지난 후 예 (x,Y)에 존재하는 바이러스의 종류를 출력
존재 하지 않는 다면 0을 출력"""
from collections import deque
import graphlib
n,k = map(int,input().split())
virus = []
for i in range(n):
    virus.append(list(map(int,input().split())))
s,x,y = map(int,input().split())
x -=1
y -=1
seequence_virus = []
for i in range(n):
    for j in range(n):
        if virus[i][j] != 0:
            seequence_virus.append((virus[i][j],0,i,j))
seequence_virus.sort()
q = deque(seequence_virus)
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while q:
    now_virus,now_s,now_x,now_y = q.popleft()
    
    if now_s ==s:
        break
    
    for i in range(4):
        nx = now_x+ dx[i]
        ny = now_y+ dy[i]
        if 0<=nx and nx<n and 0<= ny and ny<n:
            #방문하지 않았다면
            if virus[nx][ny] ==0:
                virus[nx][ny] = now_virus
                q.append((now_virus,now_s+1,nx,ny))

print(virus[x][y])
                
                
 


