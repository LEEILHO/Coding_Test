""" 플로이드
n 개의 도시가 있고 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있따
모든 도시의 쌍에 대해서 도시 A에서 B로 가는 비용의 최솟값을 구하시오"""
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1,n+1):
    for b in range(1,n+1):
        if a ==b:
            graph[a][b] =0
for i in range(m):
    a,b,c = map(int, input().split())
    if graph[a][b] > c :
        graph[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end = " ")
        else:
            print(graph[a][b], end =" ")
    print()