""" 인구 이동
N X N 크기의 땅이 있고 각각의 땅에는 나라가 하나씩 존재 하며 r행 c열에 있는 나라에는 A[r][c]명이 살고 있다
오늘 부터 인구 이동이 시작 
국경선을 공유하는 두 나라 인구 차이가 L명 이상 R명 이하라면, 두나라가 공유하는 국경선을 오늘 하루 동안 개방
국경선이 모두 열리면 인구 이동을 시작
국경선이 열려 있어 인접한 칸만을 이용해 이동 할 수 있으면 그나라를 오늘 하루 동안 은 연합
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수)/ (연합을 이루고 있는 칸의 개수 편의상 소수점은 버림)
연합 해체, 국경선 닫기
첫 째 줄에 N,L,R이 주어지고
둘째줄 부터 N개의 줄에 각 나라의 인구수
인구이동이 몇번 일어나나 출력
"""
from collections import deque
n,l,r = map(int, input().split())
populations =[]
for _ in range(n):
    populations.append(list(map(int,input().split())))
#상하좌우
dx = [-1,1,0,0]
dy =[0,0,-1,1]
result =0
def process(x,y,index):
    united =[]
    united.append((x,y))
    q = deque()
    q.append((x,y))
    union[x][y] = index
    summary = populations[x][y]
    count =1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx <n and ny >=0 and ny < n and union[nx][ny] ==-1:
                if l <= abs(populations[nx][ny]- populations[x][y]) <=r:
                    q.append((nx,ny))
                    union[nx][ny] =  index
                    summary += populations[nx][ny]
                    count +=1
                    united.append((nx,ny))
    for i, j in united:
        populations[i][j] = summary //count
    return count




total_count =0
while True:
    union = [[-1] * n for _ in range(n)]
    index =0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index +=1
    if index == n * n:
        break
    total_count +=1
print(total_count)