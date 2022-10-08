""" 전보 
어떤 나라에는 N개의 도시 각 도시는 보내고자 하는 메시자 있는 경우 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송
C라는 도ㅗ시에서 위급 상황이 발생 최대한 많은 도시로 메시지를 보내고자 한다.
보낸 메시지를 받게 되는 도시의 개수는 몇개 이며 모두 받는데까지 걸리는 시간은?
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m,c = map(int, input().split())
graph = [[] for i in range(n+1)]

distance = [INF] *(n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
    
def dijkstra(start):
    q =[]
    heapq.heappush(q,(0,start))
    distance[start] =0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost = dist +i[1]
            
            if cost <  distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count =0
max_distance =0 
for d in distance:
    if d != INF:
        count +=1
        max_distance = max(max_distance,d)
print(count-1, max_distance)
