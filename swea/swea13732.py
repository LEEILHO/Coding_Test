#정사각형 판정
from collections import deque
T = int(input())

def bfs(square,arr):
    width = len(square) ** 0.5
    
    if width % 1 != 0:
        return "no"
    x,y = square.popleft()
    
    for i in range(x,x+int(width)):
        for j in range(y,y+int(width)):
            if arr[i][j] != "#":
                return "no"
    return "yes"
    
    

for test_case in range(1, T + 1):
    n = int(input())
    arr = list( (input()) for _ in range(n))
    square = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                square.append((i,j))
    result = bfs(square,arr)
    
    print(f"#{test_case} {result}")
        
                   