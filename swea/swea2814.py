def dfs(i,cnt):
    global max_v
    for j in range(1,N+1):
        if  visited[j]==0  and graph[i][j]:
            visited[j] =1
            dfs(j,cnt+1)
            visited[j] =0
        else:
            if cnt > max_v:
                max_v =cnt
        
T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    graph = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * N+1
    max_v =0
    for _ in range(M):
        x,y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    for i in range(1,N+1):
        visited[i] = 1
        dfs(i,1)
        visited[i] =0
    print(f"{tc} {max_v]")