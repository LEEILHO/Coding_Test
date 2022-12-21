N , M = map(int, input().split())
A =[]
B= []
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))   
result = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        result[i][j] = A[i][j] + B[i][j]
for i in result:
    for j in i:
        print(j,end = ' ')
    print()        
