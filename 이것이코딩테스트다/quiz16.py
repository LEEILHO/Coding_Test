""" 연구소 
NxM인 직사각형으로 연구소가 나타낼 수 있으며 직사각형은 1x1크기의 정사각형으로 나누어져있다
바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다. 세로 세울수 있는 벽의 개수는 3개
꼭 3개를 세워야한다. 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최대값을 구하는 프로그램
첫째줄에 세로 크기 N 가로크기 M
0 빈칸 1 벽 2 바이러스
"""
from collections import deque
from copy import deepcopy
from itertools import combinations
n,m = map(int,input().split())
data =[]
for i in range(n):
    data.append(list(map(int,input().split())))
empty = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def virus(x,y):
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if nx >=0 and nx < n and ny>=0 and ny <m:
            if new_data[nx][ny] ==0:
                new_data[nx][ny] =2
                virus(nx,ny)
for i in range(n):
    for j in range(m):
        if data[i][j] ==0:
            empty.append((i,j))
combination_walls = list(combinations(empty,3))

result =0
for walls in combination_walls:
    new_data = deepcopy(data) 
    for wall in walls:
        x,y = wall[0],wall[1]
        new_data[x][y] =1
    for i in range(n):
        for j in range(m):
            if new_data[i][j] ==2:
                virus(i,j)
    score =0
    for i in range(n):
        for j in range(m):
            if new_data[i][j] ==0:            
                score+=1
    result = max(result,score)
print(result)    
    