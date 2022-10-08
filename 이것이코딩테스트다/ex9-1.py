# 간단한 다익스트라 알고리즘 소스 코드
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n,m = map(int, input().split())
#시작 노드 입력
start = int(input())
# 각노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 방문체크용 리스트
visited = [False] *(n+1)
# 무한으로 초기화한 거리 테이블
distance = [INF] * (n+1)


for _ in range(m):
    #a 번 노드에서 b번 노드로 가는 비용이 c
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
#방문하지 않은 노드 중에서 최단거리가 짧은 노드의 번호를 반환

def get_smallest_node():
    min_value = INF
    index =0 # 가장 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index =i
    return index

def dijkstra(start):
    distance[start] =0 #시작노드 초기화
    visited[start] = True #방문 처리
    for j in graph[start]: #시작노드에서 방문가능한 거리 
        distance[j[0]] = j[1]
    
    # 시작노드를 제외한 전체 n -1개의 노드에 대해 반복    
    for i in range(n-1): 
        now = get_smallest_node() #방문하지 않은 노드 중에서 가장 짧으 노드 번호
        visited[now] = True # 방문처리
        
        # 현재노드와 연결된 노드 확인
        for j in graph[now]: 
            # 비용 = 현재노드 까지 오는데의 비용 + 가는데의 비용
            cost = distance[now] + j[1]
            
            # 현재 노드를 거쳐서 가는 경우가 빠를 경우
            if cost < distance[j[0]]:
                distance[j[0]]  = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] ==INF:
        print("INFINITY")
    else:
        print(distance[i])