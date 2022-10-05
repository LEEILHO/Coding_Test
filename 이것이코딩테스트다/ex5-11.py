"""미로 탈출
N x M 크기의 직사각형 형태의 미로에 갇혀있음.
"""

from collections import deque

n,m = map(int,input().split())
graph = []
#graph 생성
for i in range(n):
    graph.append(list(map(int,input())))

#이동 방향 상 하 좌 우 
dx =[-1,1,0,0]
dy =[0,0,-1,1]


def bfs(x,y):
    queue = deque()
    #시작 노드 추가
    queue.append((x,y))
    # queue가 빌 때 까지
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 방향 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            # 범위를 벗어나면 무시
            if nx < 0 or ny<0 or nx >=n or ny >=m:
                continue
            # 괴물이 있는 곳이면 무시
            if graph[nx][ny] ==0:
                continue
            # 노드를 처음방문하는 경우 최단 거리 기록
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    return graph[n-1][m-1]





print(bfs(0,0))