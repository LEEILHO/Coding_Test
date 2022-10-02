from collections import deque

def bfs(graph,node, visited):
    # deque라이브러리를 활용하여 큐 구현
    queue = deque([node])
    #현재 노드를 방문 처리
    visited[node] =True 
    
    #큐가 완전히 빌때까지
    while queue:
        #큐에 삽입된 순서대로 꺼내기
        v = queue.popleft()
        # 탐색 순서 출력
        print(v, end =' ')
        #현재 처리 중인 노드에서 방문하지 않은 인접 노드를 큐에 삽입
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i]  = True


graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)