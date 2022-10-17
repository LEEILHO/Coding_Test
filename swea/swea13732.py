#정사각형 판정
from collections import deque
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = list( (input()) for _ in range(n))
    square = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                square.append((i,j))
    for i in square:
        
                   