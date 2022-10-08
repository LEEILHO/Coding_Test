"""미래도시
1번부터 N번 까지의 회사가 있음 특정회사 끼리는 도로를 통해 연결 A는 현재 1번 회사 X번 회사에 방문해 물건을 판매  
양방향으로 이동가능 시간은 1 A는 1 -> K -> X 를 이동
최소 시간을 계산하는 프로그램을 작성하시오
첫째 줄 N 경로의 개수 M 둘쨰줄부터 M+1 연결된 회사의 공백  셋째줄 X, K"""
#플로이드 워셜 알고리즘 이용
n,m = map(int,input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] =0
            
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] =1
    graph[b][a] =1

x,k = map(int, input().split())


for i in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][i]+graph[i][b])


result = graph[1][k] +graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)
    