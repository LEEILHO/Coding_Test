# 개선된 다익스트라 알고리즘
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수 간선의 개수
n,m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

# 모든 간선 정보 입려력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q =[]
    #시작 노드설정
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        
        dist, now = heapq.heappop(q)
        # 현재노드가 이미 처리 되었으면 무시
        if distance[now] < dist:
            continue
        # 현재노드와 연결된 노드 확인
        for i in graph[now]:
            cost = dist +i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])