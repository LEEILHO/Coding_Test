""" 도시 분할 계획
동물원에서 막 탈출한 원숭이 한 마리 세상구경을 하고있다. 마을은 N개의 집과 그집들을 연결하는 M개의 길로 이루어져있따
길을 유지하는데 유지비가 있다. 양방향 
마을을 2개로 분할 각 마을안에 집들이 서로 연결되도록 분할, 마을 안의 두집사이에 경로가 항상 존재해야한다.
마을에는 집이 하나 이상 있어야한다. 분리된 두마을 사이에 있는 길들은 필요가 없어 없앰 길을 없애고 유지비의 합을 최소로 하고 싶음
"""
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if (a > b):
        parent[a] = b
    else:
        parent[b] = a

n,m = map(int,input().split())
parent = [0]*(n+1)
edges = []
result =0
for i in range(1,n+1):
    parent[i] = i
for i in range(m):
    a,b, cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
last =0
for edge in edges:
    cost,a,b = edge 
    if find_parent(parent,a) != find_parent(parent,b):
        union(parent,a,b)
        result += cost
        last =cost
print(result -last)