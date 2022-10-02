# 리스트를 활용한 DFS 구현

def dfs(graph, start_node):
    need_visited, visited = list(), list()
    
    # 시작 노드 지정
    need_visited.append(start_node)
    
    # 방문이 필요한 노드가 있다면
    while need_visited:
        #가장 마지막 데이터 추출
        node = need_visited.pop()
        # 만약 노드가 방문되지 않았다면
        if node not in visited:
            # 방문 목록에 추가
            visited.append(node)
            # 노드에 연결된 노드들을 방문할리스트에 추가
            need_visited.extend(graph[node])
    return visited


# deque를 활용한 dfs 구현
from collections import deque
def dfs2(graph,start_node):
    visited = []
    need_visited = deque()

    #시작 노드 설정
    need.visited.append(start_node)

    # 방문이 필요한 리스트가 존재한다면
    while need_visited:
        # 시작 노드 지정
        node = need_visited.pop()
        # 만약 노드가 방문하지 않았다면
        if node not in visited:
            # 방문목록에 추가
            visited.append(node)
            # 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
    return visited

# 재귀함수를 통한 DFS 구현

def dfs_recursive(graph, start, visted= []):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited