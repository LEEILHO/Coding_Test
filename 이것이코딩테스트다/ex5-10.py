"""음료수 얼려 먹기
N xM 크기의 얼음 틀 구멍이 뚫려 있으면 0 칸막이 존재 1 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
생성되는 아이스크림의 개수를 구하는 프로그램을 작성하시오.
첫 째줄 얼음틀의 새로길이 N 가로길이 M 
두번째 줄부터 얼음틀의 형태
"""
n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))
# dfs로 특정한 노드를 방문한 뒤 연결된 모드 노드들도 방문
def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >=m:
        return False
    # 현재 노드 방문하지 않았다면
    if graph[x][y] ==0:
        graph[x][y] =1 # 방문 처리
        #상하좌우 재귀 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) ==True:
            result +=1
print(result)