""" 금광
n X m 크기의 금광  각 칸은 특정한 크기의 금이 들어 있다. 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작 
맨 처음에는 첫 번째 열의 어느 행에서든 출발 이후 m번에 걸쳐 오른쪽 위 ,오른쪽,오른쪽 아래 3 가지 중 하나의 위치로 이동
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램"""
T = int(input())
for tc in range(T):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    mine = []
    for i in range(n):
        mine.append(list(arr[i*m: (i+1)*m ]))
    
    for j in range(1,m):
        for i in range(n):
            if i ==0:
                left_up =0
            else:
                left_up = mine[i-1][j-1]
            if i==n-1:
                left_down =0
            else:
                left_down = mine[i+1][j-1]
            left = mine[i][j-1]
            mine[i][j] += max(left_up,left_down,left)
    
    result = []
    for i in range(n):
        result.append(mine[i][m-1])
    answer = max(result)
    print(answer)
                
            
        
    