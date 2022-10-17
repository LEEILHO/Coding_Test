""" 특정 거리의 도시 찾기
어떤 나라에는 1~ N번까지의 도시와 M개의 단방향 도로 존재
모든 도로의 거리는 1
이때 특정 도시 x로부터 출발하여 도달할 수 있는 모든 도시 중 에서 최단거리가 정확히 K인 모든 도시의 번호를 출력하는 
프로그램을 작성하시오. x-> x 는 항상 0이라 가정
첫째 줄에 도시의 개수 2<=N<=300,000, 도로의 개수 1<=M <=1,000,000, 거리 정보 1<=k <=300,000 , 1<=x<=n
둘째 줄부터 M개의 줄에 걸쳐서 두개의 자연수 A,B가 주어지며, 각 자연수는 공백으로 구분
출력 조건 X부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나 씩 오름 차순으로 출력
최단거리 K인 도시 가 하나도 존재하지 않으면 -1 출력 
"""
from collections import deque
#BFS 알고리즘 이용
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for road in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    
#거리 무한으로 초기화
distance = [1e9] * (n+1)
#시작 도시의 거리 0으로 초기화
distance[x] =0

q = deque([x])
#큐가 존재할 때까지
while q:
    now = q.popleft()
    # 현재 도시 와 연결된 도시들 확인
    for next in graph[now]:
        # 연결된 도시가 방문하지 않은 도시라면
        if distance[next] == 1e9:
            # 최단 거리 갱신
            distance[next] = distance[now] +1
            q.append(next)

check = False
for i in range(1, n+1):
    if distance[i] ==k:
        print(i)
        check = True
if check== False:
    print(-1)